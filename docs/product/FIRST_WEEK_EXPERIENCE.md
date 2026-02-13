# ClosetAI - First Week Experience: The Make-or-Break Window

## TL;DR

The first 7 days decide everything. Day 1 creates the "wow" through magical AI item extraction from a mirror selfie. Days 2-7 build the habit through daily outfit suggestions that visibly improve as the closet grows. By Day 7, the user has 15-25 items, genuinely useful suggestions, a streak they don't want to break, and the feeling that "this app gets me." Every screen adapts based on closet size — we never show an empty, useless state.

---

## The OOTD Selfie: Designing the "Wow" Moment

This is our Shazam moment. When Shazam identifies a song, there's magic — the pulsing animation, the anticipation, the satisfying reveal. Our equivalent: take a mirror selfie, watch AI extract your individual clothing items in real-time.

### Why This Moment Matters

- It's the first time the user sees ClosetAI's intelligence
- If it feels magical, they tell friends. If it feels clinical, they close the app.
- The extracted items with clean backgrounds make their closet look premium instantly
- This is the screenshot moment — the thing they'll share on WhatsApp/Instagram

### The Exact Flow (Second by Second)

```
T+0.0s  User taps camera button
        → Haptic feedback (iOS .impact, Android 50ms vibration)
        → Camera opens with framing guide overlay
        → Guide shows: "Stand in front of a mirror, full body visible"
        → Subtle animated dotted outline showing ideal framing

T+1-5s  User takes selfie
        → Shutter haptic + subtle flash animation
        → Photo zooms to fill screen (300ms ease-out transition)

T+0.3s  Processing begins — THE MAGIC STARTS
        → Photo stays on screen
        → A warm-toned shimmer sweep moves across the photo
          (left to right, 1.5s duration, rose-gold gradient)
        → Text appears: "Analyzing your outfit..." in elegant Inter font
        → Below: skeleton cards start appearing (showing HOW MANY items
          will be found — builds anticipation)

T+2.0s  Detection phase
        → Shimmer continues on photo
        → On the photo itself: subtle glowing outlines appear around
          detected garments (like Pinterest Lens does)
        → Counter animates: "Found 1... 2... 3... 4 items!"
        → Each number triggers a tiny haptic pulse

T+3.0s  THE REVEAL — Items cascade in
        → Photo slides up to top 40% of screen
        → Below: items appear one by one with staggered cascade
        → Each item: fade-in + slight slide-up + scale 0.9→1.0
        → Timing: 100ms between each item
        → Each item card shows:
          ┌──────────────────────────────┐
          │  [Clean extracted photo]      │  ← Transparent bg, drop shadow
          │                              │
          │  Navy Silk Blouse   [✓ Yes]  │  ← Category auto-detected
          │  Top · Formal · Navy/White   │  ← Quick-confirm or tap to edit
          └──────────────────────────────┘

T+3.5s  All items visible
        → Brief pause (200ms) for user to see everything
        → Then: subtle sparkle animation on the item count
        → "4 items found!" badge with Sparkles icon

T+4.0s  User confirms
        → Each item has a [✓] that's already pre-selected
          (assume AI is right — user only taps to CHANGE, not to confirm)
        → Tap any item card to expand: edit category, colors, tags
        → Bottom: big CTA "Add 4 Items to My Closet"

T+5.0s  Success celebration (FIRST TIME ONLY)
        → On tap "Add to Closet":
        → Items fly up and "collect" into a closet icon (300ms)
        → Confetti burst (subtle, 50 particles, rose-gold themed)
        → Haptic: success pattern
        → "Your closet is started! 🎉"
        → Brief pause, then transition to next screen
```

### The "Add More" Flow

After the first OOTD is confirmed, present options WITHOUT pressure:

```
Screen: "Great Start!"
├── "4 items in your closet"
├── Your items shown as a mini grid (sense of accomplishment)
│
├── "Want to add more right now?"
│   ├── [📸 Another Outfit]     ← Opens camera again
│   │     "Wearing something different? Snap it!"
│   │
│   ├── [📷 From Gallery]       ← Photo picker
│   │     "Add photos you've already taken"
│   │
│   ├── [🛍️ From Myntra/Amazon] ← Explain share feature
│   │     "Screenshot a product → share to ClosetAI"
│   │
│   └── DEFAULT: [Continue →]   ← BIGGEST BUTTON, primary color
│         "Let's see what you can wear!"
│
└── Note: "Continue" is the default action.
    Adding more is optional and never feels required.
    The button hierarchy makes "Continue" the obvious path.
```

### If They Choose to Add More

- Camera opens again with same magic flow
- Each additional OOTD goes through the same extraction
- Counter updates: "4 items → 8 items → 12 items"
- After each batch: same "Add more or Continue?" screen
- After 3 batches (12+ items): the app gently suggests:
  "Amazing! 12 items is enough for great suggestions. You can always add more later."

### Gallery Upload Flow

If they choose "From Gallery":
- Photo picker opens (multi-select enabled)
- Selected photos queue up
- Each photo gets the same AI extraction (but batch-processed)
- Show progress: "Processing photo 1 of 3..."
- All extracted items presented at once for bulk confirmation
- Same staggered cascade reveal for each photo's items

### Error Handling (When AI Struggles)

```
If photo is too dark/blurry:
├── "Hmm, the lighting made this tricky 📸"
├── Show what WAS detected (even partial results)
├── "Want to try with better lighting?"
├── [Retake] [Use what we found] [Skip]
└── NEVER: "Error: Detection failed" or "Processing error"

If only 1-2 items detected (expected 3-4):
├── "We found 2 items! Some might be hidden in the photo"
├── Show detected items normally
├── "Tap + to manually add items we missed"
└── Treat as partial success, not failure

If AI misidentifies an item:
├── User taps the wrong item card
├── Quick edit: category dropdown + color picker + tag editor
├── Swipe left to remove entirely
├── "Thanks for the correction — we'll learn from this!"
└── Store correction as training signal for future
```

### Copy That Makes It Magical

**During processing:**
- "Analyzing your outfit..." (not "Processing image...")
- "Finding your pieces..." (not "Running detection model...")
- "Almost there..." (not "Please wait...")

**On reveal:**
- "Found 4 pieces!" (not "4 objects detected")
- "Looking stylish!" (not "Analysis complete")

**On confirm:**
- "Your closet is growing!" (not "Items saved to database")

### Animation Specifications (For Developers)

```css
/* Shimmer sweep on photo */
.shimmer-sweep {
  background: linear-gradient(
    90deg,
    transparent 0%,
    rgba(232, 160, 191, 0.15) 50%,  /* Rose with low opacity */
    transparent 100%
  );
  animation: sweep 1.5s ease-in-out infinite;
}

/* Item card reveal */
.item-card-enter {
  animation: revealItem 400ms ease-out forwards;
  opacity: 0;
  transform: translateY(20px) scale(0.95);
}
@keyframes revealItem {
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

/* Stagger: nth-child delay */
.item-card:nth-child(1) { animation-delay: 0ms; }
.item-card:nth-child(2) { animation-delay: 100ms; }
.item-card:nth-child(3) { animation-delay: 200ms; }
.item-card:nth-child(4) { animation-delay: 300ms; }

/* Confetti: use canvas-confetti library */
/* Config: 50 particles, rose/gold colors, 2s duration */
confetti({
  particleCount: 50,
  spread: 60,
  colors: ['#E8A0BF', '#C9A96E', '#FDEBD3'],
  origin: { y: 0.7 }
});
```

---

## The First Outfit Suggestion (Day 1 Cold Start)

The user has 3-4 items from their first OOTD. We can't generate a completely new outfit. But we CAN deliver value.

### What We Show (3-4 Items)

```
Screen: "Here's a Style Idea for Tomorrow"
┌────────────────────────────────────────┐
│                                        │
│  [Same items arranged differently]      │
│  OR                                     │
│  [Styling tip applied to their items]   │
│                                        │
│  ─────────────────────────────────────  │
│                                        │
│  "Style Tip: Try tucking your navy     │
│   blouse into your jeans and rolling    │
│   the sleeves — instant polished        │
│   casual look. The white sneakers       │
│   keep it relaxed."                     │
│                                        │
│  Why this works:                        │
│  • Navy + white is a timeless combo     │
│  • Tucked blouse elongates your frame   │
│  • Great for: Office → After-work drinks│
│                                        │
│  ─────────────────────────────────────  │
│                                        │
│  [Love This 💛] [Show Me Another →]    │
│                                        │
│  "The more items you add, the more      │
│   outfit combos we can create!"         │
│                                        │
│  [Enable Morning Outfit Notification ☀️]│
│  "We'll have a fresh idea at 8 AM"     │
│                                        │
└────────────────────────────────────────┘
```

### The Claude Prompt for Day 1 (Few Items)

```python
FEW_ITEMS_PROMPT = """
You are a personal stylist. The user just started using ClosetAI
and has only {count} items in their closet:

{items_with_descriptions}

Since there aren't enough items for a completely new outfit,
provide a STYLING TIP for tomorrow using these same items.

Suggest ONE of these approaches:
1. A different way to WEAR the same items (tucked vs untucked,
   sleeves rolled, layering order, accessory placement)
2. How to transition the outfit for a different OCCASION
   (office → evening, casual → meeting)
3. Which single item is most versatile and why

Return as JSON:
{
  "suggestion_type": "styling_tip" | "occasion_shift" | "versatility_spotlight",
  "title": "short catchy title",
  "description": "2-3 sentences of actionable styling advice",
  "items_used": ["item_ids used"],
  "why_it_works": ["2-3 short reasons"],
  "occasions": ["what occasions this works for"],
  "add_more_nudge": "what ONE item type would unlock the most new outfits"
}
"""
```

### How "Show Me Another" Works With Few Items

With 3-4 items, there are limited combinations. Instead of showing the same items rearranged:

```
Suggestion 1: Styling tip (how to wear the items differently)
Suggestion 2: Occasion shift (same outfit, different context)
Suggestion 3: Versatility spotlight (deep dive on one item)
```

After 3 suggestions: "Add more items to unlock more ideas! 📸"

---

## Day-by-Day: The First Week

### Day 1 — "This App Sees Me"

**Goal:** Create wonder. User feels the AI understands their style.

```
Onboarding (3 minutes):
├── OAuth → Name → Style Vibe grid → OOTD selfie → Items extracted
├── First styling tip from their items
├── Morning notification opt-in
└── User leaves with: 3-4 items, style archetype, one tip

Evening (optional):
├── If they come back: "How was today's outfit? 📸 Log it?"
└── If not: fine, we'll prompt tomorrow morning
```

**Today screen state (3-4 items):**
- Greeting + weather
- "Welcome to ClosetAI!" banner (first time only)
- Style archetype card: "You're a Modern Classic"
- Style tip (not full outfit — not enough items)
- "What goes with this?" tap any item for pairing ideas
- "Add more items" (secondary, not pushy)
- Notification reminder if not enabled

### Day 2 — "It Remembered Me"

**Goal:** The morning notification works. User opens app, sees their items, logs today's OOTD.

```
8:00 AM notification:
"Good morning! Here's a style idea for today ☀️"

User opens → Today screen:
├── "Good morning, Priya! ☀️ 28°C Mumbai"
├── Today's Suggestion:
│   ├── Styling tip from their 3-4 items
│   ├── "Why this works" (Claude-generated reasoning)
│   └── [Love This 💛] [Show Me Another →]
├── After decision: "📸 What are you wearing today?"
│   └── OOTD selfie → 3-4 NEW items extracted
│   └── "8 items in your closet! Getting to know your style..."
├── Streak: "Day 2"
└── "Tomorrow's suggestion will have more variety!"
```

**Key:** After they log today's OOTD, show a preview:
"With 8 items, we can now create 6 outfit combinations. Tomorrow's suggestion will be a REAL outfit, not just a styling tip!"

This creates anticipation for Day 3.

### Day 3 — "It's Actually Useful Now"

**Goal:** First REAL outfit combination from mixed items. The quality jump is noticeable.

```
8:00 AM notification:
"Your first real outfit combo is ready! 🎉"

User opens → Today screen:
├── "Good morning, Priya! ☀️ 30°C Mumbai"
├── Today's Outfit: (FIRST REAL COMBINATION)
│   ├── [Day 1 top] + [Day 2 bottom] + [Day 1 shoes]
│   ├── Items they've never worn together
│   ├── Style score: 78/100
│   ├── "Why this works":
│   │   ├── "Navy blouse + khaki trousers = office-ready contrast"
│   │   ├── "Perfect for 30°C — both items are breathable cotton"
│   │   └── "You haven't tried this combo yet!"
│   └── [Wear This ✓] [Show Me Another →] [I'll Pick Myself]
├── After decision: "📸 Log today's OOTD"
│   └── 10-12 items now
├── Streak: "Day 3 🔥"
└── Quick stat: "You've already found 3 new outfit combinations!"
```

**Why Day 3 matters:** This is where the app proves its intelligence. The user wore these items separately on Day 1 and Day 2. ClosetAI combined them in a way the user hadn't thought of. THAT'S the value.

### Day 4 — "It's Learning"

**Goal:** Accept/reject feedback starts showing results. User sees the AI adapting.

```
If user rejected a formal suggestion on Day 3:
├── Day 4 suggestion is more casual
├── Subtle acknowledgment: "Based on what you've liked, here's
│   something more relaxed for today"
└── User feels: "It's paying attention"

If user accepted a bold color combo on Day 3:
├── Day 4 suggestion includes another bold element
├── "You liked the navy + mustard combo — here's another
│   unexpected pairing from your closet"
└── User feels: "It gets me"

Today screen:
├── 12-16 items
├── 2 outfit options available (can "Show Me Another")
├── Streak: "Day 4 🔥"
├── Closet growth: "16 items — your suggestions are getting smarter!"
└── Nudge: "Have items you haven't photographed yet?
    Try Batch Mode: lay 5 items on your bed, snap once 📸"
```

### Day 5 — "I Rely on It"

**Goal:** Habit forms. User opens the app before getting dressed — it's part of the morning routine.

```
Today screen:
├── 16-20 items
├── 3 outfit options (real variety now)
├── Weather integration matters: "Rain expected this afternoon —
│   we picked water-resistant shoes"
├── Streak: "Day 5 🔥🔥"
├── Quick insight: "You've worn 12 of your 20 items this week"
└── "Share today's outfit with friends?" (first social prompt)
```

### Day 6 — "It Knows My Gaps"

**Goal:** First closet intelligence insight. User sees the analytical power.

```
Today screen:
├── 20-24 items
├── 3-5 outfit options
├── NEW SECTION: "Quick Insight"
│   └── "You have 8 tops but only 3 bottoms. That's why some
│       tops keep pairing with the same jeans. A couple more
│       bottoms would double your outfit options."
├── Streak: "Day 6 🔥🔥"
└── "Tomorrow is Day 7 — unlock your Style DNA Insights! ⭐"
```

### Day 7 — "I Can't Delete This App"

**Goal:** Milestone celebration. Unlock Style DNA insights. User feels invested.

```
On opening app:
├── 🎉 "7-Day Streak! You're a style natural!"
├── Celebration animation (confetti, achievement badge)
├── "UNLOCKED: Style DNA Insights ⭐"
│
│   Style DNA Card:
│   ├── "Your Style DNA: Modern Classic with Ethnic Fusion Edge"
│   ├── Color wheel showing their wardrobe colors
│   ├── Category balance visualization
│   ├── "Your wardrobe is 60% casual, 25% office, 15% ethnic"
│   ├── Top insight: "Navy and black dominate — adding warm tones
│   │   like terracotta or mustard would expand your palette"
│   └── "Your most versatile item: [White sneakers] — used in
│       5 outfit combinations this week"
│
├── Gap Analysis Preview:
│   └── "A structured blazer would unlock 12 new outfit combos →"
│
├── Today's outfit (full intelligence, 5 options)
├── Streak: "Day 7 🔥🔥🔥"
└── "Tell a friend about ClosetAI?" (share prompt)

By Day 7, user has:
├── 25-30 items (from 7 daily OOTDs + maybe 1-2 batch adds)
├── 7 days of outfit history
├── Accept/reject data training the AI
├── A streak they don't want to break
├── Style DNA that feels personal
├── First gap analysis insight
└── The feeling: "This app understands my wardrobe better than I do"
```

---

## How the Today Screen Adapts

The Today screen is NEVER empty. It always has something useful, but what it shows scales with closet size.

### State 1: New User (0 items, pre-onboarding)

```
"Your closet, but smarter."
[Start Now →] (takes to onboarding)
```

### State 2: Just Onboarded (1-4 items)

```
"Welcome to ClosetAI! ✨"

Your Style: Modern Classic
[Style archetype card with visual]

Your Items (mini grid of 3-4 extracted items)

Today's Style Tip:
"Your navy blouse is incredibly versatile — it works tucked
into trousers for the office, or loose over jeans on weekends.
The key is in the accessories."

[What Goes With This?] → tap any item for pairing ideas

"Add more items to unlock outfit suggestions!"
├── [📸 Add Outfit] [📷 From Gallery]
└── [Enable Morning Notifications ☀️]
```

### State 3: Growing Closet (5-10 items)

```
"Good morning, Priya! ☀️ 28°C Mumbai"

Today's Suggestion:
[Outfit card with 2-3 items + styling tip]
Style Score: 72/100
"Why this works" (1-2 reasons)
[Love This 💛] [Show Me Another →]

Your Closet: 8 items
[Progress bar] "Add 2 more items to unlock weather-smart suggestions"

Streak: Day 3 🔥

[📸 Log Today's OOTD]
```

### State 4: Useful Closet (10-25 items)

```
"Good morning, Priya! ☀️ 28°C Mumbai"

Today's Outfit:
[Full outfit card — top, bottom, shoes, optional accessory]
Style Score: 84/100 | Office | Color Harmony ✓
"Why this works":
  • "Navy + cream creates professional contrast"
  • "Cotton breathes well in today's 28°C heat"
  • "Haven't worn this combination in 2 weeks — fresh!"
[Wear This ✓] [Show Me Another →] [I'll Pick Myself]

Quick Stats: 16/22 items worn this week (73%)
Streak: Day 5 🔥🔥

Style Tip: "Roll your sleeves to the elbow to
instantly make any blouse feel more relaxed"

[📸 Log Today's OOTD]
```

### State 5: Full Intelligence (25+ items)

```
"Good morning, Priya! ☀️ 28°C Mumbai"   [🔔]

Today's Outfit:
[2x2 item grid with outfit visualization]
Style Score: 91/100 | Office → Evening | ✓ Color Harmony
Badges: "Trending" (trend-aware), "Fresh Combo" (never worn together)

"Why this works":
  • "This color palette is trending on Pinterest this week"
  • "Blazer dresses it up for your 2pm meeting"
  • "Remove the blazer → ready for evening drinks"
  • "Haven't worn the silk blouse in 12 days — time to bring it back"
[Wear This ✓] [Show Me Another →] [I'll Pick Myself]

34/47 items worn this month (72%) | 12 outfit streak 🔥

Style Tip Card:
"The art of the 'third piece': a scarf, belt, or jacket that
transforms a basic outfit into a styled look."

🔍 "3 items you haven't worn in 2 weeks — let's style them"

[📸 Log Today's OOTD]
```

---

## How All 5 Tabs Adapt

### Tab 1: TODAY — Covered above

### Tab 2: CLOSET

**0-4 items:**
```
"Your Closet"  4 items  [+ Add]

[Grid showing 3-4 items]

"Your closet is just getting started!"
"Every day you log an outfit, it grows automatically."

[📸 Add an Outfit] [📷 Quick Add from Gallery]
```

**5-15 items:**
```
"My Closet"  12 items  [+ Add]

Category chips: [All] [Tops(5)] [Bottoms(3)] [Shoes(2)] [Accessories(2)]

[2-column grid of items]
Each card: photo, name, times worn badge

"Closet Insights" pill → basic stats
```

**25+ items:**
```
"My Closet"  47 items  [+ Add]

Category chips: [All] [Tops(18)] [Bottoms(8)] [Dresses(5)] [Ethnic(4)] ...
Filter row: Sort (Recent/Most Worn/Least Worn) | Color | Season

[2-column masonry grid]
Each card: photo, name, times worn, heart icon
Items not worn in 30+ days: subtle amber "forgotten" indicator

"Closet Insights" floating pill at bottom
├── Most worn items (top 5)
├── Never worn items (shame pile)
├── Color distribution chart
├── Category balance
├── Cost-per-wear (if purchase price entered)
└── "Your most versatile item: White sneakers (in 8 outfits)"
```

### Tab 3: OUTFITS

**0-2 saved outfits:**
```
"Outfits"

[Friendly illustration]
"No saved outfits yet!"
"Accept today's outfit suggestion to save your first combo."

[See Today's Suggestion →]
```

**3-10 saved outfits:**
```
"My Outfits"  7 outfits

[List of outfit cards]
Each: thumbnail grid of items, name, occasion tag, date last worn

[+ Create Outfit] → manual outfit builder
```

**10+ saved outfits:**
```
"My Outfits"  24 outfits

[Calendar View] toggle: see what you wore each day
[List View] toggle: browse saved outfits

Filters: Occasion | Season | Favorites

Each outfit card:
├── Item thumbnails
├── Style score + occasion
├── "Last worn: 5 days ago"
├── [Remix] → AI creates a variation
└── [Wear Again] → logs to today's history
```

### Tab 4: SHOP (Discover)

**< 15 items:**
```
"Smart Shopping"

"We need to know your closet better before making
shopping recommendations."

"Keep adding items — we'll unlock shopping insights at 15 items!"
[Progress bar: 10/15]

Meanwhile: "Before You Buy" scanner
├── "About to buy something?"
├── "Take a photo — we'll check if you already own something similar"
└── [Open Scanner 📸]
```

**15+ items:**
```
"Smart Shopping"  [Search bar]

"What's Missing" section:
├── "A white sneaker would unlock 8 new outfits" [High]
├── "You need a layering piece for monsoon season" [Medium]
└── Each with outfit preview thumbnails

"Complete the Look" section:
├── Horizontal scroll of your items
├── Tap one → see what's missing to complete outfits with it

"Recommended" product grid:
├── Budget / Mid-range / Premium picks
├── Each: photo, brand, price, "+N outfits" badge
└── "View on Store →" (affiliate link)

"Before You Buy" CTA
```

### Tab 5: PROFILE

**Always available (adapts in depth):**
```
"Profile"

[Avatar + name]
"Modern Classic" style archetype badge

Style DNA Visualization:
├── Color wheel (from wardrobe colors) — richer with more items
├── Formality spectrum bar
├── Category balance donut chart
├── Style evolution (after 30+ days): "Getting bolder this month!"
└── (Initially simple, grows complex with data)

Settings:
├── My Preferences (skin tone, body type — things skipped in onboarding)
├── Notification Settings
├── Morning outfit time (default 8 AM)
├── Subscription (Free / Pro / Premium)
├── Privacy & Data
└── Sign Out
```

---

## Notification Strategy (First Week)

### Day 1 (Onboarding Day)
- **No notification** — they just signed up, don't be pushy

### Day 2 — 8:00 AM
- "Good morning! Your first style idea is ready ☀️"
- If they DON'T open: reminder at 12:00 PM: "Still thinking about what to wear? We have a suggestion 👗"

### Day 3 — 8:00 AM
- "Your first real outfit combo is ready — mixing items from two days! 🎉"

### Day 4 — 8:00 AM
- "Based on what you've liked, today's suggestion is more [casual/bold/etc.] ✨"

### Day 5 — 8:00 AM
- "Day 5! Rain expected — we picked weather-appropriate items ☔"
- **Evening 7 PM:** "How was today's outfit? Quick rate: 👍👎" (first evening engagement)

### Day 6 — 8:00 AM
- "Quick insight: you have way more tops than bottoms. Today's outfit works around that 🧠"

### Day 7 — 8:00 AM
- "🔥 7-Day Streak! Unlock your Style DNA Insights today ⭐"
- This notification should feel special — different emoji, exclamation, achievement language

### Rules
- NEVER send more than 2 notifications per day
- If user hasn't opened app in 3+ days, switch to re-engagement: "Your closet misses you — 3 unworn items waiting to be styled 👀"
- If user opens app before notification: skip the notification
- Always respect notification settings

---

## The Streak System (Detail)

### How It Works

```
OOTD logged today? → Streak continues
No OOTD today?    → Streak freezes (1 free freeze per week)
No OOTD + no freeze? → Streak resets to 0
```

### Streak Freeze
- 1 free freeze per week (auto-used if they miss a day)
- Pro subscribers get 3 freezes per week
- "Your streak was saved! You have 0 freezes left this week"
- This is the Duolingo pattern — 21% churn reduction from streak freeze alone

### Streak Milestones

| Streak | Celebration | Unlock |
|--------|------------|--------|
| Day 1 | "First OOTD logged!" | Basic outfit tips |
| Day 3 | "🔥 3-day streak!" | Real outfit combinations |
| Day 7 | "🔥🔥 7-day streak!" | Style DNA Insights |
| Day 14 | "🔥🔥🔥 14-day streak!" | Closet Analytics dashboard |
| Day 30 | "⭐ 30-day streak!" | Full wardrobe intelligence |
| Day 100 | "💎 100-day streak!" | Badge + premium trial |

### Visual Treatment
- Streak appears on Today screen with fire emoji
- Streak number in bottom nav on Today tab (small badge)
- Milestone celebrations: full-screen overlay with animation (dismissible)

---

## Feature Unlock Progression

Features unlock based on closet SIZE (not subscription tier). This motivates adding items.

| Items | Unlock | UI Signal |
|-------|--------|-----------|
| 1 | "What goes with this?" | Immediate |
| 5 | Daily outfit suggestions | "Suggestions unlocked!" toast |
| 10 | Weather-aware suggestions | "Now checking weather!" toast |
| 15 | Shopping gap analysis | "Shopping insights unlocked!" |
| 25 | Full closet analytics | "Analytics dashboard unlocked!" |
| 30 | "Before You Buy" scanner | "Duplicate scanner unlocked!" |
| 50 | Seasonal wardrobe planning | "Season planner unlocked!" |

The subscription (Pro/Premium) unlocks LIMITS on these features (free gets 1 outfit/day, Pro gets 5), but the features themselves are unlocked by engagement.

---

## The "Wear This → Wore This" Two-Moment System

### The Problem: Intent ≠ Reality

When a user taps "Wear This ✓" in the morning, that's an **intent signal**, not confirmation they actually wore it. Users change their mind — a stain on the top, weather shifts, mood changes, forgot about a meeting. If we log morning taps as "worn," our AI trains on lies.

The gap between "planned" and "actual" is our most valuable data:

| Signal | What It Tells Us | AI Weight |
|--------|-----------------|-----------|
| Accepted + Actually Wore | This combo genuinely works | 2x positive |
| Accepted + Rated 🔥 | Power outfit — save for important days | 2.5x positive |
| Accepted + Got Compliments | Social proof — strong confidence signal | 3x positive |
| Accepted + Changed | Liked the idea, something was wrong (fit, weather, mood) | Weak 0.3x positive + investigate reason |
| Accepted + Changed + Photo of what they wore | Their REAL preference when our pick missed | Strong learning signal |
| Rejected in morning | Style mismatch — suppress this pattern | -1x negative |
| Ignored entirely | Not engaged, or notification timing off | Neutral |

### Morning Flow: Intent (Zero Friction)

```
Today's Outfit suggestion
├── [Wear This ✓]
│   → Haptic + checkmark animation
│   → Logged as "planned" on calendar (NOT "confirmed")
│   → Streak day started ✓
│   → "Have a great day!"
│
├── [Show Me Another →]
│   → Next option slides in
│   → Track: how many alternatives viewed (pickiness signal)
│   → After 3-5: "Want to pick yourself?" nudge
│
├── [I'll Pick Myself]
│   → Opens closet in quick-select mode
│   → Tap items to build outfit manually
│   → Save → counts as "planned" for streak
│
└── No action by noon
    → Soft reminder: "Still deciding? Your outfit is waiting"
    → If no action all day → use streak freeze or break streak
```

**Key design decision:** "Wear This" counts for streak IMMEDIATELY. Zero friction in the morning. The habit is opening the app and engaging — we don't want ANY barrier here.

### Evening Flow: Confirmation (Incentivized, Not Required)

This is where the real learning happens. Two paths — ultra-quick and rich:

```
7:00 PM notification: "How was today's outfit? 👍 or 👎"

PATH A: Quick Rate (2 seconds, from notification itself)
├── 👍 tap → "Nice! We'll suggest similar combos"
│   → Strong positive signal saved
├── 👎 tap → Opens app to "What was off?"
│   → Quick tag selection (see below)
└── Dismiss → No penalty, no streak impact

PATH B: Rich Feedback (in-app, optional)
"How did today's outfit go?"

├── Emoji rating: 😫 😐 😊 😍 🔥
│
├── Quick tags (multi-select, 1 tap each):
│   ✅ "Comfortable all day"
│   ✅ "Got compliments"
│   ❌ "Too hot/cold"
│   ❌ "Felt overdressed"
│   ❌ "Felt underdressed"
│   ❌ "Uncomfortable fabric"
│   ❌ "Changed my outfit"
│
├── IF "Changed my outfit" selected:
│   "What did you actually wear?"
│   ├── [📸 Quick OOTD Photo]  ← GROWTH HACK
│   │   → Extracts items from what they ACTUALLY wore
│   │   → Adds any NEW items to closet (passive growth!)
│   │   → Logs the REAL outfit to history
│   │   → We now know: planned A, wore B — rich signal
│   ├── [Pick from closet] → select items manually
│   └── [Skip] → just mark as "changed"
│
├── Optional: "Any notes?" (free text, small input)
│   → "Iron this shirt next time" / "Perfect for monsoon"
│
└── [Done ✓]
    → "Thanks! Tomorrow's suggestion will be even better 💛"
    → If rating was 🔥: "Save as a Power Outfit? ⭐"
```

### How to Incentivize Evening Check-in

The hard part — why would users bother? These four mechanisms work:

**1. Visible "Smart Score" that improves with feedback**
- Show on Today screen: "Suggestion accuracy: 72% → 78% this week"
- This number only goes up when they give feedback
- Visible proof that their input makes the AI better
- "Your feedback this week improved suggestions by 6%"

**2. Power Outfit detection (🔥 ratings)**
- If they rate 🔥 or select "got compliments": "Save as Power Outfit? ⭐"
- Power Outfits get a ⭐ badge, suggested for important days (meetings, dates, events)
- Only unlocked through the evening rating flow
- Creates a personal "best of" collection they're proud of

**3. Make it FAST**
- 👍/👎 from notification = 2 seconds
- Quick tags = 5 seconds
- Full feedback with OOTD photo = 30 seconds
- Most days it's just 👍 and done

**4. The "Changed Outfit" OOTD is a closet growth hack**
- If they changed their outfit, taking a photo of what they ACTUALLY wore adds new items
- So the closet grows even when the AI was "wrong"
- The "wrong" suggestion led to a "right" outcome (more items)
- Frame it as: "Oh you changed? Show us — we'll learn AND grow your closet!"

**5. Quality metric (not punitive)**
- Morning tap = streak day started, evening confirm = streak day COMPLETED
- Don't BREAK streak for skipping evening — that's too punitive
- But show: "Confirmed: 5/7 days this week" as a quality indicator
- After 3 skipped evening confirms: gentle nudge "Confirming helps us learn your style 3x faster"

### How Feedback Feeds Back Into the AI

```python
# Feedback signal weight system
SIGNAL_WEIGHTS = {
    "accepted_and_confirmed": 2.0,           # Strong positive — wore it, liked it
    "accepted_and_rated_high": 2.5,          # Very strong — enthusiastic
    "accepted_and_got_compliments": 3.0,     # Power outfit signal
    "accepted_but_changed": 0.3,             # Weak positive — liked idea, not execution
    "accepted_changed_weather": 0.5,         # Not a style issue, weather model needs calibration
    "accepted_changed_comfort": -0.5,        # Item has comfort problem — suppress in combos
    "accepted_changed_occasion": 0.2,        # Occasion mismatch — improve calendar integration
    "rejected_morning": -1.0,                # Don't suggest this pattern
    "rejected_too_formal": -0.8,             # Reduce formality weight for this user
    "rejected_too_casual": -0.8,             # Increase formality weight for this user
    "ignored": 0.0,                          # No signal
}

# What each feedback adjusts:
# 👍 → boost: same color combos, same formality level, same occasion mapping
# 👎 "too formal" → reduce formality preference weight for this user's profile
# 👎 "too hot" → increase weather sensitivity multiplier for this user
# "got compliments" → flag combo as power outfit, suggest for meetings/dates/events
# "changed outfit" + OOTD photo → learn their real preference when suggestion misses
# "uncomfortable fabric" → add item-level metadata, suppress item in hot weather combos
# "changed" reason tracking → over time reveals patterns (always changes on Mondays = different Monday context?)
```

### Database Schema for Two-Moment System

```sql
-- Enhanced outfit_history for intent vs. confirmation
ALTER TABLE outfit_history ADD COLUMN status TEXT DEFAULT 'planned';
  -- 'planned' (morning accept), 'confirmed' (evening ✓), 'changed' (wore something else)

ALTER TABLE outfit_history ADD COLUMN comfort_tags TEXT[];
  -- ['comfortable', 'got_compliments', 'too_hot', 'too_cold',
  --  'felt_overdressed', 'felt_underdressed', 'uncomfortable_fabric']

ALTER TABLE outfit_history ADD COLUMN changed_to_outfit_id UUID REFERENCES outfits(id);
  -- If they changed, link to what they actually wore

ALTER TABLE outfit_history ADD COLUMN is_power_outfit BOOLEAN DEFAULT FALSE;
  -- Rated 🔥 or "got compliments" — gets ⭐ badge, suggested for important days

-- Track suggestion accuracy per user
ALTER TABLE onboarding_progress ADD COLUMN suggestion_accuracy NUMERIC DEFAULT 0;
  -- % of accepted outfits that were confirmed (not changed)
ALTER TABLE onboarding_progress ADD COLUMN total_confirmed INTEGER DEFAULT 0;
ALTER TABLE onboarding_progress ADD COLUMN total_changed INTEGER DEFAULT 0;
```

### Notification Updates for Evening Check-in

```
Day 1:  No evening notification (just signed up)
Day 2:  No evening notification (too early, building trust)
Day 3:  7 PM: "How was today's outfit? Quick rate 👍👎" (first evening check-in)
Day 4:  7 PM: "Was today's outfit a hit? 👍👎"
Day 5:  7 PM: "How was today's outfit? Quick rate 👍👎"
        → After their 3rd evening rating: "Your feedback has improved suggestion accuracy by 8%!"
Day 6:  7 PM: "Quick rate! 👍👎" (shorter, they know the drill)
Day 7:  7 PM: "Rate today + see your weekly style recap! ✨"
        → Special: weekly summary unlocks after Day 7 evening confirm
```

**Rules:**
- Evening notification only appears if they tapped "Wear This" that morning
- If they didn't engage in the morning, no evening check-in (nothing to rate)
- Max 1 evening notification per day
- Combined with morning: max 2 notifications per day (unchanged)
- "Dismiss" is always fine — never punish for skipping

### How It Integrates With the First Week

Update to the day-by-day flow:

```
Day 1: Morning → OOTD onboarding. No evening check-in.
Day 2: Morning → suggestion + OOTD. No evening check-in yet.
Day 3: Morning → first real outfit combo + "Wear This".
        Evening → FIRST evening check-in: "How was the outfit? 👍👎"
        This is when the two-moment system starts.
Day 4: Morning → personalized suggestion (informed by Day 3 feedback).
        Evening → 👍👎 + if they changed, ask why.
Day 5: Morning → weather-aware suggestion.
        Evening → 👍👎 + "3 confirmed days — accuracy improving!"
Day 6: Morning → gap-aware suggestion.
        Evening → 👍👎 + quick tags available.
Day 7: Morning → full intelligence + 7-day streak celebration.
        Evening → Weekly recap: "You confirmed 4/5 outfits. Top combo: [X]. Power outfit: [Y]."
```

### Sources

- [Stitch Fix Feedback Loop Architecture](https://algorithms-tour.stitchfix.com/)
- [Duolingo Session Ratings (iOS 18)](https://www.cultofmac.com/news/duolingo-ios-18-session-ratings/)
- [The Power of Micro-Feedback in UX](https://uxdesign.cc/micro-interactions-why-when-and-how-to-use-them-to-boost-the-ux-17094b3baaa0)
- [BeReal OOTD Sharing Model](https://www.businessofapps.com/data/bereal-statistics/)
- [NPS vs In-App Feedback (UserPilot)](https://userpilot.com/blog/in-app-feedback/)

---

## Key Metrics to Track (First Week)

| Metric | Day 1 Target | Day 7 Target | What It Tells Us |
|--------|-------------|-------------|-----------------|
| Onboarding completion | 75%+ | — | Is the flow too long? |
| First OOTD taken | 70%+ | — | Is the camera step intimidating? |
| Items confirmed (not edited) | 80%+ | 85%+ | Is AI accuracy good enough? |
| Day 2 return | — | 50%+ | Did the hook work? |
| Day 7 return | — | 30%+ | Is habit forming? |
| Average items per OOTD | 3-4 | 3-4 | Is segmentation working? |
| Outfit suggestion open rate | — | 40%+ | Are notifications effective? |
| Suggestion accept rate | — | 30%+ | Are suggestions useful? |
| "Show Me Another" rate | — | 20-40% | Users want more (good!) |
| Streak freeze used | — | < 30% | Most don't need it (ideal) |
| Evening check-in rate | — | 40%+ | Are users closing the feedback loop? |
| Evening quick rate (👍) | — | 70%+ of check-ins | Is the outfit generally right? |
| "Changed outfit" rate | — | < 20% | How often does reality differ from plan? |
| Power outfit (🔥) rate | — | 10-15% of confirmed | Are we creating standout combos? |
| Suggestion accuracy (confirmed/total) | — | 60%+ | Core AI quality metric |
| Changed + took OOTD photo | — | 30%+ of "changed" | Closet growth from feedback loop |

---

## Sources

- [Shazam Animation Architecture](https://medium.com/@veniosg/behind-the-scenes-of-the-shazam-animation-9bc7f922b2be)
- [Duolingo Streak Psychology](https://www.justanotherpm.com/blog/the-psychology-behind-duolingos-streak-feature)
- [Duolingo Streak Freeze 21% Churn Reduction](https://blog.duolingo.com/how-duolingo-streak-builds-habit/)
- [Skeleton Screens 101 (NNGroup)](https://www.nngroup.com/articles/skeleton-screens/)
- [Animation Duration Best Practices (NNGroup)](https://www.nngroup.com/articles/animation-duration/)
- [The Illusion of Time in UX](https://medium.com/swlh/the-illusion-of-time-8f321fa2f191)
- [ModiFace AR Beauty Tech](https://www.modiface.com/)
- [PhotoRoom Background Removal UX](https://www.photoroom.com/)
- [Duolingo Onboarding Breakdown](https://goodux.appcues.com/blog/duolingo-user-onboarding)
- [Micro-Interaction Design Patterns](https://bricxlabs.com/blogs/micro-interactions-2025-examples)
- [canvas-confetti Library](https://github.com/catdad/canvas-confetti)
