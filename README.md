# ClosetAI

**Your closet, but smarter.**

AI-powered personal style intelligence platform that knows your wardrobe, your body, and your life.

## What It Does

- **Digital Closet** - Photograph your wardrobe, AI auto-tags everything
- **Daily Outfits** - Get personalized outfit suggestions based on weather, calendar, and your style
- **Style DNA** - Evolving style profile that learns your preferences
- **Smart Shopping** - Know what's missing, avoid duplicate purchases, unlock new outfits

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React 18 + Vite + TypeScript + Tailwind + shadcn/ui (PWA) |
| Backend | FastAPI (Python) |
| Database | Supabase (PostgreSQL + Auth + Storage) |
| AI | Claude API (vision + styling) |
| Deploy | Vercel + Railway + Supabase Cloud |

## Getting Started

### Prerequisites
- Node.js 18+
- Python 3.10+
- Supabase account

### Frontend
```bash
cd apps/web
cp .env.example .env    # Fill in Supabase credentials
npm install
npm run dev             # http://localhost:3000
```

### Backend
```bash
cd apps/api
cp .env.example .env    # Fill in all API keys
pip install -r requirements.txt
uvicorn app.main:app --reload   # http://localhost:8000/api/docs
```

### Database
1. Create a Supabase project at [supabase.com](https://supabase.com)
2. Run migrations in order from `supabase/migrations/`
3. Enable Google OAuth in Supabase Auth settings
4. Create a `wardrobe-images` storage bucket (public)

## Project Structure

```
closetai/
├── apps/
│   ├── web/          # React PWA
│   └── api/          # FastAPI backend
├── supabase/         # Database migrations
├── docs/             # Documentation
└── .github/          # CI/CD workflows
```
