# ClosetAI - AI Deep Dive: The Heart of the Recommendation Engine

## TL;DR

The core problem is: given 50 clothing items, which 3-4 should you wear together today? This breaks into 7 layers, each with a different AI approach. Phases 1-2 need zero ML engineers — just APIs, math, and pre-trained models. Phase 3 (custom models) is optional and only triggers at 10K+ users. Humans only agree 71-82% of the time on what's a "good outfit," so 70-75% recommendation accuracy already approaches the ceiling.

---

## The Core Problem (Deceptively Simple)

Everything in ClosetAI — the closet, the Style DNA, the shopping — exists to make one answer better:

> **"What should I wear today?"**

That single question is actually 5 stacked problems:

| Sub-problem | Question | Difficulty |
|-------------|----------|------------|
| Item Understanding | What IS this clothing? | Solved (Vision APIs) |
| Compatibility | Do these items work together? | Hard (the core challenge) |
| Context Matching | Is this right for today? | Easy (rules) |
| Personalization | Does this match what THIS user likes? | Medium (needs data) |
| Novelty | Is this fresh? | Easy (database query) |

---

## How Others Have Tried to Solve This

### Stitch Fix (The Cautionary Tale)

The biggest fashion AI company ever built. $2B+ valuation at peak.

**What they built:**
- 80-100 PhD data scientists (math, neuroscience, astrophysics)
- Hybrid human-AI system: ML narrows options, human stylists make final picks
- Collaborative filtering + mixed-effects models + deep learning + NLP pipeline
- 90+ data points collected per user at signup
- By 2024, AI handled 75% of selections

**Key numbers:**
- 63% match score (probability a client keeps a specific item)
- 85% accuracy on fashion trend forecasting
- 83-86% repeat purchase rates

**What happened:**
- Jan 2023: 20% workforce laid off, CEO stepped down
- Distribution centers closed (950+ jobs gone)
- Jan 2024: All full-time stylists moved to part-time only
- Revenue in decline

**Lesson:** 100 data scientists couldn't save a business with poor unit economics. Product-market fit and habit formation matter more than model accuracy.

### Amazon Echo Look (The Failure)

$200 camera for your bedroom. "Alexa, how do I look?"

**Why it died (discontinued July 2020, 3 years after launch):**
- Privacy concerns: camera on your bedroom dresser, no physical lens shutter
- AI quality was poor: reviewers said it made "tone-deaf style choices"
- Narrow product-market fit: dedicated $200 hardware for a use case people do 2x/week
- Widely perceived as a data-collection play to sell Amazon Fashion

**Lesson:** Fashion AI needs to be embedded in existing workflows, not a standalone device. The quality bar is very high because people are emotionally invested in how they look. Binary "which is better" comparisons are too simplistic.

### Academic Research (The Benchmarks)

The Polyvore dataset was the gold standard — 21,889 human-curated outfits, 126,054 items. The site shut down in 2018 but the dataset lives on.

**State-of-the-art accuracy on Polyvore (2024):**

| Model | Fill-in-the-Blank Accuracy | Compatibility AUC | Year |
|-------|---------------------------|-------------------|------|
| Random baseline | 25.0% | 0.50 | — |
| Type-Aware Embeddings | 57.8% | 0.88 | 2018 |
| OutfitTransformer | 67.1% | 0.93 | 2023 |
| OutfitTransformer + CLIP | 69.2% | 0.95 | 2024 |

**Critical insight:** Even state-of-the-art gets only ~69% on "pick the right item for this outfit." That means the best models in the world get 1 in 3 wrong.

**But here's the thing:** Human agreement on "is this a good outfit?" is only **71-82%** (measured by Spearman correlation between annotator groups, SIGGRAPH Asia 2024). Fashion is subjective. There is no objectively correct answer. Approaching 70% accuracy means you're approaching the ceiling of what's meaningful.

### Plain LLMs on Fashion (The Surprising Data)

A 2024 paper ("Decoding Style") tested LLMs directly on outfit compatibility:

| Approach | Fill-in-the-Blank | Compatibility AUC |
|----------|-------------------|-------------------|
| Plain LLM (zero-shot) | 29% (near-random!) | 57.9% |
| LoRA fine-tuned LLM | 49% | 62.3% |
| LoRA + DPO (preference tuning) | 61% | 81.0% |
| Specialized model (OutfitTransformer) | 69% | 95.0% |

**A plain LLM is essentially random at outfit compatibility.** But fine-tuning gets it to 61%, and specialized models hit 69%. The gap between 61% and 69% costs months of ML engineering. The human ceiling is ~75%.

### GPT-4V on Fashion Aesthetics (SIGGRAPH Asia 2024)

- Raw accuracy: 53-74% (varies by dataset)
- After calibration: 60-99%
- Key weakness: struggles ranking outfits with similar colors
- Key strength: excellent at explaining WHY something works

---

## Color Harmony: The Surprising Science

### Traditional Color Theory is Empirically Wrong

Itten's color wheel (complementary, analogous, triadic) is what every wardrobe app uses. Research shows it's flawed:
- Itten's "complementary" pairs don't match perceptual complements
- One classical model was "almost non-correlated" with modern aesthetic preferences

### What Actually Works

**"The Science of Style" (PLOS ONE, 2014):**
- 239 participants, 30 color combinations each
- Found a robust quadratic effect: **maximum fashionableness at MODERATE color coordination**
- Neither matchy-matchy nor clashing was preferred — the Goldilocks principle
- This effect accounted for 2x the variance of a simple linear model

**Practical implication:** Don't hardcode color wheel rules. Instead:
- Convert to LAB color space (perceptually uniform)
- Score for moderate color distance (not too similar, not too different)
- 2-3 colors per outfit is the sweet spot
- LLMs are surprisingly good at color reasoning because they've ingested millions of styling articles

---

## The 7 Layers of Our AI Pipeline

### Layer 1: Item Understanding (Claude Vision API)

**What:** Photo → category, color, pattern, material, formality, occasions

**Approach:** Claude Vision / GPT-4o API call with structured JSON output

**Accuracy:** 85-95% on category and color, 70%+ on material

**Enhancement:** Background removal before analysis:
- Development: rembg with BiRefNet model (free, ~87% IoU)
- Production: fal.ai RMBG-2.0 ($0.002/image, ~90% IoU)
- Do NOT use rembg's default U2-Net — drops to 39% IoU on diverse images

**Cost:** ~$0.003/item

**ML needed? No. API calls + good prompts.**

### Layer 2: Color Harmony Scoring (Math)

**What:** Do these colors work together?

**Approach:**
```python
# Convert dominant_colors to LAB color space
# Calculate pairwise color distance (Delta E)
# Score using "moderate matching" heuristic:
#   - Delta E 20-60: high harmony (moderate contrast)
#   - Delta E 0-20: too matchy (penalize slightly)
#   - Delta E 60+: clashing (penalize more)
# Neutral colors (black, white, grey, navy, beige) are wildcards
# Bonus for 2-3 color outfits, penalty for 4+
```

**Why not ML here:** Color harmony is well-studied mathematically. The PLOS ONE research gives us a clear, empirically-validated scoring function. No need to train a model for something math handles well.

**ML needed? No. Pure math (color science).**

### Layer 3: Outfit Candidate Generation (Rules + Scoring)

**What:** Given 50 items, generate the top 10 possible outfit combinations

**Approach:**
```python
# 1. Category constraint
#    Strategy A: top + bottom (+optional outerwear, shoes, accessory)
#    Strategy B: dress (+optional outerwear, shoes, accessory)
#    Strategy C: ethnic set (kurta+bottom / saree / lehenga)

# 2. Weather/season filter
#    If temp > 30°C: exclude "winter" tagged items
#    If rain forecast: boost waterproof materials, closed shoes

# 3. Score each candidate (0-100):
score = (
    formality_consistency * 20  # items within ±1 formality level
    + color_harmony * 25        # from Layer 2
    + occasion_fit * 20         # all items match target occasion
    + freshness * 15            # not worn in last 7 days
    + variety * 10              # mix of textures/patterns
    + user_preference * 10      # similar to previously accepted
)

# 4. Sort by score, return top 10
```

A 50-item wardrobe generates maybe 100-500 valid combinations. Score, rank, take top 10. This runs in milliseconds with zero AI cost.

**ML needed? No. Filtering + arithmetic.**

### Layer 4: Outfit Ranking + Reasoning (LLM — The Magic Layer)

**What:** Take 10 candidates → rank top 3-5 with natural language reasoning

**This is where Claude earns its keep.**

```
Prompt:
"You are a personal stylist for {name}. Style archetype: {archetype}.

Here are 10 outfit candidates for today:
{candidates with item descriptions, colors, formality}

Context:
- Weather: {temp}°C, {condition}
- Occasion: {calendar_event or primary_occasion}
- Recently worn: {last 5 outfits}
- Preferences: {from style DNA + feedback history}

Rank the top 5 outfits. For each:
1. Ranking
2. One sentence explaining why it works
3. A styling tip

Return as JSON."
```

**Why this works:** Claude has ingested millions of fashion articles, styling guides, and outfit advice. It won't beat OutfitTransformer on a Polyvore benchmark, but it gives reasonable, explainable suggestions. And the explanation is half the value — "here's WHY this works" builds trust and teaches users about style.

**Why we don't just use Claude for everything:** A plain LLM scores 29% on outfit compatibility (near-random). By doing Layers 1-3 first (rules + color science + scoring), we pre-filter to the best 10 candidates. Claude only needs to rank 10 good options, not pick from 500 random ones. This dramatically improves quality while keeping cost low.

**Cost:** ~$0.005 per ranking

**ML needed? No. API call with well-crafted prompt.**

### Layer 5: Personalization / Learning (Simple Tracking → Light ML)

**What:** Learn from accept/reject patterns to improve over time

**Phase 1 — Simple version (no ML):**
```python
# Track what user accepts and rejects
# Build preference weights:

preferences = {
    "color_combos": {
        ("navy", "white"): +3,     # accepted 3 times
        ("red", "orange"): -2,     # rejected 2 times
    },
    "pattern_mixing": -1,           # usually rejects pattern-on-pattern
    "formality_bias": +0.5,         # prefers slightly more formal
    "max_items": 3,                 # prefers simpler outfits
}

# Apply as bonus/penalty in Layer 3 scoring
```

This is just counting and adjusting weights. A database query, not a model.

**Phase 2 — Embedding version (light ML):**
- Use Marqo-FashionSigLIP (pre-trained, free, on HuggingFace) to embed each item
- Items the user wears together → pull embeddings closer (simple vector math)
- Items rejected together → push apart
- Over time, the embedding space personalizes

**ML needed? Phase 1: no. Phase 2: light (pre-trained model inference only).**

### Layer 6: Style Similarity & Discovery (Pre-trained Embeddings)

**What:** "Items similar to this" and "People with your Style DNA also wear..."

**Approach:**
1. Embed all items with FashionSigLIP on upload (one-time cost)
2. Store vectors in Supabase with pgvector extension
3. Query nearest neighbors for similarity

**Real-world validation:** Mercari (Japanese marketplace) did exactly this with fine-tuned SigLIP. Results: **+50% click-through rate, +14% conversion rate.**

**Marqo-FashionSigLIP (2024) benchmarks:**
- +57% improvement in MRR over FashionCLIP 2.0
- Category-to-product precision@1: 75.8%
- Available free on HuggingFace, no training needed

**ML needed? No training. Just inference with a pre-trained model.**

### Layer 7: Custom Compatibility Model (Real ML — Maybe Never)

**What:** Train a model specifically on "outfits our users accepted" vs "outfits they rejected"

**When to trigger:** Only after 10K+ users with 6+ months of data

**What it looks like:**
- OutfitTransformer architecture (or similar)
- Train on our accept/reject data
- Replaces or supplements Layer 3 scoring

**Reality check:** The gap between "well-prompted LLM + good rules" (~70% satisfaction) and "custom trained model" (~80% satisfaction) is small relative to the engineering cost. Stitch Fix needed 80+ data scientists. We probably never need this layer if Layers 1-6 work well.

**ML needed? Yes, real ML expertise. Hire a contractor for 2-4 weeks if you get here.**

---

## The Quality Equation

### What "Amazing Recommendations" Actually Means

Users don't evaluate recommendations on a benchmark. They evaluate on feeling:

```
"Amazing" = Right items + Right context + Good explanation + Surprise element

Right items:     The clothes actually go together (color, formality, style)
Right context:   Appropriate for weather, occasion, what they wore recently
Good explanation: "This works because..." builds trust and teaches
Surprise element: "I wouldn't have thought of that!" creates delight
```

### The Quality Stack

```
70% of quality comes from: NOT showing bad outfits
   → Layer 3 (rules) eliminates the obviously wrong combinations
   → This alone makes you better than "staring at closet"

20% of quality comes from: RANKING good outfits well
   → Layer 4 (Claude) picks the best from pre-filtered candidates
   → Explanations make even imperfect picks feel intentional

10% of quality comes from: LEARNING over time
   → Layer 5 (feedback tracking) stops repeating mistakes
   → This creates the "it's getting to know me" magic
```

### The Bar We Need to Clear

We're not trying to beat a human stylist. We're trying to beat **"stare at closet for 10 minutes and pick the same 5 outfits on rotation."**

That's a much lower bar. A 70% "good enough" recommendation that saves 10 minutes every morning is enormously valuable. And with explanations like "this works because navy + cream creates visual contrast for your warm skin tone," even a non-perfect recommendation teaches the user something.

---

## Background Removal: Table Stakes

Every clothing photo needs background removal before analysis and display. Clean, isolated garment photos make the closet look premium AND improve AI tagging accuracy.

### Options Compared

| Solution | Quality (IoU) | Speed | Cost | Best For |
|----------|--------------|-------|------|----------|
| rembg (U2-Net default) | 39% on diverse images | Fast | Free | DON'T USE — unreliable |
| rembg (BiRefNet model) | 87% | ~800ms | Free | Development / MVP |
| fal.ai RMBG-2.0 (Bria) | 90% | Fast | $0.002/image | Production |
| Photoroom API | ~90%+ | 300ms | $0.02-0.10/image | Premium quality |

**Recommendation:**
- MVP: rembg with BiRefNet model (free, good enough)
- Production: fal.ai RMBG-2.0 ($0.002/image, best value)
- Critical: never use rembg's default U2-Net — it's unreliable on non-portrait images

---

## Fashion Embeddings: The Secret Weapon

### What They Are

A "fashion embedding" converts a clothing image into a vector (list of numbers) that captures its visual style. Similar items have similar vectors. This enables:
- "Find items similar to this" (nearest neighbor search)
- Style compatibility scoring (how well do these vectors "go together"?)
- User style profiling (average of worn item vectors = style preference)
- "People like you also wear..." (user vector similarity)

### Best Available Model (2024)

**Marqo-FashionSigLIP:**
- Fine-tuned from SigLIP on 1M+ fashion items
- 7-part loss function (keywords, categories, colors, materials, descriptions)
- +57% MRR improvement over FashionCLIP 2.0
- Free on HuggingFace
- No training needed — just run inference

### How We'd Use It

```python
# On item upload:
embedding = fashion_siglip.encode(item_image)  # 768-dim vector
store_in_supabase(item_id, embedding)           # pgvector column

# For "items like this":
similar = supabase.rpc('match_items', {
    'query_embedding': embedding,
    'match_threshold': 0.8,
    'match_count': 10
})

# For outfit compatibility:
# High cosine similarity between items = similar style
# Moderate similarity = complementary (often what you want)
# Low similarity = clashing (usually bad, but sometimes creative)
```

### When to Add This

Phase 2 (months 4-6). It's not needed for MVP but significantly improves recommendation quality and enables features like "items similar to this" and "complete the look."

---

## Can We Do This Without ML Engineers?

### Phase 1 (Months 1-3): Absolutely Yes

| Component | Approach | Complexity |
|-----------|----------|------------|
| Item tagging | Claude Vision API | API call |
| Background removal | rembg (BiRefNet) | Library call |
| Color harmony | LAB color math | ~50 lines of Python |
| Outfit generation | Rule-based scoring | ~200 lines of Python |
| Outfit ranking | Claude API | API call + prompt |
| Personalization | Weighted feedback counts | Database queries |

**Total AI/ML code: ~300 lines of Python + API calls.** No training, no GPUs, no PhD.

**Expected satisfaction: ~70-75%** (approaching human agreement ceiling of ~80%)

### Phase 2 (Months 4-6): Yes, With Effort

| Component | Approach | Complexity |
|-----------|----------|------------|
| Fashion embeddings | FashionSigLIP (pre-trained) | Download model, run inference |
| Vector storage | Supabase pgvector | SQL extension |
| Style similarity | Cosine similarity | Math |
| Better personalization | Feedback-weighted embeddings | Vector arithmetic |
| Production bg removal | fal.ai RMBG-2.0 | API call |

**New skills needed:** Understanding embeddings conceptually, running PyTorch inference, pgvector queries. Learnable in a weekend.

**Expected satisfaction: ~75-80%**

### Phase 3 (Months 7-12): Maybe, If Needed

| Component | Approach | Complexity |
|-----------|----------|------------|
| Custom compatibility model | Train on user data | Real ML engineering |
| Fine-tuned embeddings | Train on Indian fashion | GPU infrastructure |
| Explore/exploit | Bandit algorithms | Statistics |

**When to trigger:** Only if Phase 1+2 users consistently say "recommendations are okay but not great" AND you have 10K+ users generating training data.

**If needed:** Hire an ML contractor for 2-4 weeks. By this point you'll have revenue to afford it.

**Expected satisfaction: ~80-85%**

---

## The Stitch Fix Lesson (Why This Matters)

Stitch Fix had:
- 80-100 PhD data scientists
- Millions of users
- Hundreds of millions in revenue
- The best fashion recommendation models in the world

And they still:
- Laid off 20% of staff
- Lost their CEO
- Moved all stylists to part-time
- Saw revenue decline

**Why?** Because model accuracy isn't what makes a fashion product work. What makes it work:
1. **Daily habit formation** (morning notification → open → wear → done)
2. **Trust through explanation** ("here's why" matters more than being right)
3. **Low friction** (photo → auto-tag → done, not manual entry)
4. **Emotional connection** ("this app gets me")
5. **Compounding value** (gets better the more you use it)

A 70% accurate system with beautiful UX and great explanations beats a 90% accurate system in an ugly app. Every time.

---

## Summary: The Honest Roadmap

```
Phase 1 (Months 1-3):
  Rules + Claude API
  No ML training, no GPUs
  ~70-75% satisfaction
  YOU AND I CAN BUILD THIS

Phase 2 (Months 4-6):
  Add pre-trained embeddings (FashionSigLIP)
  Still no ML training
  ~75-80% satisfaction
  YOU AND I CAN BUILD THIS (with some learning)

Phase 3 (Months 7-12):
  Custom models IF needed AND if data exists
  Hire ML contractor for 2-4 weeks
  ~80-85% satisfaction
  MAYBE NEED HELP (but might never need this)

Human agreement ceiling: ~75-82%
Anything above 75% is approaching "as good as asking a friend"
```

The heart of the app isn't a model — it's the daily habit of opening ClosetAI, seeing an outfit that makes sense, understanding WHY it works, and starting your day with confidence. That's built with product design and UX, not PhDs.
