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

**What they built (detailed architecture from their Algorithms Tour):**
- 80-100 PhD data scientists (math, neuroscience, astrophysics) — data science reported directly to CEO
- **Layer 1: Collaborative Filtering** — classic CF augmented with photographic data (Pinterest boards), textual feedback, and inventory photos
- **Layer 2: Mixed-Effects Models** — longitudinal modeling of preferences over time, separating latent factors for the stylist, the client, and their specific interaction
- **Layer 3: Latent Factor Decomposition** — matrix factorization assuming k latent factors, reducing complexity from O(m*n) to O(k*(m+n))
- **Layer 4: Deep Learning** — two neural network hidden layers on top of pooled set representations + contextual features, with softmax output for selection probabilities
- **Layer 5: NLP Pipeline** — OpenAI embeddings (as of 2023) to interpret freeform client text. GPT-4 generates concise recaps of client history for stylists. 4.5 billion+ textual data points collected (more text than all of Wikipedia)
- **Layer 6: Outfit Creation Model (OCM)** — generative AI model trained on millions of stylist-created outfits, considering real-time inventory and client preferences
- **Style Shuffle** ("Tinder for clothes"): swipe right/left on outfit images to train visual preferences
- **Evolutionary algorithms** for new styles: "recombination and mutation" of style attribute "genes" with a fitness measure, vetted by human designers before production
- By 2024, AI handled 75% of selections. Stylists retained override power.

**Key numbers:**
- 63% match score (probability a client keeps a specific item)
- 85% accuracy on fashion trend forecasting
- 83-86% repeat purchase rates
- Net revenue per active client: ~$488-525
- 90+ data points collected per user at signup

**What happened:**
- Jan 2023: 20% workforce laid off, CEO stepped down
- Distribution centers closed (393 jobs in Bethlehem, 558 in Dallas)
- Jan 2024: All 2,620 full-time stylists moved to part-time only
- Revenue in decline — a cautionary tale about how hard fashion AI is even with 100 data scientists

**Lesson:** 100 data scientists couldn't save a business with poor unit economics. Product-market fit and habit formation matter more than model accuracy. Their most important insight: "A good person plus a good algorithm is far superior to the best person or the best algorithm alone."

**Sources:**
- [Stitch Fix Algorithms Tour](https://algorithms-tour.stitchfix.com/)
- [Stitch Fix Multithreaded Blog](https://multithreaded.stitchfix.com/algorithms/blog/)
- [DataCamp: Data Science at Stitch Fix](https://www.datacamp.com/podcast/data-science-at-stitch-fix)
- [Stitch Fix Latent Style](https://multithreaded.stitchfix.com/blog/2018/06/28/latent-style/)
- [Stitch Fix Generative AI Announcement](https://newsroom.stitchfix.com/blog/how-were-revolutionizing-personal-styling-with-generative-ai/)

### Amazon Echo Look (The Failure)

$200 hands-free camera for your bedroom dresser. Launched April 2017. "Alexa, how do I look?"

**How Style Check worked:**
- Combined ML algorithms with advice from fashion specialists
- User submitted two outfits side-by-side, AI recommended one
- Response took ~1 minute, included explanations for the choice
- Exact algorithm never disclosed publicly

**Why it died (ceased functioning July 24, 2020, 3 years after launch):**
- Privacy concerns: camera on your bedroom dresser, no physical lens shutter
- AI quality was poor: reviewers consistently said Style Check "isn't very useful" and made "tone-deaf style choices"
- Narrow product-market fit: dedicated $200 hardware for a use case people do 2x/week
- Widely perceived as a data-collection play to sell Amazon Fashion inventory
- Users received a free Echo Show 5 as compensation when it shut down
- Style features were migrated to the Amazon Shopping app

**Lessons:**
- Fashion AI needs to be embedded in existing workflows, not a standalone hardware device
- The quality bar for fashion advice is very high because people are emotionally invested in how they look
- Binary "which is better" comparisons are too simplistic — users need nuanced, contextual advice
- Privacy sensitivity is extreme for bedroom/closet contexts

**Sources:**
- [VoiceBot: Amazon Echo Look No More](https://voicebot.ai/2020/05/29/amazon-echo-look-no-more/)
- [VentureBeat: Amazon Discontinues Echo Look](https://venturebeat.com/ai/amazon-discontinues-the-echo-look-and-migrates-ai-style-recommendations-to-other-apps-and-devices)
- [TechHive: Echo Look Review](https://www.techhive.com/article/583385/amazon-echo-look-review-this-alexa-manifestation-is-great-for-taking-selfies-but-you-can-t-trust-it.html)

### Academic Research (The Benchmarks)

**The Polyvore Dataset:**

Polyvore.com was a fashion social platform where users created "sets" — curated outfits composed of individual items. Acquired by SSENSE and shut down in 2018. Before shutdown, researchers crawled it to create the most important benchmark dataset in fashion AI.

- **21,889 outfits** (17,316 train / 1,497 validation / 3,076 test)
- **126,054 items** across **380 raw categories** (filtered to 120 appearing 100+ times)
- Each item has: product image, text description, category label
- Two versions: **Polyvore Outfits** (items may overlap train/test) and **Polyvore Disjoint** (no overlap — harder, more realistic)
- Standard tasks: Fill-in-the-Blank (FITB) and Compatibility Prediction (CP AUC)

**State-of-the-art accuracy on Polyvore (2024):**

| Model | Fill-in-the-Blank Accuracy | Compatibility AUC | Year | Key Innovation |
|-------|---------------------------|-------------------|------|----------------|
| Random baseline | 25.0% | 0.50 | — | — |
| Type-Aware Embeddings | 57.8% | 0.88 | ECCV 2018 | Type-pair-specific subspaces (compatibility isn't transitive — shoes matching a top must be close in "shoe-top" space) |
| CSA-Net | 63.7% | — | 2020 | Cross-attention for set compatibility |
| NGNN ("Dressing as a Whole") | — | — | WWW 2019 | Node-wise GNN where edge transformations determined by BOTH connected nodes. Supports visual + textual + multimodal |
| HFGN (Hierarchical Fashion Graph) | — | — | SIGIR 2020 | Three-level hierarchy: users → outfits → items. Jointly models item compatibility AND user preference |
| OutfitTransformer | 67.1% | 0.93 | WACV 2023 | Contrastive learning with transformer. +15.7-19.4% CP improvement, +6.5-9.7% FITB over prior SOTA |
| OutfitTransformer + CLIP | 69.2% | 0.95 | 2024 | Vision-language pre-training boost |
| Hybrid Multimodal Framework | 69.2% | 0.95 | 2024 | Multi-modal fusion |

**On the harder Polyvore Disjoint split:** FITB ~53-57%, CP AUC ~0.81-0.83. No item overlap makes this more realistic but significantly harder.

**Other notable approaches:**
- **WhisperLite (Amazon)**: Contrastive learning to capture user intent from natural language. Composite loss (BCE + contrastive). Significant improvement on real-world Amazon fashion data.
- **FND (False Negative Distillation)**: Contrastive framework with data augmentation for outfit data sparsity.

**Critical insight:** Even state-of-the-art gets only ~69% on "pick the right item for this outfit." The best models in the world get 1 in 3 wrong.

**But here's the thing:** Human agreement on "is this a good outfit?" is only **71-82%** (measured by Spearman correlation between annotator groups, SIGGRAPH Asia 2024). Fashion is subjective. There is no objectively correct answer. Approaching 70% accuracy means you're approaching the ceiling of what's meaningful.

**The benchmark gap:** No major dataset exists for Indian fashion. Polyvore is Western-centric, IQON is Japanese, iFashion is Chinese (Alibaba/Taobao). This means every competitor's model is trained on Western fashion data — our Indian cultural context (see CREATIVE_AI_AND_TRENDS.md) is a genuine moat.

**Sources:**
- [Polyvore Dataset GitHub](https://github.com/xthan/polyvore-dataset)
- [Fashion Recommendation: Outfit Compatibility using GNN (2024)](https://arxiv.org/html/2404.18040v1)
- [Type-Aware Embeddings (ECCV 2018)](https://arxiv.org/pdf/1803.09196)
- [OutfitTransformer (WACV 2023)](https://openaccess.thecvf.com/content/WACV2023/papers/Sarkar_OutfitTransformer_Learning_Outfit_Representations_for_Fashion_Recommendation_WACV_2023_paper.pdf)
- [HFGN (SIGIR 2020)](https://arxiv.org/pdf/2005.12566)
- [NGNN "Dressing as a Whole" (WWW 2019)](https://arxiv.org/abs/1902.08009)
- [A Review of Explainable Fashion Compatibility](https://dl.acm.org/doi/10.1145/3664614)

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

- Raw accuracy: **53-74%** (varies by dataset — wide range is significant)
- After calibration: **60-99%**
- **Position bias**: When shown two outfits side-by-side, GPT-4V preferentially rates the outfit in a specific position (left/right). The range of 30-74% raw accuracy partly reflects this bias. Must randomize presentation order.
- Key weakness: struggles ranking outfits with similar colors or subtle styling differences
- Key strength: excellent at explaining WHY something works — "the navy blazer creates visual weight that grounds the lighter bottom" is genuinely useful reasoning
- Correlation with human taste: **0.36-0.52** (moderate at best — fashion is deeply subjective)
- Performs best at distinguishing obviously good vs obviously bad outfits (85-99% after calibration)
- Performs worst at ranking multiple "good enough" options against each other

**Source:** [GPT-4V Fashion Aesthetic Evaluation (SIGGRAPH Asia 2024)](https://arxiv.org/abs/2410.23730)

---

## Color Harmony: The Surprising Science

### Traditional Color Theory is Empirically Wrong

Itten's color wheel (complementary, analogous, triadic) is what every wardrobe app uses. Research shows it's flawed:
- Itten's "complementary" pairs don't match perceptual complements
- One classical model was "almost non-correlated" with modern aesthetic preferences
- Classical harmony rules were derived from art theory, not empirical human preference data

### What Actually Works

**"The Science of Style" (PLOS ONE, 2014):**
- 239 participants, 30 color combinations each
- Found a robust quadratic effect: **maximum fashionableness at MODERATE color coordination**
- Neither matchy-matchy nor clashing was preferred — the Goldilocks principle
- This effect accounted for 2x the variance of a simple linear model

**ML-Based Color Harmony Research (Fashion & Textiles, 2025):**
- SVM achieves **0.99+ accuracy** classifying color harmony vs disharmony in fashion
- CNNs achieve **0.95+ accuracy** on fashion color harmony evaluation
- GAN-based framework generates harmonious color palettes for specific garment types
- Key finding: ML models consistently outperform rule-based color theory approaches
- However, these models are overkill for our use case — the simple Delta E math from the PLOS ONE research gives us 90%+ of the quality at 0% of the training cost

**Practical implication:** Don't hardcode color wheel rules. Instead:
- Convert to LAB color space (perceptually uniform)
- Score for moderate color distance (not too similar, not too different)
- 2-3 colors per outfit is the sweet spot
- LLMs are surprisingly good at color reasoning because they've ingested millions of styling articles

**Sources:**
- [The Science of Style (PLOS ONE, 2014)](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0102772)
- [Color Harmony Evaluation Model (Fashion & Textiles, 2025)](https://link.springer.com/article/10.1186/s40691-025-00433-y)
- [Multi-color Harmony in Real-life Scenes (Frontiers in Psychology, 2022)](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.945951/full)

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

### Layer 5: Personalization / Learning (Two-Moment Feedback → Light ML)

**What:** Learn from the full feedback loop — not just morning accept/reject, but evening confirmation of what was actually worn.

**The Two-Moment System:**
Our key insight: "Wear This ✓" in the morning is an INTENT signal. Evening confirmation is the REALITY signal. The gap between them is our richest data source.

```
Morning "Wear This" = planned (weak signal, ~0.5x weight)
Evening "👍 Confirmed" = actually wore it (strong signal, ~2.0x weight)
Evening "🔥" = power outfit (very strong, ~2.5x weight)
Evening "Got compliments" = social proof (strongest, ~3.0x weight)
Evening "Changed outfit" = intent didn't match reality (investigate WHY)
```

**Phase 1 — Two-Moment Feedback Weights (no ML):**
```python
# Signal weight system — feeds into Layer 3 scoring
SIGNAL_WEIGHTS = {
    "accepted_and_confirmed": 2.0,           # Actually wore it, liked it
    "accepted_and_rated_high": 2.5,          # Enthusiastic confirmation
    "accepted_and_got_compliments": 3.0,     # Power outfit — social proof
    "accepted_but_changed": 0.3,             # Liked idea, not execution
    "accepted_changed_weather": 0.5,         # Weather model needs calibration
    "accepted_changed_comfort": -0.5,        # Item has comfort issue
    "accepted_changed_occasion": 0.2,        # Occasion mismatch
    "rejected_morning": -1.0,                # Don't suggest this pattern
    "rejected_too_formal": -0.8,             # Lower formality preference
    "rejected_too_casual": -0.8,             # Raise formality preference
    "ignored": 0.0,                          # No signal
}

# Aggregate preferences from feedback history:
preferences = {
    "color_combos": {
        ("navy", "white"): +6.0,   # confirmed 3x (2.0 each)
        ("red", "orange"): -2.0,   # rejected 2x (-1.0 each)
    },
    "formality_bias": +0.8,         # confirmed outfits skew 0.8 above neutral
    "weather_sensitivity": 1.3,     # changed due to weather 3x → increase weather weight
    "pattern_mixing": -1.5,         # rejects pattern-on-pattern consistently
    "power_outfits": [              # 🔥 rated combos — suggest for important days
        {"items": [...], "occasions": ["meeting", "date"]},
    ],
    "comfort_flags": {              # items with comfort issues
        "item_xyz": ["too_hot"],    # don't suggest this item above 30°C
    },
}

# Apply as bonus/penalty in Layer 3 scoring
# Also pass to Layer 4 Claude prompt as preference context
```

**What each feedback type adjusts:**
- 👍 confirmed → boost: same color combos, formality level, occasion mapping
- 👎 "too formal" → reduce formality preference weight for this user
- 👎 "too hot" → increase weather sensitivity multiplier
- "got compliments" → flag combo as power outfit, suggest for important days
- "changed + OOTD photo" → learn real preference when suggestion missed
- "uncomfortable fabric" → item-level flag, suppress in hot weather combos
- "changed" reason patterns → reveals meta-patterns (always changes on Mondays? different Monday needs?)

**Visible feedback loop (critical for incentivizing feedback):**
- Display "Suggestion accuracy: 78%" on Today screen
- Shows improvement over time: "Your feedback improved accuracy by 12% this month"
- Users see direct impact of their evening check-ins

**Phase 2 — Embedding version (light ML):**
- Use Marqo-FashionSigLIP (pre-trained, free, on HuggingFace) to embed each item
- Items the user CONFIRMS wearing together → pull embeddings closer (stronger signal than just "accepted")
- Items rejected together → push apart
- Power outfit items → cluster tighter (these combos WORK)
- Over time, the embedding space personalizes based on real wear data, not just intent

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

Every clothing photo needs background removal before analysis and display. Clean, isolated garment photos make the closet look premium AND improve AI tagging accuracy. The ai-closet repo (240 stars) uses fal.ai at $0.002/image — this is the proven approach.

### Options Compared

| Solution | Quality (IoU) | Speed | Cost | Best For |
|----------|--------------|-------|------|----------|
| rembg (U2-Net default) | 39% on diverse images | Fast | Free | DON'T USE — unreliable |
| rembg (BiRefNet model) | 87% | ~800ms | Free | Development / MVP |
| fal.ai RMBG-2.0 (Bria) | 90% | Fast | $0.002/image | Production |
| Photoroom API | ~90%+ | 300ms | $0.02-0.10/image | Premium quality (10-50x more expensive) |

**Recommendation:**
- MVP: rembg with BiRefNet model (free, good enough)
- Production: fal.ai RMBG-2.0 ($0.002/image, best price-to-quality ratio)
- Premium fallback: Photoroom API ($0.02-0.10/image) — 300ms response time, highest quality, but 10-50x more expensive than fal.ai. Only use if fal.ai quality proves insufficient.
- Critical: **never use rembg's default U2-Net** — drops to 39% IoU on diverse (non-portrait) images

**rembg Production Warning:**
- rembg has known **memory leak issues** in long-running processes. In production, either:
  - Run rembg as a separate process per image (subprocess approach)
  - Use a worker pool with periodic restart
  - Or just use fal.ai API ($0.002/image is negligible)
- For MVP/development, rembg with BiRefNet is fine — the memory leak only matters under sustained load

**Sources:**
- [rembg GitHub](https://github.com/danielgatis/rembg)
- [fal.ai RMBG-2.0](https://fal.ai/models/fal-ai/rmbg-v2)
- [Photoroom API](https://www.photoroom.com/api)
- [BiRefNet: Bilateral Reference Network](https://arxiv.org/abs/2401.03407)

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
