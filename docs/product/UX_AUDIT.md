# ClosetAI — UX Audit: Lovable Design vs Spec

**Date:** February 14, 2026
**Method:** Cloned `closetai-onboarding` Lovable repo, ran locally, captured 56 Playwright screenshots across all screens and states (31 round 1 + 25 round 2). Cross-referenced every screen against USER_JOURNEYS.md, FIRST_WEEK_EXPERIENCE.md, AI_DEEP_DIVE.md, and ONBOARDING_STRATEGY.md.

**Round 2 (Feb 14):** Re-pulled after 9 new Lovable screens were committed (ArchetypeReveal, AddItemSheet, WhatGoesWith, StateWelcomeBack, ItemDetail, AddItem, OutfitBuilder, OutfitRemix, BeforeYouBuy, Upgrade). Re-tested all flows. 17 files changed, +2292 lines.

---

## What's Built (Lovable Design Coverage)

| Screen | Status | Notes |
|---|---|---|
| Welcome | ✅ Matches spec | Clean, tagline + CTA + sign in link |
| Login (Google/Apple/Email) | ✅ Matches spec | OAuth buttons, email/password fallback |
| Signup | ✅ Matches spec | Name, email, password, terms |
| Onboarding Step 1 — About You | ✅ Matches spec | Name, gender (4 options), age group (4 options) |
| Onboarding Step 2 — Style Vibe | ✅ Matches spec | 3×3 grid, select 2-3, checkmarks |
| Onboarding Step 3 — Your Life | ⚠️ Extra step | Occasions, climate, budget — spec says move to Profile |
| Onboarding Step 4 — Scan Closet | ✅ Matches spec | Camera intro with 3-step process explanation |
| OOTD Camera | ✅ Excellent | Body outline guide, gallery, flash toggle, tips |
| OOTD Processing | ✅ Excellent | Shimmer sweep, glow outlines, item counter — nails the magic |
| OOTD Confirm | ✅ Good | Swipe to remove, edit category/occasion, checkmarks |
| Great Start (post-capture) | ✅ Matches spec | 4 items grid, add more options, continue CTA |
| First Tip | ✅ Good | Outfit suggestion + "Why this works" + notification opt-in |
| Today — JustOnboarded (1-4 items) | ✅ Good | Welcome banner, closet preview, style tip, notification nudge |
| Today — Growing (5-10 items) | ✅ Good | Outfit suggestion with score, progress bar |
| Today — Useful (10-25 items) | ✅ Good | Full outfit card, badges, why section, stats |
| Today — FullIntel (25+ items) | ✅ Good | Premium outfit card, trending badges, insights card |
| Evening Check-in | ✅ Matches spec | Quick rate → rich feedback → power outfit → completion |
| Streak Celebration | ✅ Good | 7-day modal with unlock badge, floating emojis |
| Closet Grid | ✅ Good | Category filters, 2-col grid, favorites, wear count |
| Closet Insights | ✅ Good | Most worn, forgotten, color dist, category balance |
| Outfits — Saved | ✅ Good | Cards with score/tags, wear again, remix, favorite |
| Outfits — Calendar | ✅ Good | Month view with dots, day detail card |
| Shop | ✅ Good | What's Missing, Complete the Look, Recommendations, Before You Buy card |
| Profile | ✅ Good | Avatar, style tag, settings menu, subscription link |
| Style DNA Detail | ✅ Excellent | Colors, power colors, formality, category balance, evolution, insights |
| **NEW — Round 2** | | |
| Archetype Reveal | ✅ Built | Fullscreen overlay, confetti particles, sparkle burst, trait pills, auto-dismiss 2.8s |
| Add Item Sheet | ✅ Built | Bottom sheet: Today's Outfit / Single Item / From Gallery |
| Item Detail (/closet/:id) | ✅ Built | Hero image, editable tags, stats, pairings, outfit history, archive/delete |
| What Goes With This | ✅ Built | Bottom sheet: top pairings %, complete outfits, missing pieces |
| Add Item (/add-item) | ✅ Built | Photo + shimmer analyzing, AI-detected tags as editable chips, add to closet |
| Outfit Builder (/outfit-builder) | ✅ Built | 5-slot canvas, real-time score, AI tips, wardrobe picker, save/wear |
| Outfit Remix (/outfit-remix) | ✅ Built | Swap top, dress up/down, weather adapt, score comparison |
| Before You Buy (/before-you-buy) | ✅ Built | Camera (simulated), 3 result types: Similar/Unique/Close |
| Upgrade (/upgrade) | ✅ Built | Free/Pro/Premium plans, annual toggle, testimonials |
| Welcome Back State | ✅ Built | 5 days away message, outfit suggestion, closet stats, re-engagement CTAs |

---

## Round 1 Gaps — Status After Round 2

| Gap | Original Status | Round 2 Status | Notes |
|---|---|---|---|
| Gap 1: Onboarding 6→5 steps | P0 Open | ⚠️ Still open | YourLife step still in flow, TOTAL_STEPS still = 6 |
| Gap 2: Archetype Reveal | P0 Open | ✅ Fixed | ArchetypeReveal.tsx added as fullscreen overlay after StyleVibe |
| Gap 3: Confetti on confirm | P1 Open | ⚠️ Still open | Code-only fix, not in Lovable design |
| Gap 4: 3-screen post-onboarding | P2 Open | ⚠️ Still open | Code-only fix |
| Gap 5: Suggestion accuracy metric | P1 Open | ⚠️ Still open | Code-only fix |
| Gap 6: Show Me Another counter | P2 Open | ⚠️ Still open | Code-only fix |
| Gap 7: Power Outfit badge | P1 Open | ⚠️ Still open | Code-only fix |
| Gap 8: Single-item add | P0 Open | ✅ Fixed | AddItemSheet + AddItem page built |
| Gap 9: Item Detail page | P0 Open | ⚠️ Partially fixed | Page exists at /closet/:id but NOT reachable from closet grid |
| Gap 10: Outfit Builder | P1 Open | ✅ Fixed | Full builder with canvas, scoring, wardrobe picker |
| Gap 11: Outfit Remix | P2 Open | ✅ Fixed | 3 remix cards: swap, formality, weather |
| Gap 12: Before You Buy | P2 Open | ✅ Fixed | Camera + 3 result variants |
| Gap 13: Empty states | P2 Open | ⚠️ Still open | `showEmpty` hardcoded false |
| Gap 14: Upgrade screen | P2 Open | ✅ Fixed | Full plan comparison with annual toggle |
| Gap 15: What Goes With This | P1 Open | ✅ Fixed | Bottom sheet with pairings, outfits, missing pieces |
| Gap 16: Accuracy pre-evening | P2 Open | ⚠️ Still open | Same as Gap 5 |
| Gap 17: Notification settings | P2 Open | ⚠️ Still open | No screen built |
| Gap 18: Welcome Back state | P0 Open | ✅ Fixed | Full welcome back state in Today |

**Summary: 8 of 18 gaps fixed by Lovable. 10 remain (7 are code-only fixes, 3 need attention).**

---

## Round 2 — New Gaps Found (14 Additional)

### P0 — Breaks Core Experience

#### Gap 19: Closet Item Tap Opens Pairings, Not Detail
- **Current:** Tapping any closet item opens the WhatGoesWith bottom sheet. The ItemDetail page exists at `/closet/:id` but has NO navigation path from the closet grid.
- **Spec:** Tap → Item Detail. Pairings accessible from within Item Detail.
- **Fix:** Tap item → navigate to `/closet/:id`. Move "What Goes With This?" to a section/button within ItemDetail (it's already there as a horizontal scroll — just needs the bottom sheet removed from Closet.tsx).
- **Why it matters:** Users can't edit tags, view outfit history, or see stats for any item. The most basic closet interaction is broken.
- **Design needed:** No — rewire navigation only.

#### Gap 20: "I'll Pick Myself" / "Wear This" / "Show Me Another" Are Dead Buttons
- **Current:** On ALL Today states (JustOnboarded, Growing, Useful, FullIntel), these core CTA buttons do nothing. No navigation, no state change, no feedback.
- **Spec:** "Wear This" → confirmation animation + log to history. "Show Me Another" → next suggestion + counter. "I'll Pick Myself" → outfit builder.
- **Fix:** Wire all three buttons:
  - "Wear This ✓" → brief confirmation animation ("Have a great day!") → log outfit to history
  - "Show Me Another" → swap suggestion + increment counter (after 3-5: "Want to pick yourself?" nudge)
  - "I'll Pick Myself" → navigate to `/outfit-builder`
- **Why it matters:** These are THE core daily interactions. A user opens the app, sees an outfit, and needs to act on it. Dead buttons = dead engagement.
- **Design needed:** Yes — Lovable Prompt J (Wear This confirmation animation + counter nudge)

#### Gap 21: No "Wear This" Confirmation / Dopamine Moment
- **Current:** No confirmation screen or animation when user accepts an outfit suggestion.
- **Spec (Two-Moment System):** Morning intent → "Wear This ✓" → confirmation with haptic feedback, checkmark animation, "Have a great day, Priya!" → outfit logged.
- **Fix:** Add brief confirmation overlay (0.8s) with checkmark animation, message, and subtle confetti. Auto-dismiss to Today screen with outfit-of-the-day card updated.
- **Why it matters:** This is the morning dopamine hit. Without it, wearing the suggestion feels like pressing a broken button. The confirmation creates a ritual.
- **Design needed:** Yes — Lovable Prompt J (combined with Gap 20)

---

### P1 — Significantly Impacts Daily Engagement

#### Gap 22: Profile Settings Menu Items Are All Dead
- **Current:** Profile shows 7 settings items (Style Preferences, Body Profile, Skin Tone & Colors, Notifications, Subscription, Privacy & Data, Help & Feedback). ALL lead nowhere.
- **Spec:** At minimum, Subscription → /upgrade, Notifications → notification settings form.
- **Fix:** Wire Subscription → `/upgrade`. Build notification settings as inline expandable or separate route. Other settings can be "Coming Soon" temporarily but should at least show a message.
- **Why it matters:** Users who want to customize their experience or upgrade hit dead ends. The Subscription link especially — we have /upgrade built but Profile doesn't link to it.
- **Design needed:** Notification settings needs a small form (Lovable Prompt K). Others are code wiring.

#### Gap 23: No Navigation Between Related Screens
- **Current:** Many screens reference each other but don't link:
  - Today outfit "Remix" concept exists in copy but no button to `/outfit-remix`
  - Outfits "Wear Again" button does nothing (should log outfit to today)
  - ItemDetail "See outfits" link in pairings section — no navigation
  - Shop "See outfits" / "View on Store" buttons — no navigation
  - GreatStart "From Gallery" / "From Screenshots" — no navigation
  - Calendar "Add from memory" — no navigation
  - BeforeYouBuy "Add to Wishlist" / "View Outfits" / "Buy Anyway" — no navigation
- **Fix:** Wire all cross-screen navigation. Key connections:
  - Today → can reach Outfit Remix for current suggestion
  - Outfits "Wear Again" → "Wear This" confirmation flow
  - Shop "View on Store" → external URL (or placeholder)
  - BeforeYouBuy → "Add to Wishlist" → Shop wishlist section
- **Why it matters:** Dead-end buttons erode trust. Users learn that buttons don't work and stop tapping.
- **Design needed:** No — code wiring only.

#### Gap 24: Evening Check-in Has No Time-Awareness
- **Current:** Evening Check-in is a demo button in the state switcher. No logic for when to show it.
- **Spec (Two-Moment System):** Triggered at user-configured evening time (default 8pm), only if user logged an outfit that morning.
- **Fix:** Add time-based trigger: if current time > evening_time AND user wore outfit today AND hasn't checked in → show Evening Check-in overlay. Also needs push notification.
- **Why it matters:** The two-moment system IS the daily engagement loop. Without the evening trigger, there's no feedback loop, no learning signal, no streak building.
- **Design needed:** No — logic/timing only. The UI is already perfect.

#### Gap 25: Outfit Builder "Wear Today?" Doesn't Connect to Today Screen
- **Current:** OutfitBuilder has a "Wear Today?" button that shows a toast and navigates to `/outfits`. Same for OutfitRemix.
- **Fix:** "Wear Today?" should → confirmation animation → log to outfit history → navigate to `/today` (not `/outfits`) with today's outfit updated.
- **Why it matters:** Wearing an outfit you just built should feel seamless and connected to the rest of the daily flow.
- **Design needed:** No — navigation fix.

---

### P2 — Important for Completeness & Polish

#### Gap 26: No Password Reset / Forgot Password Flow
- **Current:** Login has "Forgot password?" text but no navigation or flow.
- **Fix:** Build forgot password screen (email input → success message). Supabase Auth handles the actual reset email.
- **Design needed:** Yes — small screen, standard pattern (Lovable Prompt L or code-only).

#### Gap 27: No Loading / Skeleton States for Data-Dependent Screens
- **Current:** All screens render immediately with hardcoded data. In the real app, there will be API calls.
- **Fix:** Add skeleton loading states for: Today outfit card, Closet grid, Outfits list, Shop recommendations, ItemDetail, Style DNA.
- **Why it matters:** Without loading states, users see blank screens or layout shifts. Skeleton screens maintain perceived performance.
- **Design needed:** No — use shadcn Skeleton component (already in project).

#### Gap 28: No Error / Offline States
- **Current:** No error handling or offline detection anywhere.
- **Fix:** Add: (1) API error states with retry button, (2) Offline banner ("You're offline — showing cached data"), (3) Image load failures with placeholder.
- **Design needed:** No — standard error patterns.

#### Gap 29: Shop Search Is Non-Functional
- **Current:** Shop has a search input that accepts text but does nothing.
- **Fix:** Either implement search (filter products by query) or remove the search bar to avoid confusion. For MVP, filter existing recommendations by keyword.
- **Design needed:** No — code-only.

#### Gap 30: No Onboarding Data Persistence
- **Current:** All onboarding answers (name, gender, age, style selections, occasions) are local component state. Lost on refresh. Not passed to any API.
- **Fix:** In real app, each step saves to Supabase via API. In Lovable design, at minimum show that data flows forward (e.g., name entered in AboutYou appears in Today screen header).
- **Why it matters:** In the real build, this is critical. In the Lovable design, it's a reference issue.
- **Design needed:** No — backend implementation.

#### Gap 31: OOTD Confirm → GreatStart Doesn't Pass Items
- **Current:** ConfirmScreen navigates to `/great-start`. GreatStart shows hardcoded 4 items, not the items actually confirmed.
- **Fix:** In real app, pass confirmed items via route state or global store. GreatStart should show the actual items the user just added.
- **Design needed:** No — data flow fix.

#### Gap 32: StreakCelebration "See My Style DNA" Goes to /onboarding
- **Current:** After celebrating a 7-day streak, "See My Style DNA" navigates to `/onboarding` (the full onboarding flow!) instead of Profile → Style DNA.
- **Fix:** Navigate to `/profile` and trigger Style DNA detail view.
- **Why it matters:** Sending a 7-day user back to onboarding is confusing and breaks trust.
- **Design needed:** No — fix navigation target.

---

## Round 2 Gaps Summary

| # | Gap | Priority | Design Needed? |
|---|---|---|---|
| 19 | Item tap → pairings instead of detail | P0 | No |
| 20 | Dead CTA buttons on Today screen | P0 | Yes (Prompt J) |
| 21 | No "Wear This" confirmation animation | P0 | Yes (Prompt J) |
| 22 | Profile settings all dead | P1 | Yes (Prompt K) |
| 23 | No cross-screen navigation | P1 | No |
| 24 | Evening Check-in not time-aware | P1 | No |
| 25 | Outfit Builder "Wear Today?" wrong destination | P1 | No |
| 26 | No forgot password flow | P2 | Minimal |
| 27 | No loading/skeleton states | P2 | No |
| 28 | No error/offline states | P2 | No |
| 29 | Shop search non-functional | P2 | No |
| 30 | Onboarding data not persisted | P2 | No |
| 31 | OOTD items not passed to GreatStart | P2 | No |
| 32 | Streak DNA link goes to /onboarding | P2 | No |

*(Round 1 gap details preserved in git history. See "Round 1 Gaps — Status After Round 2" table above for current status.)*

---

## Lovable Prompts Status

| Prompt | Screen | Priority | Gap | Status |
|---|---|---|---|---|
| A | Style Archetype Reveal (interstitial) | P0 | Gap 2 | ✅ Built |
| B | Closet Item Detail Page | P0 | Gap 9 | ✅ Built (nav broken) |
| C | Single Item Add (bottom sheet + review) | P0 | Gap 8 | ✅ Built |
| D | Outfit Builder | P1 | Gap 10 | ✅ Built |
| E | Outfit Remix Flow | P2 | Gap 11 | ✅ Built |
| F | Before You Buy Scanner | P2 | Gap 12 | ✅ Built |
| G | Welcome Back / Returning User State | P0 | Gap 18 | ✅ Built |
| H | Subscription / Upgrade Screen | P2 | Gap 14 | ✅ Built |
| I | "What Goes With This?" Bottom Sheet | P1 | Gap 15 | ✅ Built |

### New Prompts Needed (Round 2)

| Prompt | Screen | Priority | Gap |
|---|---|---|---|
| J | "Wear This" confirmation animation + "Show Me Another" counter nudge | P0 | Gap 20, 21 |
| K | Notification Settings form (in Profile) | P1 | Gap 22, 17 |
| L | Forgot Password screen | P2 | Gap 26 |

---

## Impact By User Type (Updated Round 2)

| User Type | Before Round 1 | After Round 1 (9 screens added) | Remaining Gaps |
|---|---|---|---|
| **New User (Day 1)** | 6-step onboarding, no archetype wow, no confetti, only OOTD add | Archetype reveal, single-item add, 3 add options | Still 6 steps (YourLife not removed), no confetti on confirm, OOTD items don't pass to GreatStart |
| **Daily User (1 week)** | Can't self-style, no visible learning, no Power Outfits | Outfit builder, remix, closet insights | "Wear This" / "Show Me Another" / "I'll Pick Myself" are dead buttons. No accuracy metric. No evening trigger. |
| **Intermittent User (3+ days)** | Same screen as daily user | Welcome back state with re-engagement | No actual time-detection logic. Streak broken display. |
| **Power User (25+ items)** | Can't interact with closet items | Item Detail page, What Goes With This, Before You Buy | Can't reach ItemDetail from closet (tap → pairings instead). No cross-screen navigation. |
| **Upgrade-Curious User** | No upgrade screen | Full plan comparison with pricing | Profile → Subscription doesn't link to /upgrade. No paywall triggers. |

---

## All Remaining Fixes (Consolidated)

### Design Needed (3 Lovable Prompts)

| # | What | Prompt | Priority |
|---|---|---|---|
| 1 | "Wear This" confirmation animation + "Show Me Another" counter + nudge | J | P0 |
| 2 | Notification Settings form | K | P1 |
| 3 | Forgot Password screen | L | P2 |

### Code-Only Fixes (No New Designs)

**P0 — Must fix:**
1. Remove YourLife step from onboarding flow (Gap 1 — still open)
2. Fix closet item tap: tap → ItemDetail, not WhatGoesWith (Gap 19)
3. Wire Today CTAs: "Wear This" → confirm, "Show Me Another" → swap, "I'll Pick Myself" → /outfit-builder (Gap 20)
4. Fix StreakCelebration "See My Style DNA" → /profile not /onboarding (Gap 32)

**P1 — Important:**
5. Wire Profile → Subscription to /upgrade (Gap 22)
6. Wire all cross-screen navigation (Gap 23 — see full list above)
7. Add evening check-in time-awareness trigger (Gap 24)
8. Fix Outfit Builder / Remix "Wear Today?" → /today not /outfits (Gap 25)
9. Add confetti on OOTD confirm (Gap 3)
10. Add suggestion accuracy badge to Today states (Gap 5)
11. Add Power Outfit ⭐ badge to outfit cards (Gap 7)
12. Enable empty states by default (Gap 13)

**P2 — Polish:**
13. Add "Show Me Another" counter + nudge after 3-5 (Gap 6)
14. Merge/streamline GreatStart + FirstTip flow (Gap 4)
15. Add skeleton loading states for all data screens (Gap 27)
16. Add error/offline handling (Gap 28)
17. Fix or remove Shop search bar (Gap 29)
18. Pass OOTD items through to GreatStart (Gap 31)

### End-to-End Workflow Verification Checklist

When building the real app, verify these complete user journeys work:

- [ ] **New user onboarding:** Welcome → Login → AboutYou → StyleVibe → ArchetypeReveal → ScanCloset → OOTD → Confirm → GreatStart → FirstTip → Today
- [ ] **Daily morning ritual:** Open app → Today screen → See outfit → "Wear This" → confirmation → outfit logged
- [ ] **Evening feedback:** Notification → Evening Check-in → Quick rate → (optional rich feedback) → accuracy updated
- [ ] **Add single item:** Closet → FAB → "Single Item" → camera → AI analysis → review tags → "Add to Closet" → back to closet with new item
- [ ] **Browse closet:** Closet grid → tap item → ItemDetail → edit tags / view stats / see pairings → back
- [ ] **Build outfit manually:** Today "I'll Pick Myself" → OutfitBuilder → add items → see score → "Wear Today?" → confirmation → logged
- [ ] **Remix outfit:** Outfits → select outfit → "Remix" → pick variation → "Wear Today?" → confirmation → logged
- [ ] **Before you buy:** Shop → "Before You Buy" card → camera → scan → result (similar/unique/close) → action
- [ ] **Upgrade flow:** Profile → Subscription → /upgrade → pick plan → "Start Free Trial" → Stripe checkout
- [ ] **Welcome back:** 3+ days away → open app → Welcome Back state → outfit suggestion → "Log OOTD" or accept suggestion
- [ ] **Streak building:** 7 consecutive days → StreakCelebration modal → "See Style DNA" → Profile DNA view

---

## Lovable Prompt J — "Wear This" Confirmation + Counter Nudge

```
Add two new interaction components to the existing ClosetAI Today screen. This is a mobile-first app (390x844) using the existing design system: rose (#E8A0BF) primary, cream (#FFF8F5) bg, charcoal text, gold (#C9A96E) accents, Playfair Display headings, Inter body. Use shadcn/ui + Tailwind CSS.

Component 1: "Wear This" Confirmation Overlay
When the user taps "Wear This ✓" on their daily outfit suggestion, show a brief fullscreen overlay animation:
- Background: Semi-transparent cream with blur (backdrop-filter)
- Center: Large animated checkmark (draws in, like iOS success). Rose color (#E8A0BF).
- Below checkmark: "Have a great day, Priya! ✨" in Playfair Display
- Subtle confetti burst (5-8 rose/gold particles floating up) — nothing heavy
- Auto-dismiss after 1.2 seconds, transition back to Today screen
- The outfit card should then show a "Wearing today ✓" badge in rose

Component 2: "Show Me Another" Counter + Nudge
Track how many times the user taps "Show Me Another" in a session:
- First 2 taps: Just swap the outfit card (use different mock outfits)
- Tap 3: Show a small counter badge on the button ("3 alternatives viewed")
- Tap 5: Replace the "Show Me Another" button with a gentle nudge card:
  "Feeling picky today? 🎨"
  "Want to build your own outfit?"
  Two buttons: "Yes, I'll pick myself →" (rose filled, navigates to /outfit-builder) and "Show me one more" (text link)
- The nudge card should animate in with a subtle slideUp

Both components should feel premium and intentional — not heavy or intrusive. The confirmation should create a tiny dopamine hit. The nudge should feel helpful, not judgmental.
```

## Lovable Prompt K — Notification Settings

```
Add a Notification Settings screen to the existing ClosetAI Profile page. Mobile-first (390x844), same design system: rose primary, cream bg, charcoal text. shadcn/ui + Tailwind CSS.

This can be a separate route (/profile/notifications) or an expandable section within Profile.

Settings to include:
1. "Morning Outfit" notification
   - Toggle switch (on/off)
   - Time picker: "When should we suggest your outfit?" (default 7:30 AM)
   - Subtitle: "Get a daily outfit suggestion to start your day"

2. "Evening Check-in" notification
   - Toggle switch
   - Time picker (default 8:00 PM)
   - Subtitle: "Quick feedback helps us learn your style"

3. "Weekly Style Digest" notification
   - Toggle switch
   - Day picker: "Which day?" (Mon-Sun, default Sunday)
   - Subtitle: "Your weekly wardrobe insights and trends"

4. "Weather Alerts" notification
   - Toggle switch
   - Subtitle: "Outfit adjustments when weather changes significantly"

5. "Sale Alerts" notification
   - Toggle switch
   - Subtitle: "When items on your wishlist go on sale"

Layout: Clean list with toggles on the right side. Each item has icon, title, subtitle, and toggle. Time/day pickers appear below the toggle when enabled. Use the existing ClosetAI card/section styling. Back button at top to return to Profile.
```

## Lovable Prompt L — Forgot Password

```
Add a simple Forgot Password screen to ClosetAI. Mobile-first (390x844), same design system.

Route: /forgot-password (linked from Login page "Forgot password?" text)

Screen 1 (Enter Email):
- Back arrow to /login
- Heading: "Reset Password" (Playfair Display)
- Subtitle: "Enter your email and we'll send you a reset link"
- Email input field (same style as Login)
- "Send Reset Link" button (rose filled, full width)
- "Back to Sign In" text link

Screen 2 (Success — shown after submit):
- Envelope/mail icon (large, centered, rose tint)
- Heading: "Check Your Email"
- Text: "We've sent a password reset link to priya@email.com"
- "Didn't receive it? Resend" text link
- "Back to Sign In" button (outlined)

Keep it minimal — this is a utility screen, not a feature showcase.
```
