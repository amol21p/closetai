# ClosetAI - Technical Architecture

## System Overview

```
┌──────────────┐     ┌──────────────┐     ┌──────────────────────┐
│              │     │              │     │     Supabase Cloud    │
│   React PWA  │────▶│   FastAPI    │────▶│  ┌────────────────┐  │
│   (Vercel)   │     │  (Railway)   │     │  │  PostgreSQL DB  │  │
│              │     │              │     │  ├────────────────┤  │
│  Tailwind +  │     │  Python 3.10 │     │  │   Auth (GoTrue) │  │
│  shadcn/ui   │     │              │     │  ├────────────────┤  │
│              │◀───▶│              │     │  │  Storage (S3)   │  │
└──────┬───────┘     └──────┬───────┘     │  ├────────────────┤  │
       │                    │             │  │  Edge Functions  │  │
       │                    │             │  └────────────────┘  │
       │              ┌─────┴─────┐       └──────────────────────┘
       │              │           │
       │        ┌─────┴───┐ ┌────┴────┐
       │        │ Claude   │ │ OpenAI  │
       │        │ API      │ │ API     │
       │        │ (Vision+ │ │ (Embed- │
       │        │  Chat)   │ │  dings) │
       │        └─────────┘ └─────────┘
       │
  ┌────┴─────┐
  │ OpenWea- │
  │ therMap   │
  │ API      │
  └──────────┘
```

## Stack Decisions & Rationale

### Frontend: React PWA (not Flutter, not React Native)

**Choice:** React 18 + Vite + TypeScript + Tailwind CSS + shadcn/ui

**Why PWA first:**
- No app store approval needed — ship instantly, iterate daily
- Camera/photo access works in modern mobile browsers
- "Add to Home Screen" gives near-native experience
- Faster iteration than Flutter/RN for web-first features
- Can add Flutter mobile app in v2 when we need native camera/AR
- Lower barrier to entry for users (no download)

**Why Vite over Next.js:**
- Pure client-side app — no SSR needed for a personal utility app
- Simpler deployment (static files on Vercel)
- Faster dev server and HMR
- PWA plugin (vite-plugin-pwa) works seamlessly

**Why shadcn/ui over Material/Ant/Chakra:**
- Copy-paste components = full control over styling
- Built on Radix primitives = accessible by default
- Tailwind-native = consistent with our design system
- No heavy bundle from component library

**Why Zustand over Redux/Context:**
- Minimal boilerplate, TypeScript-first
- No providers needed
- Simple for auth + wardrobe state
- React Query can be added later for server state caching

### Backend: FastAPI (not Express, not Spring Boot)

**Choice:** Single Python FastAPI backend

**Why Python:**
- AI/ML integration is native (Anthropic SDK, OpenAI SDK, Pillow)
- FastAPI is as fast as Node.js for I/O-bound work (async)
- Pydantic models = automatic validation + OpenAPI docs
- Team already knows it well (kumbh-app)

**Why not Java/Spring Boot:**
- Enterprise patterns are overkill for a startup MVP
- Python is 3-5x faster to develop in for this use case
- ML libraries are all Python-first
- One language for backend + AI = simpler hiring + debugging

**Why single backend (not microservices):**
- Startup stage: speed of iteration > architectural purity
- All services share the same DB and auth
- Can extract microservices later when we know what scales independently
- Monolith is fine up to ~100K users with proper async design

### Database: Supabase (not raw PostgreSQL + Firebase + S3)

**Choice:** Supabase Cloud (PostgreSQL + Auth + Storage + Edge Functions + Realtime)

**Why Supabase:**
- One platform replaces 4 separate services
- PostgreSQL = relational + JSONB (best of both worlds)
- Auth with OAuth providers built-in (Google, Apple)
- Storage is S3-compatible (wardrobe images)
- Row-Level Security = security baked into DB layer
- Real-time subscriptions for future collab features
- Team knows it deeply (food-life)

**Why not MongoDB:**
- Our data IS relational (users → items → outfits → history)
- PostgreSQL JSONB handles the flexible fields (ai_tags, style_dna)
- We need JOINs for outfit queries ("items in this outfit")
- RLS doesn't exist in MongoDB

### AI: Claude + OpenAI

**Claude API (primary):**
- Vision: clothing item recognition from photos
- Chat: outfit suggestions, styling advice, style tips
- Structured output: consistent JSON responses for item tagging

**OpenAI (secondary, future):**
- Embeddings: style similarity matching between items
- Search: "find items similar to this" using vector similarity

**Why Claude over GPT-4V for vision:**
- Superior at structured data extraction from images
- Better at following JSON schemas consistently
- More nuanced color and pattern description
- Can switch/combine models easily via service abstraction

---

## Data Flow

### 1. Image Upload & AI Tagging

```
User captures photo
    → Frontend compresses (client-side, <2MB)
    → POST /api/wardrobe/upload (multipart)
    → FastAPI receives image bytes
    → Upload to Supabase Storage (wardrobe-images/{user_id}/{filename})
    → Get public URL
    → Convert to base64
    → Send to Claude Vision API with structured prompt
    → Receive JSON: {category, colors, pattern, formality, occasions, seasons}
    → Create wardrobe_item row in DB with AI tags
    → Return complete item to frontend
    → User confirms/adjusts tags
    → PATCH /api/wardrobe/{id} with corrections
```

### 2. Daily Outfit Generation

```
User opens Home tab (or morning notification)
    → GET /api/recommendations/daily
    → FastAPI checks for existing today's recommendations
    → If none, generates new:
        1. Fetch user's wardrobe items (all active, non-archived)
        2. Fetch style profile (Style DNA, preferences)
        3. Fetch weather (OpenWeatherMap for user's location)
        4. Fetch outfit history (last 14 days)
        5. Run outfit_engine.generate_outfit_candidates()
           - Filter by weather/season
           - Generate top+bottom and dress combos
           - Score by color harmony, formality match, freshness
        6. Optionally: Send top candidates to Claude for ranking/reasoning
        7. Save as recommendation rows (type='daily_outfit')
    → Return top 3-5 outfit recommendations
    → Frontend displays with swipe navigation
```

### 3. Authentication Flow

```
User clicks "Continue with Google"
    → Supabase Auth handles OAuth flow
    → Redirect to Google consent screen
    → Google redirects back with code
    → Supabase exchanges code for tokens
    → Creates auth.users row + triggers handle_new_user()
    → handle_new_user() creates profiles row
    → on_profile_created trigger creates free subscription
    → Frontend receives session (JWT)
    → All subsequent API calls include JWT in Authorization header
    → FastAPI extracts user_id from JWT via get_current_user_id()
```

---

## Security Architecture

### Authentication
- Supabase Auth (GoTrue) manages all auth
- JWT tokens with 1-hour expiry, refresh tokens for re-auth
- OAuth providers: Google, Apple (no password storage for OAuth users)
- Email/password with bcrypt hashing (handled by Supabase)

### Authorization
- **Row-Level Security (RLS)** on every table
- Every row has `user_id` — policies enforce `auth.uid() = user_id`
- FastAPI endpoints additionally validate `user_id` from JWT
- Double protection: even if RLS bypassed, API enforces ownership

### Data Privacy
- Images stored in user-scoped paths: `wardrobe-images/{user_id}/`
- No body photos required (body measurements are optional numeric inputs)
- AI analysis is stateless — images sent to Claude are not stored by Anthropic
- GDPR-ready: user can delete all data (CASCADE deletes handle this)

### API Security
- CORS restricted to known origins
- Rate limiting (to be added via middleware)
- File upload size limits (10MB max)
- Input validation via Pydantic models on all endpoints

---

## Infrastructure & Deployment

### Frontend (Vercel)
```
GitHub push to main
    → Vercel auto-builds (npm run build)
    → Deploys to Vercel CDN
    → PWA service worker updated
    → Users get new version on next visit (autoUpdate)
```

### Backend (Railway)
```
GitHub push to main
    → Railway builds from Dockerfile
    → Zero-downtime deployment
    → Environment variables managed in Railway dashboard
    → Health check: GET /api/health
```

### Database (Supabase Cloud)
- Managed PostgreSQL (no maintenance)
- Automatic backups
- Migrations managed manually via SQL files (applied via dashboard or CLI)
- Connection pooling via Supabase's built-in pooler

### Monitoring (Future)
- Sentry for error tracking (frontend + backend)
- Supabase dashboard for DB metrics
- Railway dashboard for API metrics
- Custom analytics events (Mixpanel or PostHog)

---

## Scaling Considerations

### Current Architecture Limits
- Single FastAPI instance handles ~1000 concurrent users easily
- Supabase free tier: 500MB DB, 1GB Storage, 50K monthly active users
- Claude API: rate limits based on tier

### When to Scale
| Signal | Action |
|--------|--------|
| API response > 500ms p95 | Add Railway instance (horizontal scale) |
| DB size > 500MB | Upgrade Supabase plan ($25/mo) |
| Storage > 1GB | Upgrade Supabase plan |
| Claude API rate limits hit | Add request queuing, batch processing |
| 10K+ users | Add Redis for caching outfit-of-the-day |
| 50K+ users | Consider extracting AI service as separate microservice |
| 100K+ users | Consider Flutter native app for camera/AR features |

### Performance Optimization Plan
1. **Image compression on client** — reduce upload size before hitting API
2. **Thumbnail generation** — serve small images in grid views
3. **Outfit caching** — daily outfits computed once per day, cached
4. **Lazy loading** — wardrobe grid uses intersection observer
5. **PWA offline** — service worker caches app shell + recent data
6. **CDN for images** — Supabase Storage serves via CDN
