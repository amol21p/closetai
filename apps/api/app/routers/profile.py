from fastapi import APIRouter, Depends, HTTPException
from app.utils.auth import get_current_user_id
from app.database import get_supabase
from app.models.user import (
    ProfileCreate,
    ProfileUpdate,
    ProfileResponse,
    StyleProfileCreate,
    StyleProfileResponse,
)

router = APIRouter()


@router.get("/", response_model=ProfileResponse)
async def get_profile(user_id: str = Depends(get_current_user_id)):
    """Get user profile."""
    supabase = get_supabase()
    result = supabase.table("profiles").select("*").eq("id", user_id).single().execute()
    if not result.data:
        raise HTTPException(status_code=404, detail="Profile not found")
    return result.data


@router.post("/", response_model=ProfileResponse)
async def create_profile(
    data: ProfileCreate, user_id: str = Depends(get_current_user_id)
):
    """Create user profile (called after signup)."""
    supabase = get_supabase()
    result = (
        supabase.table("profiles")
        .insert({"id": user_id, **data.model_dump()})
        .execute()
    )
    return result.data[0]


@router.patch("/", response_model=ProfileResponse)
async def update_profile(
    data: ProfileUpdate, user_id: str = Depends(get_current_user_id)
):
    """Update user profile."""
    supabase = get_supabase()
    updates = data.model_dump(exclude_unset=True)
    result = (
        supabase.table("profiles").update(updates).eq("id", user_id).execute()
    )
    if not result.data:
        raise HTTPException(status_code=404, detail="Profile not found")
    return result.data[0]


@router.get("/style", response_model=StyleProfileResponse)
async def get_style_profile(user_id: str = Depends(get_current_user_id)):
    """Get user's style profile."""
    supabase = get_supabase()
    result = (
        supabase.table("style_profiles")
        .select("*")
        .eq("user_id", user_id)
        .single()
        .execute()
    )
    if not result.data:
        raise HTTPException(status_code=404, detail="Style profile not found")
    return result.data


@router.post("/style", response_model=StyleProfileResponse)
async def create_style_profile(
    data: StyleProfileCreate, user_id: str = Depends(get_current_user_id)
):
    """Create or update style profile."""
    supabase = get_supabase()
    result = (
        supabase.table("style_profiles")
        .upsert({"user_id": user_id, **data.model_dump()})
        .execute()
    )
    return result.data[0]
