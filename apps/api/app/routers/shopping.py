from fastapi import APIRouter, Depends, HTTPException
from app.utils.auth import get_current_user_id
from app.database import get_supabase
from app.models.recommendation import ShoppingItemResponse

router = APIRouter()


@router.get("/gaps", response_model=list[ShoppingItemResponse])
async def get_wardrobe_gaps(user_id: str = Depends(get_current_user_id)):
    """Get wardrobe gap analysis - what's missing."""
    supabase = get_supabase()
    result = (
        supabase.table("shopping_items")
        .select("*")
        .eq("user_id", user_id)
        .eq("is_purchased", False)
        .order("priority")
        .execute()
    )
    return result.data


@router.get("/wishlist", response_model=list[ShoppingItemResponse])
async def get_wishlist(user_id: str = Depends(get_current_user_id)):
    """Get shopping wishlist."""
    supabase = get_supabase()
    result = (
        supabase.table("shopping_items")
        .select("*")
        .eq("user_id", user_id)
        .eq("is_purchased", False)
        .execute()
    )
    return result.data


@router.post("/{item_id}/purchased")
async def mark_purchased(
    item_id: str,
    wardrobe_item_id: str | None = None,
    user_id: str = Depends(get_current_user_id),
):
    """Mark a shopping item as purchased."""
    supabase = get_supabase()
    updates = {"is_purchased": True}
    if wardrobe_item_id:
        updates["purchased_item_id"] = wardrobe_item_id

    result = (
        supabase.table("shopping_items")
        .update(updates)
        .eq("id", item_id)
        .eq("user_id", user_id)
        .execute()
    )
    if not result.data:
        raise HTTPException(status_code=404, detail="Shopping item not found")
    return {"status": "purchased"}
