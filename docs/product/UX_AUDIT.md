# ClosetAI — UX Audit: Lovable Design vs Spec

**Date:** February 14, 2026
**Method:** Cloned `closetai-onboarding` Lovable repo, ran locally, captured 31 Playwright screenshots across all screens and states. Cross-referenced every screen against USER_JOURNEYS.md, FIRST_WEEK_EXPERIENCE.md, AI_DEEP_DIVE.md, and ONBOARDING_STRATEGY.md.

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

---

## Gaps Found (18 Total)

### P0 — Breaks the Core Experience (Must Fix for MVP)

#### Gap 1: Onboarding is 6 Steps — Spec Says 5
- **Current:** AboutYou → StyleVibe → YourLife → ScanCloset → StyleDNA → (step 6?)
- **Spec:** Auth → AboutYou → StyleVibe → OOTD Selfie → Style DNA (5 steps)
- **Fix:** Remove "YourLife" step from onboarding flow. Move occasions/climate/budget to Profile → Style Preferences.
- **Why it matters:** Every added onboarding step loses ~10% of users. We're losing an extra 10% for data we don't need upfront.
- **Design needed:** No — just remove the step. YourLife component moves to Profile settings.

#### Gap 2: No Archetype Reveal After Style Vibe Selection
- **Current:** After selecting 2-3 styles, advances directly to next step.
- **Spec:** "You're a Modern Classic ✨" ← FIRST WOW MOMENT. Brief animated interstitial.
- **Fix:** Add 2.5-second archetype reveal screen between Style Vibe and OOTD step.
- **Why it matters:** This is the first time the app "sees" the user. It creates an emotional bond and makes the user feel understood.
- **Design needed:** Yes — Lovable Prompt A

#### Gap 8: Closet "+" Only Does OOTD — No Single-Item Add
- **Current:** + FAB in Closet → navigates to /ootd (full outfit photo).
- **Spec (Journey 3):** Adding a single item via flat-lay or hanger photo, with individual item AI analysis.
- **Fix:** + button opens bottom sheet with 3 options: Full Outfit Photo / Single Item Photo / From Gallery.
- **Why it matters:** This is the primary way users grow their closet day-to-day. OOTD extracts multiple items but isn't suitable for adding a new purchase.
- **Design needed:** Yes — Lovable Prompt C

#### Gap 9: No Closet Item Detail Page
- **Current:** Tapping an item in the closet grid does nothing.
- **Spec (Journey 3, 4):** Item Detail page with editable tags, outfit history, pairings, stats, archive/delete.
- **Fix:** Add /closet/:id route with full item detail page.
- **Why it matters:** Users need to correct AI tags, see outfit history, and discover pairings. Without this, the closet is just a photo album.
- **Design needed:** Yes — Lovable Prompt B

#### Gap 18: No "Welcome Back" State for Returning Users
- **Current:** Intermittent user (3+ days away) sees the same Today screen as a daily user.
- **Spec:** Not explicitly in current docs — identified during audit.
- **Fix:** Add a "welcome back" adaptive state to the Today screen when last_active > 3 days.
- **Why it matters:** Intermittent users are the hardest to retain. Without acknowledgment and gentle re-engagement, they feel like they've "fallen off" and are more likely to churn.
- **Design needed:** Yes — Lovable Prompt G

---

### P1 — Significantly Improves Daily Engagement

#### Gap 3: No Confetti on "Add Items to Closet"
- **Current:** ConfirmScreen navigates to /great-start without celebration.
- **Spec:** "[Add 4 Items to My Closet] → celebration confetti"
- **Fix:** Add confetti animation on confirm button tap, before navigation.
- **Design needed:** No — code-only (e.g., canvas-confetti library)

#### Gap 5: No Suggestion Accuracy Metric on Today Screen
- **Current:** None of the 4 Today states show suggestion accuracy.
- **Spec (Two-Moment System):** "Suggestion accuracy: 78% match rate this week" — visible proof AI is learning.
- **Fix:** Add accuracy badge to FullIntel and Useful Today states.
- **Design needed:** No — add to existing component

#### Gap 7: No Power Outfit ⭐ Badge on Outfit Cards
- **Current:** Today FullIntel shows "Trending 🔥" and "Fresh Combo" but no Power Outfit badge.
- **Spec:** "Power Outfit ⭐ badge if previously rated 🔥"
- **Fix:** Add conditional "Power Outfit ⭐" badge to outfit cards.
- **Design needed:** No — add badge to existing component

#### Gap 10: No Outfit Builder / Manual Creation Screen
- **Current:** Outfits page has "+ Create" button but no destination screen.
- **Spec (Journey 6):** Full outfit builder with canvas slots, wardrobe picker, real-time scoring, AI suggestions.
- **Fix:** Build /outfits/create route with builder screen.
- **Why it matters:** Users who want to self-style (vs. accepting AI suggestions) need this. It's also the path for "I'll Pick Myself" from the Today screen.
- **Design needed:** Yes — Lovable Prompt D

#### Gap 15: No "What Goes With This?" Interaction
- **Current:** JustOnboarded state says "Tap any item for pairing ideas" but nothing happens on tap.
- **Spec (implied):** Tapping a closet item shows AI-suggested pairings.
- **Fix:** Add bottom sheet with pairing suggestions, complete outfit ideas, and missing pieces.
- **Why it matters:** This is a key daily engagement feature — users browse their closet and discover new combinations.
- **Design needed:** Yes — Lovable Prompt I

---

### P2 — Important for Monetization & Completeness

#### Gap 4: Style DNA + First Tip Split Into 3 Screens
- **Current:** StyleDNA (onboarding) → GreatStart → FirstTip — three separate screens.
- **Spec:** Step 5 combines Style DNA result + first styling tip + notification opt-in.
- **Fix:** Merge GreatStart and FirstTip into a single post-onboarding screen, or streamline the 3-screen flow to feel faster.
- **Design needed:** No — code restructuring

#### Gap 6: No "Show Me Another" Counter or Nudge
- **Current:** "Show Me Another" button exists but doesn't track taps.
- **Spec:** "After 3-5: 'Want to pick yourself?' nudge". Tap count is a "pickiness signal" for the AI.
- **Fix:** Track alternatives viewed per session; after 3-5, show "Want to pick yourself?" nudge.
- **Design needed:** No — code-only

#### Gap 11: No Outfit Remix Flow
- **Current:** Outfit cards have "Remix ✨" button but no destination.
- **Spec (Journey 6):** Remix suggests variations — swap top, dress up/down, adapt for weather.
- **Fix:** Build remix bottom sheet or screen.
- **Design needed:** Yes — Lovable Prompt E

#### Gap 12: No "Before You Buy" Scanner Screen
- **Current:** Shop page has a "Before You Buy" card but no actual scanner.
- **Spec (Journey 5):** Full scanner flow — photograph item in store → compare with wardrobe → verdict.
- **Fix:** Build /shop/scanner route with camera + 3 result variants.
- **Why it matters:** This is a KEY differentiator and the feature most likely to go viral ("check if you already own it before buying").
- **Design needed:** Yes — Lovable Prompt F

#### Gap 13: No Empty States Shown in Default Flow
- **Current:** Outfits and Closet have empty state components (disabled in code).
- **Fix:** Enable empty states as the default when count is 0.
- **Design needed:** No — already built, just needs to be enabled

#### Gap 14: No Subscription / Upgrade Screen
- **Current:** Profile shows "Free Plan" with "Upgrade to Pro" text but no upgrade screen.
- **Spec (Journey 7):** Full plan comparison, annual toggle, free trial, Stripe checkout.
- **Fix:** Build /profile/upgrade route.
- **Design needed:** Yes — Lovable Prompt H

#### Gap 16: Suggestion Accuracy Missing Pre-Evening on Today Screen
- **Current:** Accuracy only shows in Evening Check-in completion state.
- **Spec:** Visible on Today screen throughout the day as motivation to provide feedback.
- **Fix:** Covered by Gap 5 fix.
- **Design needed:** No

#### Gap 17: No Notification Settings Screen
- **Current:** Profile → Notifications menu item exists but no destination screen.
- **Fix:** Build notification preferences screen (morning time, evening time, weekly digest, weather alerts).
- **Design needed:** Yes — small screen, can be part of Profile settings (no separate Lovable prompt needed, use standard form pattern)

---

## New Lovable Prompts Needed (9 Total)

| Prompt | Screen | Priority | Gap |
|---|---|---|---|
| A | Style Archetype Reveal (interstitial) | P0 | Gap 2 |
| B | Closet Item Detail Page | P0 | Gap 9 |
| C | Single Item Add (bottom sheet + review) | P0 | Gap 8 |
| D | Outfit Builder | P1 | Gap 10 |
| E | Outfit Remix Flow | P2 | Gap 11 |
| F | Before You Buy Scanner | P2 | Gap 12 |
| G | Welcome Back / Returning User State | P0 | Gap 18 |
| H | Subscription / Upgrade Screen | P2 | Gap 14 |
| I | "What Goes With This?" Bottom Sheet | P1 | Gap 15 |

Full prompt text for each is provided to Amol separately for Lovable generation.

---

## Impact By User Type

| User Type | Before (current Lovable) | After (with gap fixes) |
|---|---|---|
| **New User (Day 1)** | 6-step onboarding, no archetype wow, no confetti, can only add items via full OOTD | 5-step onboarding, wow moment, dopamine hits, single-item and gallery add |
| **1-Week User** | Good daily suggestions but no visible learning signal, no Power Outfits, can't self-style | Sees accuracy improving, Power Outfits rewarded, outfit builder + remix |
| **Intermittent User (3+ days away)** | Same screen as daily user — confusing, no re-engagement | Warm welcome back, gentle re-engagement, quick catch-up |
| **Power User (daily, 25+ items)** | Full suggestions but can't deeply interact with closet items | Item detail with pairings, "What Goes With This?", Before You Buy scanner |

---

## Code-Only Fixes (No New Designs Needed)

These can be done directly in the real app codebase:

1. ~~Onboarding 6→5 steps:~~ Remove YourLife from onboarding flow, move to Profile
2. Add confetti on "Add Items to Closet" confirm (canvas-confetti library)
3. Add suggestion accuracy badge to Today FullIntel + Useful states
4. Add Power Outfit ⭐ badge to outfit cards (conditional on is_power_outfit)
5. Add "Show Me Another" counter + "Want to pick yourself?" nudge after 3-5 taps
6. Merge/streamline GreatStart + FirstTip post-onboarding flow
7. Enable empty states for Outfits and Closet when count is 0
8. Add notification settings form to Profile → Notifications
