# ClosetAI - AI Pipeline

## Overview

ClosetAI uses AI across three core pipelines:
1. **Item Recognition** — Analyze clothing photos to extract metadata
2. **Outfit Generation** — Create context-aware outfit combinations
3. **Shopping Intelligence** — Identify gaps and recommend purchases

All AI is orchestrated through the FastAPI backend, with Claude as the primary model.

---

## Pipeline 1: Item Recognition (Claude Vision)

### When It Runs
- User uploads a clothing photo (camera or gallery)
- "Before You Buy" scanner in-store

### Input
- JPEG/PNG image (compressed to <2MB client-side)
- User context: gender, existing wardrobe categories

### Process

```
1. Image received at POST /api/wardrobe/upload
2. Image saved to Supabase Storage
3. Image converted to base64
4. Sent to Claude Vision API (claude-sonnet-4-5-20250929)

Prompt:
"""
Analyze this clothing item photo and return a JSON object with:
{
  "category": "top|bottom|dress|outerwear|footwear|accessory|bag|jewelry|ethnic",
  "subcategory": "specific type (e.g., t-shirt, blouse, jeans, sneakers, saree, kurta)",
  "dominant_colors": ["list of 1-3 main colors"],
  "pattern": "solid|striped|plaid|floral|printed|geometric|abstract|none",
  "material": "best guess (cotton, denim, silk, polyester, leather, etc.)",
  "formality_level": 1-5 (1=very casual, 5=very formal),
  "occasion_tags": ["office", "casual", "date-night", "party", "gym", "travel", "ethnic"],
  "season_tags": ["summer", "winter", "monsoon", "all-season"],
  "description": "brief natural description of the item"
}
Return ONLY the JSON object.
"""

5. Parse JSON response
6. Create wardrobe_item with AI-extracted fields
7. User reviews and confirms/adjusts
```

### Output
```json
{
  "category": "top",
  "subcategory": "blouse",
  "dominant_colors": ["navy", "white"],
  "pattern": "striped",
  "material": "cotton",
  "formality_level": 3,
  "occasion_tags": ["office", "casual"],
  "season_tags": ["all-season"],
  "description": "Navy and white striped cotton blouse with button-down collar"
}
```

### Accuracy Targets
| Field | Target Accuracy | Notes |
|-------|----------------|-------|
| Category | 95%+ | Major category (top/bottom/dress) is reliable |
| Subcategory | 85%+ | Specific type (blouse vs shirt) is harder |
| Dominant colors | 90%+ | Lighting affects this; 1-3 colors is usually right |
| Pattern | 90%+ | Solid vs printed is easy; specific patterns are harder |
| Material | 70%+ | Hard to detect from photos alone |
| Formality | 80%+ | Contextual; a blazer could be 3 or 4 |
| Occasions | 75%+ | Subjective; user should always confirm |

### Edge Cases & Handling
- **Multiple items in photo:** Prompt specifies "single item" — if Claude detects multiple, return the most prominent one with a note
- **Poor lighting/blur:** Return lower confidence scores, prompt user to retake
- **Ethnic wear (saree, lehenga, kurta):** Specific subcategory support in prompt
- **Accessories:** Lower detail extraction, focus on color and type
- **Already cropped/catalog images:** Work well — even better than real photos

### Cost Estimate
- Claude Sonnet Vision: ~$0.003 per image (768 input tokens for image + 200 output tokens)
- At 100 items/user: ~$0.30/user for initial closet setup
- At 1000 users: ~$300 for all closet setups

---

## Pipeline 2: Outfit Generation

### When It Runs
- Daily, early morning (pre-compute for active users)
- On-demand when user requests "Show Me Another"

### Inputs
```
1. Wardrobe items (all active, non-archived)
2. Style DNA profile
3. Weather data (current + forecast)
4. Calendar events (if connected)
5. Outfit history (last 14 days — avoid repeats)
6. Feedback history (accepted/rejected patterns)
```

### Two-Stage Process

#### Stage 1: Algorithmic Candidate Generation (Fast, No AI Cost)

```python
# outfit_engine.py

1. Filter items by weather/season
   - If temp > 30°C: exclude "winter" tagged items
   - If rain forecast: boost items with practical materials

2. Group items by category
   - tops[], bottoms[], dresses[], outerwear[], footwear[], accessories[]

3. Generate candidates
   Strategy A: top + bottom (+ optional outerwear, shoes, accessory)
   Strategy B: dress (+ optional outerwear, shoes, accessory)
   Strategy C: ethnic set (kurta + bottom / saree / lehenga)

4. Score each candidate (0-100):
   - Formality consistency: items within ±1 formality level (+20)
   - Color harmony: complementary/analogous colors (+25)
   - Occasion fit: all items match target occasion (+20)
   - Freshness: items not worn in last 7 days (+15)
   - Variety: mix of textures/patterns (+10)
   - User preference: similar to previously accepted outfits (+10)

5. Sort by score, return top 10 candidates
```

#### Stage 2: Claude Ranking & Reasoning (Optional, Higher Quality)

```
Send top 10 candidates to Claude for final ranking:

Prompt:
"""
You are a personal stylist for {user_name}. Their style archetype is {archetype}.

Here are 10 outfit candidates for today:
{candidates with item descriptions, colors, formality}

Context:
- Weather: {temp}°C, {condition}
- Occasion: {primary_occasion for today}
- Recently worn: {last 5 outfits}
- Style preferences: {from style DNA}

Rank the top 5 outfits and provide:
1. Ranking (best to good)
2. One sentence explaining why each works
3. Any styling tip (e.g., "roll the sleeves for a casual touch")

Return as JSON array.
"""
```

### Output (per outfit recommendation)
```json
{
  "item_ids": ["uuid-1", "uuid-2", "uuid-3"],
  "style_score": 87,
  "color_harmony_score": 92,
  "occasion": "office",
  "reasoning": "Navy + cream is a timeless office combo. The cotton fabric is perfect for 28°C. You haven't worn this shirt since last Tuesday.",
  "styling_tip": "Add a gold watch or bracelet to elevate the look"
}
```

### Cost Estimate
- Stage 1 (algorithmic): $0 — runs locally in Python
- Stage 2 (Claude ranking): ~$0.005 per generation (500 input + 300 output tokens)
- Daily for 1000 users: ~$5/day = $150/month
- Optimization: only run Stage 2 for Pro/Premium users

---

## Pipeline 3: Shopping Intelligence

### When It Runs
- Weekly background job for all users
- On-demand when user views Discover tab
- "Before You Buy" scanner (on-demand)

### Gap Analysis

```python
# shopping.py

1. Analyze wardrobe composition:
   - Category counts (tops: 18, bottoms: 4, shoes: 2)
   - Color distribution (40% blue, 25% black, ...)
   - Occasion coverage (office: 80%, party: 20%, ethnic: 10%)
   - Formality spread (avg 2.8 = leaning casual)

2. Identify gaps:
   - Category imbalance: "18 tops but only 4 bottoms"
   - Missing essentials: "no outerwear", "only 1 pair of shoes"
   - Occasion gaps: "no party-appropriate items"
   - Color gaps: "no warm tones in wardrobe"

3. Score each gap by "outfit unlock potential":
   - A new bottom would combine with 18 tops = high potential
   - A new accessory would enhance existing outfits = medium potential

4. Generate shopping suggestions with reasoning:
   - Category, subcategory, color suggestion
   - Why it's needed
   - How many new outfits it unlocks
   - Budget range based on user's profile
```

### "Before You Buy" Scanner

```
User photographs item in store
    → Same Claude Vision pipeline as item recognition
    → Extract: category, subcategory, colors, pattern
    → Compare with existing wardrobe:
        SELECT * FROM wardrobe_items
        WHERE user_id = ?
        AND category = ?
    → For each existing item, compute similarity:
        - Same category + same colors + same pattern = HIGH similarity
        - Same category + similar colors = MEDIUM similarity
        - Same category only = LOW similarity
    → Return verdict:
        - "You already own 2 similar items" (with photos)
        - "This is unique — it unlocks X new outfits"
        - "Similar to [item], but different enough to add variety"
```

---

## Style DNA Computation

### When It Runs
- After onboarding (initial profile)
- Weekly refresh (as wardrobe and history grow)
- After significant wardrobe changes (10+ items added)

### Process

```python
# style_dna.py

Inputs:
- All wardrobe items
- All outfit history (what was actually worn)
- Style profile (self-reported preferences)
- Recommendation feedback (accepted/rejected)

Compute:
1. Color Palette Analysis
   - Count color frequency across all items
   - Weight by times_worn (worn items matter more)
   - Top 8 colors = user's actual palette

2. Category Balance
   - Count per category
   - Compare to "ideal" ratios
   - Flag imbalances

3. Formality Distribution
   - Average formality of all items
   - Weighted by wear frequency
   - Label: casual / balanced / formal

4. Wardrobe Utilization
   - % of items worn at least once
   - "Never worn" pile identification

5. Style Archetype (future: Claude-computed)
   - Based on colors, formality, occasion patterns
   - "Modern Classic" / "Bold Experimenter" / "Casual Minimalist" etc.

6. Gap Analysis
   - Missing categories vs. essentials
   - Missing occasion coverage
   - Color variety score

Output: style_dna JSONB field on style_profiles table
```

---

## Future AI Features (Post-MVP)

### 1. Style Embedding & Similarity (OpenAI Embeddings)
- Embed each wardrobe item's description as a vector
- Enable: "find items similar to this" search
- Enable: "people with similar style also wear..." recommendations
- Store in Supabase with pgvector extension

### 2. Outfit Explanation (Claude Chat)
- "Why do these items work together?"
- "How can I dress this outfit up/down?"
- Interactive styling Q&A

### 3. Trend Awareness
- Periodic prompts to Claude about current fashion trends
- Match trends to user's existing wardrobe
- "This trend works with items you already own"

### 4. Selfie-Based Color Analysis
- Upload selfie → Claude Vision analyzes:
  - Skin tone (fair/medium/olive/brown/deep)
  - Undertone (warm/cool/neutral)
  - Best colors (based on color theory)
- Result: personalized power color palette

### 5. AR Virtual Try-On (Phase 3+)
- Flutter mobile app with camera overlay
- Hold up item → see it on your body
- Requires: Flutter + ARCore/ARKit + custom ML model
- Timeline: 6+ months out

---

## AI Cost Management

### Cost Per User Per Month (Estimated)

| Feature | Cost | Frequency | Monthly Total |
|---------|------|-----------|---------------|
| Item recognition | $0.003/item | 5 items/month avg | $0.015 |
| Daily outfit (Stage 2) | $0.005/day | 20 days/month | $0.10 |
| Shopping analysis | $0.01 | 2x/month | $0.02 |
| Style tips | $0.002 | 4x/month | $0.008 |
| **Total per user** | | | **~$0.14/month** |

### At Scale
| Users | Monthly AI Cost | Revenue (5% Pro @ $5) | Margin |
|-------|----------------|----------------------|--------|
| 1,000 | $140 | $250 | Positive |
| 10,000 | $1,400 | $2,500 | Positive |
| 100,000 | $14,000 | $25,000 | Positive |

### Cost Optimization Strategies
1. **Cache daily outfits** — generate once per day, not per request
2. **Skip Stage 2 for free users** — algorithmic-only outfits
3. **Batch processing** — generate recommendations during off-peak
4. **Model selection** — use Haiku for simple tasks, Sonnet for complex
5. **Prompt optimization** — shorter prompts, structured outputs, fewer tokens
