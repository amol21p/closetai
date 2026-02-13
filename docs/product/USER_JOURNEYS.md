# ClosetAI - User Journeys

## Journey 1: First-Time Onboarding (3 minutes)

### Goal
Get user from download → closet with 3-4 items → first outfit suggestion in under 3 minutes. The Spotify test: first value faster than you can make a cup of tea.

### Key Design Decisions (From Research)
- **OOTD-first, not closet-scan-first:** Photographing your closet takes 3-4 hours and kills 70%+ of users. A single mirror selfie takes 30 seconds and extracts 3-4 items. See ONBOARDING_STRATEGY.md for full research.
- **DROP body measurements from onboarding:** Let AI learn from photos over time. Move to Profile settings.
- **DROP skin tone picker from onboarding:** Move to Profile settings. Reduces friction.
- **5 steps max:** Every added step loses ~10% of users.

### Flow

```
Step 1: Welcome + Auth (15 seconds)
├── "Your closet, but smarter."
├── [Continue with Google] ← primary (one-tap OAuth)
├── [Continue with Apple]
└── [Continue with Email]

Step 2: About You (15 seconds)
├── Name (pre-filled from OAuth if available)
├── Gender: [Female] [Male] [Non-binary] [Prefer not to say]
│   └── Affects: category labels, style archetypes, outfit photos shown
└── Age group: [18-24] [25-34] [35-44] [45+]

Step 3: Your Style Vibe (30 seconds)
├── 3×3 grid of outfit photos (MIX of Indian + Western fashion)
│   ├── Casual Chic, Classic Elegant, Street Style
│   ├── Bohemian, Minimalist, Ethnic Fusion
│   └── Sporty Luxe, Romantic, Edgy Modern
├── User taps 2-3 that resonate
├── AI computes initial style archetype
└── "You're a Modern Classic ✨" ← FIRST WOW MOMENT

Step 4: OOTD Selfie — THE HOOK (60 seconds)
├── "Let's see today's outfit! 📸"
├── Camera opens with framing guide (dotted body outline)
├── User takes mirror selfie
├── MAGIC: AI extracts individual items with shimmer animation
│   ├── Items cascade in one by one (staggered 100ms)
│   ├── Each item: clean extracted photo + auto-detected category
│   ├── "Found 4 items!" with sparkle animation
│   └── Pre-checked ✓ (assume AI is right, tap to edit)
├── [Add 4 Items to My Closet] → celebration confetti
├── "Want to add more right now?"
│   ├── [📸 Another Outfit] [📷 From Gallery] [🛍️ From Screenshots]
│   └── DEFAULT: [Continue →] "Let's see what you can wear!"
└── See FIRST_WEEK_EXPERIENCE.md for second-by-second animation spec

Step 5: Style DNA + First Suggestion (30 seconds)
├── "Your Style DNA ✨" with computed archetype
├── Color palette from extracted items
├── 2-3 insight bullet points
├── First styling tip for tomorrow using their items
├── [Enable Morning Outfit Notification ☀️]
│   └── "We'll have a fresh idea ready at 8 AM"
└── [Let's Go →] → Home screen

(Body measurements, skin tone, detailed preferences → moved to Profile tab)
```

### Drop-off Prevention
- Every step has a [Skip] option
- Progress bar visible throughout (Step X of 5)
- Can always come back to complete later
- Minimum viable path: OAuth → Name → Tap 2 styles → Skip camera → Home (under 90 seconds)
- OOTD selfie is the hook but NOT a blocker — skipping still gets you to the app

---

## Journey 2: Daily Outfit Loop — The Two-Moment System

### Context
The daily loop has TWO moments, not one. Morning = intent (what you plan to wear). Evening = confirmation (what you actually wore). The gap between intent and reality is our richest learning signal.

### Morning Flow (2-3 minutes, getting ready)

```
1. Open App → Home / "Today" Tab
   ├── "Good morning, Priya" with weather (28°C ☀️ Mumbai)
   ├── Suggestion accuracy: "78% match rate this week" (visible proof of AI learning)
   └── If calendar connected: "You have 3 meetings today"

2. Today's Outfit Card (hero)
   ├── Outfit #1 of 3-5 options
   ├── Individual item photos arranged as outfit layout
   │   ├── Top → Bottom → Shoes → Accessory
   │   └── Tap any item → item detail
   ├── Badges: Style Score (87/100), Occasion (Office), Color Harmony ✓
   ├── Power Outfit ⭐ badge if previously rated 🔥
   └── "Why this works" expandable:
       ├── "Navy + cream is a classic office palette"
       ├── "Perfect for 28°C — breathable cotton"
       └── "You haven't worn this shirt in 2 weeks"

3. User Decision (INTENT — logged as "planned")
   ├── "Wear This ✓" → logged as PLANNED (not confirmed)
   │   → Haptic + checkmark animation
   │   → Streak day started
   │   → "Have a great day!"
   ├── "Show Me Another →" → next option slides in
   │   → Track: how many alternatives viewed (pickiness signal)
   │   → After 3-5: "Want to pick yourself?" nudge
   ├── "I'll Pick Myself" → opens Closet in quick-select mode
   │   → Manual outfit selection still counts for streak
   └── No action by noon → soft reminder notification

4. Post-decision
   ├── Quick stats: "You've worn 34 of 47 items this month 🎯"
   ├── Style tip of the day card
   ├── [📸 Log Today's OOTD] → camera for new item extraction
   └── Streak counter: "Day 5 🔥🔥"
```

### Evening Flow (30 seconds - 2 minutes, optional but incentivized)

```
7:00 PM notification: "How was today's outfit? 👍 or 👎"
(Only appears if they tapped "Wear This" that morning)

1. Quick Rate (from notification — 2 seconds)
   ├── 👍 → "Nice! We'll suggest similar combos"
   │   → outfit_history.status = 'confirmed'
   ├── 👎 → Opens app to "What was off?"
   └── Dismiss → Fine, no penalty

2. Rich Feedback (in-app — optional)
   ├── Emoji rating: 😫 😐 😊 😍 🔥
   ├── Quick tags (multi-select, 1 tap each):
   │   ✅ Comfortable  ✅ Got compliments
   │   ❌ Too hot/cold  ❌ Felt overdressed  ❌ Felt underdressed
   │   ❌ Uncomfortable fabric  ❌ Changed my outfit
   ├── IF "Changed my outfit":
   │   ├── [📸 OOTD Photo] → extracts what they REALLY wore
   │   │   → Adds NEW items to closet (passive growth!)
   │   │   → Logs real outfit to history
   │   ├── [Pick from closet] → select actual items
   │   └── [Skip] → mark as changed, no details
   ├── IF rating is 🔥: "Save as Power Outfit? ⭐"
   │   → Power Outfits get suggested for important days
   └── [Done] → "Thanks! Tomorrow's suggestion will be even better"

3. How feedback feeds back:
   ├── 👍 confirmed → boost same color combos, formality, occasion
   ├── 👎 "too formal" → reduce formality weight for this user
   ├── 👎 "too hot" → increase weather sensitivity
   ├── "got compliments" → flag as power outfit
   ├── "changed + OOTD photo" → learn real preference vs AI suggestion
   └── Over time: suggestion accuracy visibly improves on Today screen
```

### Intelligence Inputs
- Weather API (today's temp, humidity, rain probability)
- Calendar events (if connected — meeting types, dress codes)
- Outfit history (what was worn in last 7/14/30 days)
- **Evening feedback patterns** (confirmed vs changed, comfort tags, power outfit flags)
- **Suggestion accuracy trend** (% of planned outfits that were confirmed)
- Season + climate preferences
- Style DNA profile
- **Pickiness signal** (avg "Show Me Another" taps per session)

---

## Journey 3: Adding a New Item (1-2 minutes)

### Trigger
User bought something new, or is adding more items to their closet.

### Flow

```
1. Closet Tab → "+" button → Camera opens

2. Capture
   ├── Take photo (ideally flat-lay or on hanger)
   ├── OR select from gallery
   └── Image preview + "Use this photo" / "Retake"

3. AI Processing (2-3 seconds)
   ├── Loading animation: "Analyzing your item..."
   ├── Claude Vision extracts:
   │   ├── Category: Top
   │   ├── Subcategory: Blouse
   │   ├── Colors: [Navy, White]
   │   ├── Pattern: Striped
   │   ├── Material: Cotton
   │   ├── Formality: 3/5 (Smart Casual)
   │   ├── Occasions: [Office, Casual, Date Night]
   │   └── Seasons: [All-season]
   └── AI Description: "Navy and white striped cotton blouse with button-down collar"

4. User Review
   ├── All AI fields shown as editable chips/tags
   ├── Tap to change any incorrect tag
   ├── Add optional fields: brand, size, purchase price
   ├── "Looks right!" → Save
   └── Items rarely need correction (target: 90% accuracy)

5. Post-Save
   ├── "Added! This blouse creates 8 new outfit possibilities."
   ├── Quick outfit preview: shows 2-3 new combinations unlocked
   └── "Add another item" or return to closet
```

---

## Journey 4: Closet Insights (Weekly Check-in, 3-5 minutes)

### Trigger
User taps "Closet Insights" pill at bottom of Closet tab, or receives weekly digest notification.

### Flow

```
1. Insights Dashboard
   ├── Wardrobe Summary
   │   ├── Total items: 47
   │   ├── Items worn this month: 34 (72%)
   │   └── Estimated wardrobe value: ₹48,000

2. Usage Stats
   ├── Most worn items (top 5 with photos + wear counts)
   ├── "Hall of Fame" — items worn 10+ times
   ├── Never worn items (the "shame pile")
   │   ├── 8 items never worn
   │   ├── Each with days-since-added
   │   └── CTA: "Wear it this week?" / "Donate?" / "Sell?"
   └── Cost-per-wear breakdown
       ├── Best value: "White sneakers — ₹200/wear (worn 15x)"
       └── Worst value: "Red heels — ₹3,500/wear (worn 1x)"

3. Color Distribution
   ├── Pie/donut chart of wardrobe colors
   ├── "Your wardrobe is 40% blue, 25% black, 15% white..."
   └── "Missing warm tones — could add variety"

4. Category Balance
   ├── Bar chart: Tops (18) | Bottoms (8) | Dresses (5) | ...
   ├── Ideal ratio overlay
   └── "Heavy on tops, light on bottoms"

5. Style Evolution (after 30+ days)
   ├── Timeline showing style changes
   ├── "You've been dressing more casually this month"
   └── "Your color palette has expanded — nice!"

6. Gap Analysis (links to Discover/Shopping)
   ├── "A versatile blazer would unlock 12 new outfits"
   ├── Priority ranked suggestions
   └── "See recommendations →"
```

---

## Journey 5: Shopping Intelligence ("Before You Buy")

### Trigger A: Proactive gap analysis (Discover tab)

```
1. Discover Tab → "What's Missing"
   ├── Card: "A white sneaker would unlock 8 new outfits"
   │   ├── Shows outfit combination previews
   │   ├── Budget range: ₹2,000-5,000
   │   └── "See options →" → product links (affiliate)
   ├── Card: "You have no layering pieces for winter"
   │   └── Priority: High (winter approaching)
   └── Each suggestion shows "outfit unlock potential"

2. Product Recommendations
   ├── Curated picks per gap
   ├── Budget / Mid-range / Premium options
   ├── Each shows: photo, brand, price, "unlocks X outfits" badge
   └── "View on store →" (affiliate link)
```

### Trigger B: In-store scanner

```
1. User is in a store, about to buy something
2. Opens app → "Before You Buy" scanner
3. Takes photo of item on rack
4. AI analyzes → compares with existing wardrobe
5. Result A: "You already own 2 similar items" (shows them)
   └── "You might not need this"
6. Result B: "This is unique in your closet!"
   ├── "This would create 6 new outfit combinations"
   └── Shows which items it pairs with
7. Result C: "This is close to something you have, but different enough"
   └── "Your existing navy blazer is similar, but this one is more casual"
```

---

## Journey 6: Outfit Creation (Manual)

### Trigger
User wants to plan an outfit themselves (Outfits tab → "+" button).

### Flow

```
1. Outfit Builder
   ├── Canvas area showing outfit layout slots:
   │   Top / Bottom / Shoes / Outerwear / Accessory
   ├── Wardrobe items shown below as scrollable grid
   ├── Drag item → slot (or tap to assign)
   └── Filters: category, color, occasion

2. As items are added:
   ├── Real-time style score updates
   ├── Color harmony indicator
   ├── "This combination works because..."
   └── AI suggestions: "Try adding a gold accessory"

3. Save Outfit
   ├── Name (optional, AI suggests one)
   ├── Tag: occasion, season
   ├── Save → appears in Outfits tab
   └── "Wear this today?" option

4. Remix
   ├── Select a saved outfit
   ├── "Remix" → AI suggests variations
   │   ├── Swap the top for similar alternative
   │   ├── Dress it up / down
   │   └── Adapt for different weather
   └── Save variation as new outfit
```

---

## Journey 7: Subscription Upgrade

### Trigger
User hits a free tier limit or sees Pro feature teaser.

### Natural Upgrade Moments

```
1. Item Limit
   ├── "You've reached 30 items (free limit)"
   ├── "Upgrade to Pro for unlimited items"
   └── Shows items waiting to be added

2. Daily Outfit Limit
   ├── "You've seen today's outfit" (free: 1/day)
   ├── "Pro members get 5 daily suggestions"
   └── Teaser of what the next outfit could be

3. AI Auto-tagging
   ├── Free: manually tag items
   ├── Pro teaser: "Auto-tag with AI? Upgrade to Pro"
   └── Shows time savings: "Save 2 min per item"

4. Before You Buy
   ├── Free: 0 scans
   ├── Pro: 5/month
   ├── Premium: unlimited
   └── Shows scanner with locked overlay

5. Upgrade Screen
   ├── Plan comparison table
   ├── Annual discount highlighted (save 40%)
   ├── Free trial offer (7 days Pro)
   ├── Testimonials/social proof
   └── Stripe checkout integration
```

---

## Notification Strategy

### Daily — Two-Moment System
- **Morning outfit** (8 AM local): "Good morning! Today's outfit is ready ☀️"
  - Only if user has opened app 3+ times in last 7 days (avoid annoying churned users)
- **Evening check-in** (7 PM local): "How was today's outfit? 👍👎"
  - Only if user tapped "Wear This" that morning (nothing to rate otherwise)
  - Starts from Day 3 (not Day 1 — build trust first)
  - Actionable directly from notification (iOS/Android quick actions)
- **Max 2 notifications per day** (morning + evening). Never exceed this.

### Weekly
- **Closet digest** (Sunday evening): "This week: you wore 12 items. 5 items still waiting 👀"
- **Style tip**: "Try combining [item] with [item] this week"
- **Accuracy report** (after Week 2): "Your suggestion accuracy improved to 78% this week!"

### Contextual
- **Weather change**: "Rain expected tomorrow — we've updated your outfit suggestion"
- **Calendar event**: "You have [event] tomorrow. We've prepared an outfit"
- **Never-worn nudge**: "[Item] has been in your closet 30 days unworn. Time to try it?"
- **Power outfit moment**: "Important meeting tomorrow? We suggest your Power Outfit ⭐"

### Growth
- **Milestone**: "You've created 50 outfits! You're a style pro 🎉"
- **Streak**: "7-day outfit streak! Keep it going"
- **Referral**: "Share ClosetAI with a friend, both get 1 month Pro free"
- **Feedback loop**: "Your 10th rating! Suggestion accuracy jumped 12% this month"
