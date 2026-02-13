# ClosetAI - Development Conventions

## Project Overview
ClosetAI is a personal style intelligence platform (PWA) that solves the daily "what do I wear?" problem. It combines a digital closet with AI-powered outfit suggestions, style DNA profiling, and smart shopping recommendations.

## Team
- Amol, Shivali, Suyash - all full-stack contributors

## Tech Stack
- **Frontend:** React 18 + Vite + TypeScript + Tailwind CSS + shadcn/ui (PWA)
- **Backend:** FastAPI (Python 3.10)
- **Database:** Supabase (PostgreSQL + Auth + Storage)
- **AI:** Claude API (vision + styling), OpenAI (embeddings)
- **Deploy:** Vercel (web) + Railway (API) + Supabase Cloud

## Project Structure
```
apps/web/     - React PWA frontend
apps/api/     - FastAPI backend
supabase/     - Database migrations
docs/         - Product, technical, business docs
```

## Development Commands

### Frontend (apps/web/)
```bash
npm install          # Install deps
npm run dev          # Dev server on :3000
npm run build        # Production build
npm run lint         # ESLint
```

### Backend (apps/api/)
```bash
pip install -r requirements.txt                    # Install deps
uvicorn app.main:app --reload                      # Dev server on :8000
ruff check app/                                    # Lint
```

## Coding Conventions

### Frontend
- Use TypeScript strictly (no `any`)
- Components in PascalCase, files match component name
- shadcn/ui for all UI primitives (Button, Card, Input, etc.)
- Zustand for global state, React Query for server state
- Tailwind only — no CSS modules or styled-components
- Import paths use `@/` alias (maps to `src/`)
- Mobile-first design (max-width: 430px container)

### Backend
- FastAPI routers in `app/routers/`, business logic in `app/services/`
- Pydantic models for all request/response schemas
- All endpoints require auth via `Depends(get_current_user_id)`
- Supabase client for DB operations (not raw SQL)
- Use `ruff` for linting

### Database
- All tables have RLS enabled — users can only access their own data
- Migrations in `supabase/migrations/` numbered sequentially
- Use `gen_random_uuid()` for primary keys
- JSONB for flexible/evolving data structures

### Design System
- **Colors:** Rose (#E8A0BF), Cream (#FFF8F5), Charcoal (#2D2D2D), Gold (#C9A96E)
- **Typography:** Playfair Display (headings), Inter (body)
- **Style:** Clean, premium, feminine. Rounded corners, soft shadows, generous whitespace
- Mobile-first PWA (390-430px viewport)

### Git
- Branch naming: `feature/`, `fix/`, `chore/`
- Commit messages: conventional commits (feat:, fix:, chore:, docs:)
- PR required for main branch
