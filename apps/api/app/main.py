from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings
from app.routers import auth, profile, wardrobe, outfits, recommendations, shopping

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    docs_url=f"{settings.api_prefix}/docs",
    openapi_url=f"{settings.api_prefix}/openapi.json",
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth.router, prefix=f"{settings.api_prefix}/auth", tags=["auth"])
app.include_router(profile.router, prefix=f"{settings.api_prefix}/profile", tags=["profile"])
app.include_router(wardrobe.router, prefix=f"{settings.api_prefix}/wardrobe", tags=["wardrobe"])
app.include_router(outfits.router, prefix=f"{settings.api_prefix}/outfits", tags=["outfits"])
app.include_router(
    recommendations.router,
    prefix=f"{settings.api_prefix}/recommendations",
    tags=["recommendations"],
)
app.include_router(shopping.router, prefix=f"{settings.api_prefix}/shopping", tags=["shopping"])


@app.get(f"{settings.api_prefix}/health")
async def health_check():
    return {"status": "healthy", "version": "0.1.0"}
