# ClosetAI - User Journeys

## Journey 1: First-Time Onboarding (5-7 minutes)

### Goal
Get user from download → closet with 10+ items → first outfit suggestion in under 7 minutes.

### Flow

```
Step 1: Welcome Screen
├── "Your closet, but smarter."
├── Beautiful minimal illustration
├── [Continue with Google] ← primary (one-tap)
├── [Continue with Apple]
└── [Continue with Email]

Step 2: Tell Us About You (30 sec)
├── Name (pre-filled from OAuth if available)
├── Gender (visual selector: Women / Men / Non-binary / Prefer not to say)
│   └── Affects: category labels, style archetypes, occasion types
└── Age group (18-24 / 25-34 / 35-44 / 45+)
    └── Affects: style suggestion tone, trend relevance

Step 3: Your Body (optional, 1 min)
├── Height slider (cm/ft toggle)
├── Weight slider (kg/lbs toggle)
├── Body type selection
│   ├── Visual silhouettes (not text labels)
│   ├── Options shown are gender-appropriate
│   └── "Not sure? Skip — AI will learn from your photos"
└── [Skip] always available

Step 4: Your Colors (1 min)
├── Skin tone picker (visual swatches, 7 options)
│   ├── Fair, Light, Medium, Olive, Tan, Brown, Deep
│   └── Carousel with model photos for reference
├── OR: "Upload a selfie for AI analysis"
│   ├── Camera/upload prompt
│   ├── Claude Vision analyzes skin tone + undertone
│   └── Shows result for confirmation
├── Result: "Your Power Colors" palette (5-6 colors)
└── Result: "Colors to be careful with" (2-3 colors)

Step 5: Your Style Vibe (1 min)
├── 3×3 grid of outfit photos (women's fashion)
│   ├── Casual Chic
│   ├── Classic Elegant
│   ├── Street Style
│   ├── Bohemian
│   ├── Minimalist
│   ├── Ethnic/Fusion
│   ├── Sporty
│   ├── Romantic
│   └── Edgy
├── User taps 2-3 that resonate
├── AI computes style archetype from selections
└── Shows: "You're a Modern Classic with Streetwear Edge"

Step 6: Your Life (1 min)
├── Occasion priority (drag to rank top 4)
│   ├── Office/Work
│   ├── Casual Everyday
│   ├── Date Night
│   ├── Fitness/Gym
│   ├── Travel
│   ├── Events/Parties
│   ├── Ethnic/Traditional
│   └── Work From Home
├── Climate selector (Tropical / Temperate / Cold / Variable)
└── Monthly clothing budget slider ($0-500+)

Step 7: Scan Your Closet (2-3 min) ← THE HOOK
├── Exciting CTA: "Let's see what you've got!"
├── Quick capture mode
│   ├── "Lay items on bed/hang them up, snap photos"
│   ├── Continuous camera mode (snap, snap, snap)
│   ├── Each photo → Claude Vision auto-detects:
│   │   category, color, pattern, style, formality
│   ├── User sees items appear in grid in real-time
│   └── Can tap any item to adjust AI labels
├── OR: Upload from gallery (batch select)
├── Target: 10-20 items minimum
├── Progress: "12 items added! Great start."
└── [Skip for now, I'll add items later]

Step 8: Your Style DNA is Ready!
├── Beautiful visualization of computed style profile
├── Style archetype name + visual badge
├── Color palette wheel (wardrobe colors + power colors)
├── Wardrobe summary (X items detected)
├── 3 insight cards:
│   ├── "Your wardrobe is 70% casual, 20% office, 10% party"
│   ├── "Blue and black dominate — try adding warm tones"
│   └── "You have 8 tops but only 2 bottoms"
└── CTA: "Let's pick your first outfit!" → Home
```

### Drop-off Prevention
- Every step has a [Skip] option
- Progress bar visible throughout (Step X of 8)
- Can always come back to complete later
- Minimum viable path: OAuth → Name → Skip body → Skip colors → Pick 2 styles → Skip closet → Home (under 2 min)

---

## Journey 2: Daily Morning Routine (2-3 minutes)

### Context
User opens app in the morning, getting ready for the day.

### Flow

```
1. Open App → Home / "Today" Tab
   ├── "Good morning, Priya" with weather (28°C ☀️ Mumbai)
   └── If calendar connected: "You have 3 meetings today"

2. Today's Outfit Card (hero)
   ├── Outfit #1 of 3-5 options
   ├── Individual item photos arranged as outfit layout
   │   ├── Top → Bottom → Shoes → Accessory
   │   └── Tap any item → item detail
   ├── Badges: Style Score (87/100), Occasion (Office), Color Harmony ✓
   └── "Why this works" expandable:
       ├── "Navy + cream is a classic office palette"
       ├── "Perfect for 28°C — breathable cotton"
       └── "You haven't worn this shirt in 2 weeks"

3. User Decision
   ├── "Wear This ✓" → logs to history, items marked as worn today
   ├── "Show Me Another →" → swipe/tap for next suggestion
   ├── "I'll Pick Myself" → opens Closet tab
   └── "Not feeling it" → feedback: too casual? too formal? wrong vibe?

4. Post-decision
   ├── Quick stats: "You've worn 34 of 47 items this month 🎯"
   ├── Style tip of the day card
   └── Notification scheduled for tomorrow morning
```

### Intelligence Inputs
- Weather API (today's temp, humidity, rain probability)
- Calendar events (if connected — meeting types, dress codes)
- Outfit history (what was worn in last 7/14/30 days)
- User feedback patterns (accepted/rejected outfit styles)
- Season + climate preferences
- Style DNA profile

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

### Daily
- **Morning outfit** (8 AM local): "Good morning! Today's outfit is ready ☀️"
- Only if user has opened app 3+ times in last 7 days (avoid annoying churned users)

### Weekly
- **Closet digest** (Sunday evening): "This week: you wore 12 items. 5 items still waiting 👀"
- **Style tip**: "Try combining [item] with [item] this week"

### Contextual
- **Weather change**: "Rain expected tomorrow — we've updated your outfit suggestion"
- **Calendar event**: "You have [event] tomorrow. We've prepared an outfit"
- **Never-worn nudge**: "[Item] has been in your closet 30 days unworn. Time to try it?"

### Growth
- **Milestone**: "You've created 50 outfits! You're a style pro 🎉"
- **Streak**: "7-day outfit streak! Keep it going"
- **Referral**: "Share ClosetAI with a friend, both get 1 month Pro free"
