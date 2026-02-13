# ClosetAI - Creative AI Quality & Trend Intelligence

## TL;DR

The creative/taste side of AI styling is good enough for launch with the right architecture. LLMs default to "safe" recommendations but we solve this with a creativity dial, prompt engineering, and a 60/25/15 allocation strategy (safe/stretch/surprise). For trend tracking, a weekly batch pipeline using scrapers + Pinterest API + LLM summarization costs $0-150/month with no ML needed. Our Indian fashion cultural context — injected via prompts, not trained models — is a moat no Western competitor has.

---

## Part 1: Is the Creative Part Good Enough?

### What the Research Says

**The good news:**
- Claude/GPT-4o have genuine fashion knowledge from training on millions of Vogue articles, styling guides, fashion blogs
- GPT-4V scored **85-99% accuracy** distinguishing great outfits from bad ones when differences were obvious (SIGGRAPH Asia 2024)
- For everyday "should I wear this blazer with these chinos?" questions, LLMs are genuinely competent
- Humans only agree **71-82%** of the time on outfit quality — fashion is inherently subjective

**The honest gaps:**
- A plain LLM is **near-random (29%)** at raw outfit compatibility on benchmarks
- LLM correlation with human taste is **0.36-0.52** (moderate at best)
- Models struggle ranking outfits with similar colors or subtle styling differences
- Default bias toward "safe" conventional recommendations — won't suggest bold/creative combinations without prompting

**The key insight:** We don't use the LLM raw. Our 7-layer pipeline (from AI_DEEP_DIVE.md) pre-filters candidates through rules + color math before Claude sees them. Claude ranks 10 good options, not 500 random ones. That's a dramatically easier task.

### Sources

- [GPT-4V Fashion Aesthetic Evaluation](https://arxiv.org/abs/2410.23730) — SIGGRAPH Asia 2024
- [Decoding Style: LLM Fine-Tuning for Outfit Recommendation](https://arxiv.org/abs/2409.12150) — September 2024
- [Toward Computational Taste: LLMs, Aesthetics & Judgment](https://patron.fund/blog/toward-computational-taste-llms-aesthetics-judgment) — January 2025
- [Deconstructing Taste: Human-Centered AI Framework](https://arxiv.org/abs/2601.17134) — January 2026

---

## Color Matching: The Science

### Traditional Color Theory is Wrong

Itten's color wheel (complementary, analogous, triadic) — what every wardrobe app uses — is empirically flawed:
- Itten's "complementary" pairs don't match perceptual complements
- One classical model was "almost non-correlated" with modern aesthetic preferences
- Research shows these rules diverged from how people actually perceive color harmony

### What Actually Works

**"The Science of Style" (PLOS ONE, 2014):**
- 239 participants, 30 color combinations each
- Maximum fashionableness at **MODERATE color coordination** — the Goldilocks principle
- Neither matchy-matchy nor clashing was preferred
- This quadratic effect accounted for **2x the variance** of a linear model

### Our Approach

```python
# color_harmony.py

def score_color_harmony(colors: list[str]) -> float:
    """
    Score based on research-backed moderate matching heuristic.
    NOT traditional Itten's rules.
    """
    # Convert to LAB color space (perceptually uniform)
    lab_colors = [rgb_to_lab(hex_to_rgb(c)) for c in colors]

    # Calculate pairwise color distance (Delta E)
    distances = pairwise_delta_e(lab_colors)

    # Score using moderate matching heuristic:
    #   Delta E 20-60: high harmony (moderate contrast) → score 80-100
    #   Delta E 0-20:  too matchy (boring) → score 50-70
    #   Delta E 60+:   clashing (risky) → score 30-50

    # Neutral colors (black, white, grey, navy, beige) are wildcards
    # They don't count toward clash scoring

    # Bonus for 2-3 non-neutral colors, penalty for 4+

    # Allow Claude to override for trend-aware combinations
    # ("color-blocking is in right now, so orange + pink is intentionally bold")

    return harmony_score
```

**Why not ML for color matching:** The PLOS ONE research gives us a clear, empirically-validated scoring function. No model training needed — it's math that outperforms the rule-based approaches every other app uses.

### Sources

- [Color Harmony Evaluation Model](https://link.springer.com/article/10.1186/s40691-025-00433-y) — Fashion & Textiles, 2025
- [The Science of Style: Colors Should Match Only Moderately](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0102772) — PLOS ONE
- [Multi-color Harmony in Real-life Scenes](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.945951/full) — Frontiers in Psychology

---

## The Creativity Problem (And How We Solve It)

### Why AI Defaults to "Safe"

LLMs suggest navy + cream every time. They won't tell you that an oversized blazer with bike shorts is a legitimate fashion-forward look, or that orange + pink is intentionally bold right now.

Reasons:
1. Training data skews toward "conventional wisdom" fashion advice
2. Safety alignment discourages bold/controversial outputs
3. Color theory rules are well-represented; intentional rule-breaking is contextual
4. Temperature is NOT the answer — research shows it correlates weakly with novelty and moderately with incoherence (ICCC 2024)

### The Creativity Dial

Map to the existing `comfort_level` field in StyleProfile:

```python
CREATIVITY_PROMPTS = {
    "conservative": """
        Suggest outfits prioritizing classic coordination and
        polished execution. Stick to proven combinations.
        Emphasize appropriateness and subtlety.
    """,

    "moderate": """
        Suggest outfits with one unexpected element — an
        interesting texture mix, a statement accessory, or
        an item used in a non-obvious way. Balance reliability
        with personality.
    """,

    "adventurous": """
        Push boundaries. Reference dopamine dressing, high-low
        mixing, intentional contrast. Think editorial, not
        boardroom. Pair items from different style registers
        (formal + casual, vintage + modern, streetwear + tailored).
        The goal is self-expression, not safety.
    """
}
```

### The 60/25/15 Allocation Strategy

For each batch of daily recommendations:

| Category | % | Description | Example |
|----------|---|-------------|---------|
| **Safe** | 60% | High-confidence matches based on user history | Navy blazer + beige chinos + white sneakers |
| **Stretch** | 25% | Slightly outside comfort zone, grounded in preferences | That blazer but with olive cargo pants they never paired it with |
| **Surprise** | 15% | Deliberately unexpected, validated before presenting | The kurta they tagged "office" styled casually with jeans + statement earrings |

Track which category gets the best `OutfitHistory.rating` scores. Over time, the ratio personalizes per user:
- User who consistently rates "surprise" picks highest → shift to 40/30/30
- User who always rejects "surprise" picks → shift to 80/15/5

### Better Approaches for Creative Surprise Than Random Temperature

**1. Constraint-based creativity:**
```
"Create an outfit pairing an item from the user's least-worn
category with their most-worn favorite. The combination should
be unexpected but coherent."
```

**2. Style cross-pollination:**
```
"Style this outfit inspired by Japanese minimalism meets Indian
textile richness" or "90s grunge meets contemporary tailoring"
```

**3. Occasion subversion:**
```
"Take this user's workwear blazer and style it for a weekend
brunch — pair it with the most unexpected bottom from their
wardrobe that still creates a coherent look."
```

**4. The "underused item" prompt:**
```
"This user hasn't worn [item] in 45 days. Build an outfit
around it that gives them a reason to pull it out again."
```

### Source

- [Is Temperature the Creativity Parameter of Large Language Models?](https://arxiv.org/abs/2405.00492) — ICCC 2024

---

## Occasion-Aware Creativity Scaling

Different occasions call for different levels of creative risk:

| Occasion | Creativity Level | Prompt Strategy |
|----------|-----------------|-----------------|
| Office/Work | Conservative | Appropriateness, subtlety, polished execution |
| Casual/Weekend | Moderate | Allow personality, suggest one unexpected element |
| Date Night | Moderate-High | Encourage statement pieces, interesting combinations |
| Party/Night Out | High | Push boundaries, bold combinations welcome |
| Festival/Celebration | Context-Dependent | Match cultural expectations, allow personal flair |
| Fashion Event | Maximum | Editorial styling, risk-taking encouraged |
| WFH/Errands | Low | Comfort-first, still put-together |

This maps to the existing `Outfit.occasion` and `WardrobeItem.occasion_tags` fields. Combined with `WardrobeItem.formality_level`, we get a two-dimensional space: **formality x creativity**. Each recommendation is placed intentionally within this space.

---

## The Personality Score (Two-Axis Evaluation)

Current schema has `style_score` and `color_harmony_score`. Research suggests we should evaluate on two separate dimensions:

### Correctness (Does it follow the rules?)
- Color coordination within moderate harmony range
- Formality consistency across items
- Proportion balance (not all oversized or all tight)
- Season/weather appropriateness

### Personality (Does it show creative intention?)
- Unexpected combinations that still work
- Distinctive accessories or statement pieces
- Intentional contrast (high-low, formal-casual mixing)
- Items that tell a story or create a mood
- Mixing of style registers (vintage + modern, streetwear + tailored)

```python
OUTFIT_EVALUATION_PROMPT = """
Rate this outfit on two dimensions:

CORRECTNESS (0-10): Basic style rule adherence. Color coordination,
formality consistency, proportion balance.

PERSONALITY (0-10): Creative intention. Unexpected combinations that
work, distinctive accessories, intentional contrast, style register
mixing, overall "this person has taste" factor.

An outfit can score:
- High correctness, low personality = safe/boring (fine for conservative users)
- High correctness, high personality = fashion-forward (the goal for adventurous users)
- Low correctness, high personality = experimental (risky, only for very adventurous)
- Low correctness, low personality = bad (never suggest this)
"""
```

---

## Progressive Trust Building

Don't ask users where they want to be on the creativity spectrum — observe and adapt:

### Week 1-2: Conservative Start
- 80% safe, 20% moderate stretch
- Learn baseline preferences from accept/reject patterns

### Week 3-4: Test the Waters
- If stretch picks accepted at >50% rate → shift to 60/30/10
- If rejected consistently → stay at 80/20/0

### Month 2+: Fully Personalized
- Ratio computed from tracked preferences per user
- Ratio adapts per occasion (user may be conservative at work, adventurous on weekends)

### "Mood" Override
Allow users to override defaults on any given day:
```
"Today I'm feeling..."
  → Minimal & Safe
  → My Usual
  → A Little Bold
  → Fashion Risk Day
```

---

## Part 2: Keeping Up With Fashion Trends

### The Problem

Fashion changes weekly. Claude's training data has a cutoff. If "butter yellow + lavender" becomes the color combo of Spring 2026, our system won't know unless we tell it.

### How the Big Companies Do It

| Company | Approach | Cost | Accuracy |
|---------|----------|------|----------|
| **Heuritech** | CV analysis of 3M+ social media images/day, 2,000+ fashion attributes detected | Thousands of €/month | 91%+ on trend direction |
| **WGSN** | Human experts + TrendCurve AI | $25K/year full, $59/month starter | 90% claimed |
| **Stitch Fix** | 80+ data scientists, proprietary models | $10M+/year team cost | 85% claimed |
| **Trendalytics** | Search + social signal aggregation | $12K+/year | Not disclosed |

### How Heuritech Actually Works (Technically)

The most sophisticated approach in the industry:

1. **Curated panels** of Instagram/Weibo/WeChat accounts, segmented by influence tier:
   - "Edgy" — fashion professionals, stylists, runway influencers
   - "Trendy" — fashion-forward early adopters
   - "Mainstream" — conservative followers

2. **Computer vision pipeline** (CNNs trained on weakly-annotated e-commerce images):
   - Detects 2,000+ attributes: colors, prints, fabrics, silhouettes, shapes
   - Combines attributes into compound micro-trends (e.g., "oversized beige linen blazer")

3. **Forecasting models**:
   - Classical statistical methods (exponential smoothing) for stable baselines
   - Deep learning / RNNs for detecting early signals from edgy/trendy segments
   - Meta-algorithm selects optimal method combination per trend

4. **Key insight:** Fashion diffuses from edgy → trendy → mainstream in a predictable cascade. Measuring what the "edgy" segment wears today predicts what mainstream wears in 6-12 months.

We cannot build this. But we don't need to.

### What We Can Actually Build ($0-150/month)

#### Tier 0: Free — LLM With Web Search

```python
# Weekly batch job (runs every Monday at 6 AM)

def generate_trend_snapshot():
    """Ask Claude with web search for current fashion trends."""

    response = claude.messages.create(
        model="claude-sonnet-4-5-20250929",
        messages=[{
            "role": "user",
            "content": """
            Research and return the current top fashion trends
            in India for women 22-40. Include:

            1. Macro trends (broad movements)
            2. Micro trends (specific items/styles going viral)
            3. Color trends (what's in, what's fading)
            4. India-specific trends (Bollywood, festival, regional)
            5. Trends that are declining

            Return as structured JSON.
            Search current sources: Vogue India, Elle India,
            Who What Wear, TikTok fashion, Instagram fashion.
            """
        }]
    )

    # Parse and store in trend_snapshots table
    store_trend_snapshot(response)
```

This alone keeps us 80% current. Zero additional cost beyond the API call.

#### Tier 1: Low-Cost Automation ($100-150/month)

Add automated data signals:

| Source | Tool | Cost | What It Gives Us |
|--------|------|------|-----------------|
| Google Trends | pytrends (Python library) | $0 | Search volume momentum for fashion terms |
| Pinterest Trends API | Official API | $0 | What people are pinning — strongest shopping intent signal |
| TikTok trends | Apify scraper | $49/month | Viral fashion hashtags, what's blowing up this week |
| Fashion RSS feeds | Custom scraper | ~$10/month | Vogue, Elle, Who What Wear article content |
| Social listening | Brand24 | ~$99/month | Fashion keyword velocity across all platforms |

#### The Architecture

```
                    Weekly Batch Job (Monday 6 AM)
                    ┌──────────────────────────────────┐
                    │                                  │
   Google Trends ──→│  1. Collect signals from all      │
   (pytrends)       │     sources                       │
                    │                                  │
   Pinterest API ──→│  2. Score each signal:            │
                    │     - Search momentum (0-1)       │
   TikTok Apify  ──→│     - Social velocity (0-1)       │──→ trend_snapshots
   scraper          │     - Pinterest trending (0-1)    │    table in Supabase
                    │     - Editorial coverage (0-1)    │
   Fashion RSS   ──→│                                  │
   feeds            │  3. Composite score = weighted avg│
                    │     Flag anything > 0.7 as        │
                    │     "trending now"                │
                    │                                  │
                    │  4. LLM summarizes into           │
                    │     structured JSON snapshot      │
                    └──────────────────────────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────────────┐
                    │  Recommendation Engine            │
                    │                                  │
   User wardrobe ──→│  Claude prompt includes:          │
                    │  - User's wardrobe items          │──→ Outfit
   User style    ──→│  - User's style DNA              │    suggestions
   preferences      │  - Latest trend snapshot ← NEW   │
                    │  - Weather/occasion context       │
   Weather data  ──→│                                  │
                    └──────────────────────────────────┘
```

#### The Trend Snapshot Format

```json
{
  "snapshot_date": "2026-02-14",
  "season": "Spring 2026",
  "macro_trends": [
    {
      "name": "Color Blocking Revival",
      "confidence": 0.85,
      "keywords": ["color-blocking", "bold", "contrast"],
      "colors": ["orange", "pink", "electric blue"],
      "description": "Bold, intentional color pairings replacing quiet luxury",
      "lifecycle": "growing",
      "source_signals": ["tiktok_hashtag_velocity", "pinterest_trending", "vogue_editorial"]
    },
    {
      "name": "Modern Chanderi",
      "confidence": 0.72,
      "keywords": ["chanderi", "handloom", "contemporary"],
      "colors": ["ivory", "sage", "dusty rose"],
      "description": "Traditional Chanderi fabric in contemporary western-inspired cuts",
      "lifecycle": "emerging",
      "source_signals": ["instagram_mumbai", "designer_collections"]
    }
  ],
  "micro_trends": [
    {
      "name": "Butter Yellow Accessories",
      "confidence": 0.70,
      "platform_origin": "tiktok",
      "lifecycle": "emerging",
      "relevance_to_existing_wardrobes": "Pairs well with navy, white, denim, cream"
    }
  ],
  "color_trends": {
    "rising": ["butter yellow", "lavender", "cherry red", "sage green"],
    "stable": ["navy", "cream", "black", "white"],
    "declining": ["neon green", "hot pink (Barbiecore fading)"]
  },
  "india_specific": [
    {
      "name": "Indo-Western Office Fusion",
      "description": "Kurta tops with tailored trousers replacing traditional western office wear",
      "cities": ["Mumbai", "Bangalore", "Delhi"],
      "lifecycle": "mainstream"
    },
    {
      "name": "Diwali 2026 Preview",
      "description": "Deep emerald and gold replacing traditional red and maroon",
      "lifecycle": "emerging"
    }
  ],
  "declining_trends": [
    {
      "name": "Quiet Luxury",
      "note": "Peaked mid-2025, now being replaced by more expressive styling"
    },
    {
      "name": "Logomania",
      "note": "Oversized logos declining across all demographics"
    }
  ]
}
```

#### How Trends Flow Into Recommendations

```python
# In outfit_engine.py, when generating Claude ranking prompt:

def build_ranking_prompt(candidates, user, weather, occasion):
    trend_snapshot = get_latest_trend_snapshot()

    prompt = f"""
    You are a personal stylist for {user.name}.
    Style archetype: {user.style_archetypes}.

    CURRENT TREND CONTEXT (as of {trend_snapshot.date}):
    Rising trends: {trend_snapshot.macro_trends}
    Trending colors: {trend_snapshot.color_trends.rising}
    Declining: {trend_snapshot.declining_trends}
    India-specific: {trend_snapshot.india_specific}

    When ranking outfits, give a small bonus to combinations
    that align with current trends — but only if they genuinely
    work for this user's style and occasion. Never force a trend
    that doesn't fit.

    Here are 10 outfit candidates for today:
    {format_candidates(candidates)}

    Context:
    - Weather: {weather.temp}°C, {weather.condition}
    - Occasion: {occasion}
    - Recently worn: {user.recent_outfits}

    Rank the top 5 with reasoning.
    """

    return prompt
```

### Why Pinterest Is Our Best Free Data Source

Pinterest is arguably the most valuable trend signal for fashion because:
- **570M+ monthly active users**, heavily skewed toward shopping intent
- **1.5 billion pins saved per week**
- Users explicitly pin aspirational fashion — this is INTENT data, not passive scrolling
- Fashion/style is one of Pinterest's top categories
- **Free API** with trend endpoints:
  - `GET /trends/keywords/{region}/top/{trend_type}` — trending keywords by region
  - `GET /trends/product_categories/trending` — trending product categories

Google Trends is useful for validation (confirming trends exist) but **lags social media by 4-8 weeks**. By the time something trends on Google Search, it's been trending on TikTok/Instagram for a month.

### The Hidden Trend Source: Our Own Users (Free, Real-Time)

After 1,000+ users, our wardrobe upload data becomes a trend signal:

```python
# trend_detection_internal.py

def detect_internal_trends():
    """Analyze our own user uploads for emerging trends."""

    # What colors are users uploading this month vs last month?
    color_shift = compare_upload_colors(this_month, last_month)
    # → "Earth tones up 30%, neon down 15%"

    # What categories are growing?
    category_shift = compare_upload_categories(this_month, last_month)
    # → "Wide-leg pants up 40%, skinny jeans down 20%"

    # What are users in specific cities uploading?
    regional_trends = compare_by_city(this_month)
    # → "Mumbai: more indo-western fusion pieces"

    # What items are being added to favorites?
    favorite_trends = trending_favorites(this_week)

    return InternalTrendReport(
        color_shift=color_shift,
        category_shift=category_shift,
        regional_trends=regional_trends,
        favorite_trends=favorite_trends
    )
```

This is free, real-time, and specific to our exact target demographic. No scraping, no API costs.

---

## Indian Fashion: The Cultural Moat

### The Gap No One Has Filled

**No major fashion AI benchmark dataset exists for Indian fashion.** This is a massive finding:
- Polyvore is Western-centric
- IQON is Japanese
- iFashion is Chinese
- DeepFashion is Western catalog images

This means every competitor's AI is trained on Western fashion data. None understand:
- How a saree drapes differently from a maxi dress
- That Diwali calls for jewel tones and gold accents, not pastels
- That a kurta pairs with churidar differently than with palazzo pants
- That Chanderi is for summer elegance while Banarasi is for celebrations
- That Mumbai humidity requires different fabric choices than Delhi winter

### How We Build This Advantage (Zero ML Cost)

We inject cultural intelligence directly into prompts:

```python
INDIAN_FASHION_CONTEXT = """
INDIAN FASHION INTELLIGENCE:

Fabric Hierarchy:
- Chanderi: Summer elegance, office-appropriate, light and breathable
- Banarasi: Celebrations, weddings, festivals — heavy, ornate
- Khadi: Casual sophistication, sustainability signal, all-season
- Silk: Formal occasions, evening events, festivals
- Cotton: Everyday, office, casual — Mumbai/Chennai essential
- Chiffon: Party wear, layering, monsoon-avoid

Indo-Western Fusion Rules:
- Kurta + jeans + statement earrings = smart casual
- Dupatta as scarf over western outfit = instant fusion
- Kolhapuri chappals with western sundress = weekend fusion
- Blazer over kurta = power dressing fusion
- Crop top + lehenga skirt = contemporary celebration

Festival Dressing:
- Diwali: Jewel tones (emerald, ruby, sapphire), gold accents,
  silk/brocade fabrics
- Holi: Playful colors, washable fabrics, white base
- Eid: Elegant pastels, whites, subtle embroidery
- Navratri: Bright colors, chaniya choli, dandiya-ready
- Pongal/Onam: Traditional whites and golds, regional specific

Regional Climate Adaptation:
- Mumbai: Humidity-resistant, breathable, monsoon-proof shoes
- Delhi: Layer-ready (extreme seasons), winter shawl integration
- Bangalore: Moderate, versatile pieces, light layers
- Chennai: Maximum breathability, cotton-forward

Occasion Spectrum (Indian-specific):
- Pooja/temple visit: Modest, ethnic-leaning
- Sangeet/mehendi: Colorful, celebratory, can be playful
- Wedding guest: Rich fabrics, statement jewelry, occasion-specific
- Office in India: Smart ethnic accepted (kurta + trousers is formal)
"""
```

### Why This Is a Moat

A competitor would need to:
1. Understand Indian fashion deeply enough to write these rules
2. Validate them with real Indian users
3. Keep them current with Indian fashion trends
4. Handle regional variations (what works in Mumbai ≠ Delhi ≠ Bangalore)

This is domain expertise, not technology. Our founding team is Indian, understands the context, lives the problem. No amount of ML training on Western data can replicate this.

### Bollywood as Trend Signal

Bollywood is the single largest fashion influence for Indian women 22-40. When a film releases:
- The lead actress's outfits become instant trends
- Designers see 3-5x demand for similar styles
- Regional adaptations of Bollywood looks drive local fashion

We can track this by adding Bollywood fashion coverage to our RSS feed pipeline. After major film releases, update the trend snapshot with Bollywood-inspired styling notes.

---

## Data Model Extensions for Trend + Creativity Features

### New Table: trend_snapshots

```sql
CREATE TABLE trend_snapshots (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    snapshot_date DATE NOT NULL,
    season TEXT,
    data JSONB NOT NULL,          -- full snapshot JSON
    source_signals JSONB,         -- which sources contributed
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_trend_date ON trend_snapshots(snapshot_date DESC);
```

### Extensions to Existing Tables

```sql
-- style_profiles: add creativity/cultural fields
ALTER TABLE style_profiles ADD COLUMN creativity_preference INTEGER DEFAULT 50;
  -- 0-100 scale, updated from behavior
ALTER TABLE style_profiles ADD COLUMN cultural_context TEXT DEFAULT 'mixed';
  -- western, indian_traditional, indo_western_fusion, mixed
ALTER TABLE style_profiles ADD COLUMN regional_preference TEXT;
  -- mumbai, delhi, bangalore, etc.

-- outfits: add creativity metadata
ALTER TABLE outfits ADD COLUMN personality_score NUMERIC;
  -- 0-10, separate from style_score (correctness)
ALTER TABLE outfits ADD COLUMN creativity_tier TEXT DEFAULT 'safe';
  -- safe, stretch, surprise

-- recommendations: add trend/creativity context
ALTER TABLE recommendations ADD COLUMN creativity_level INTEGER;
  -- what creativity level was used to generate this
ALTER TABLE recommendations ADD COLUMN trend_references JSONB;
  -- which trends informed this suggestion
```

---

## Cost Summary

| Component | Phase 1 (Months 1-3) | Phase 2 (Months 4-6) |
|-----------|---------------------|---------------------|
| Color harmony scoring | $0 (math) | $0 (math) |
| Creativity dial / prompt engineering | $0 (prompts) | $0 (prompts) |
| Indian fashion context | $0 (domain knowledge) | $0 (domain knowledge) |
| Trend snapshot via Claude web search | ~$1/week ($4/month) | ~$1/week ($4/month) |
| Google Trends (pytrends) | $0 | $0 |
| Pinterest Trends API | $0 | $0 |
| TikTok Apify scraper | — | $49/month |
| Fashion RSS scraper | — | ~$10/month |
| Social listening (Brand24) | — | ~$99/month |
| Internal user trend detection | — | $0 (our own data) |
| **Total** | **~$4/month** | **~$162/month** |

---

## The Quality Flywheel

The creative quality of recommendations isn't static — it improves through a flywheel:

```
1. CAPTURE
   Onboarding captures style preferences, comfort level,
   cultural context, occasions

2. GENERATE
   Claude generates outfits across creativity spectrum
   (60% safe / 25% stretch / 15% surprise)

3. PRESENT
   Show recommendations with clear creative intent
   ("Classic pick" vs "Something different" vs "Style experiment")

4. SIGNAL
   User accepts, rejects, saves, wears, rates
   Track which creativity tier gets best ratings

5. LEARN
   Update creativity_preference based on signals
   Update style_dna with evolving taste data
   Adjust safe/stretch/surprise ratio per user

6. TREND
   Weekly trend snapshot refreshes what "current" means
   Internal user data reveals our demographic's real preferences

7. EVOLVE
   Next generation uses updated profile + fresh trends
   Periodically introduce aspirational suggestions slightly
   ahead of where the user currently is
   (Don't freeze taste — help it grow)
```

### The Patron Warning: Don't Freeze Taste

Research on computational taste warns against "locking users into past preferences." Recommendation systems that only show what users liked before create filter bubbles. The system should periodically test whether taste is evolving:

- If a user who rated "safe" picks highest for 3 months suddenly rates a "stretch" pick 5/5, their taste may be evolving
- Gradually increase the stretch/surprise ratio
- Frame it positively: "Your style is evolving — we're noticing you're drawn to bolder combinations lately"

---

## Bottom Line

| Question | Answer |
|----------|--------|
| Is color matching good enough? | Yes. LAB math + moderate matching heuristic is research-backed and better than what any competitor uses. |
| Can AI have "taste"? | Partially. 85-99% on obvious differences, 36-52% correlation on subtle taste. Good enough for launch, improves with user feedback. |
| Will recommendations be "safe" and boring? | Not with the creativity dial. 60/25/15 allocation + prompt engineering + occasion-aware scaling ensures variety. |
| How do we keep up with trends? | Weekly trend snapshot pipeline. $0-162/month depending on phase. LLM with web search is the backbone. |
| What about Indian fashion trends? | Cultural context injection via prompts. Bollywood tracking. No competitor has this. Zero ML cost. |
| Do we need ML engineers for any of this? | No. Prompts, math, APIs, and domain knowledge. |
| What's the unfair advantage? | Indian cultural depth + compounding user preference data + trend-aware prompts. No Western-trained model can replicate this. |
