from fastapi import APIRouter, Depends, HTTPException
from app.utils.auth import get_current_user_id
from app.database import get_supabase
from app.models.outfit import (
    OutfitCreate,
    OutfitResponse,
    OutfitHistoryCreate,
    OutfitHistoryResponse,
)

router = APIRouter()


@router.get("/", response_model=list[OutfitResponse])
async def list_outfits(user_id: str = Depends(get_current_user_id)):
    """List all saved outfits."""
    supabase = get_supabase()
    result = (
        supabase.table("outfits")
        .select("*")
        .eq("user_id", user_id)
        .order("created_at", desc=True)
        .execute()
    )
    return result.data


@router.post("/", response_model=OutfitResponse)
async def create_outfit(
    data: OutfitCreate, user_id: str = Depends(get_current_user_id)
):
    """Create a new outfit combination."""
    supabase = get_supabase()
    result = (
        supabase.table("outfits")
        .insert({"user_id": user_id, **data.model_dump()})
        .execute()
    )
    return result.data[0]


@router.get("/{outfit_id}", response_model=OutfitResponse)
async def get_outfit(outfit_id: str, user_id: str = Depends(get_current_user_id)):
    """Get a single outfit."""
    supabase = get_supabase()
    result = (
        supabase.table("outfits")
        .select("*")
        .eq("id", outfit_id)
        .eq("user_id", user_id)
        .single()
        .execute()
    )
    if not result.data:
        raise HTTPException(status_code=404, detail="Outfit not found")
    return result.data


@router.delete("/{outfit_id}")
async def delete_outfit(outfit_id: str, user_id: str = Depends(get_current_user_id)):
    """Delete an outfit."""
    supabase = get_supabase()
    supabase.table("outfits").delete().eq("id", outfit_id).eq("user_id", user_id).execute()
    return {"status": "deleted"}


@router.post("/history", response_model=OutfitHistoryResponse)
async def log_outfit_worn(
    data: OutfitHistoryCreate, user_id: str = Depends(get_current_user_id)
):
    """Log that an outfit was worn."""
    supabase = get_supabase()
    result = (
        supabase.table("outfit_history")
        .insert({"user_id": user_id, **data.model_dump(exclude_unset=True)})
        .execute()
    )

    # Update times_worn on individual items
    for item_id in data.item_ids:
        supabase.rpc(
            "increment_times_worn", {"item_id": item_id}
        ).execute()

    return result.data[0]


@router.get("/history/", response_model=list[OutfitHistoryResponse])
async def get_outfit_history(
    limit: int = 30,
    user_id: str = Depends(get_current_user_id),
):
    """Get outfit wearing history."""
    supabase = get_supabase()
    result = (
        supabase.table("outfit_history")
        .select("*")
        .eq("user_id", user_id)
        .order("worn_date", desc=True)
        .limit(limit)
        .execute()
    )
    return result.data
