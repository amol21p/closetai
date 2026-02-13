from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from app.utils.auth import get_current_user_id
from app.database import get_supabase
from app.models.wardrobe import (
    WardrobeItemCreate,
    WardrobeItemUpdate,
    WardrobeItemResponse,
)

router = APIRouter()


@router.get("/", response_model=list[WardrobeItemResponse])
async def list_items(
    category: str | None = None,
    user_id: str = Depends(get_current_user_id),
):
    """List wardrobe items, optionally filtered by category."""
    supabase = get_supabase()
    query = (
        supabase.table("wardrobe_items")
        .select("*")
        .eq("user_id", user_id)
        .eq("is_archived", False)
        .order("created_at", desc=True)
    )
    if category:
        query = query.eq("category", category)
    result = query.execute()
    return result.data


@router.post("/", response_model=WardrobeItemResponse)
async def create_item(
    data: WardrobeItemCreate, user_id: str = Depends(get_current_user_id)
):
    """Add a new wardrobe item."""
    supabase = get_supabase()
    result = (
        supabase.table("wardrobe_items")
        .insert({"user_id": user_id, **data.model_dump(exclude_unset=True)})
        .execute()
    )
    return result.data[0]


@router.get("/{item_id}", response_model=WardrobeItemResponse)
async def get_item(item_id: str, user_id: str = Depends(get_current_user_id)):
    """Get a single wardrobe item."""
    supabase = get_supabase()
    result = (
        supabase.table("wardrobe_items")
        .select("*")
        .eq("id", item_id)
        .eq("user_id", user_id)
        .single()
        .execute()
    )
    if not result.data:
        raise HTTPException(status_code=404, detail="Item not found")
    return result.data


@router.patch("/{item_id}", response_model=WardrobeItemResponse)
async def update_item(
    item_id: str,
    data: WardrobeItemUpdate,
    user_id: str = Depends(get_current_user_id),
):
    """Update a wardrobe item."""
    supabase = get_supabase()
    updates = data.model_dump(exclude_unset=True)
    result = (
        supabase.table("wardrobe_items")
        .update(updates)
        .eq("id", item_id)
        .eq("user_id", user_id)
        .execute()
    )
    if not result.data:
        raise HTTPException(status_code=404, detail="Item not found")
    return result.data[0]


@router.delete("/{item_id}")
async def delete_item(item_id: str, user_id: str = Depends(get_current_user_id)):
    """Archive a wardrobe item (soft delete)."""
    supabase = get_supabase()
    result = (
        supabase.table("wardrobe_items")
        .update({"is_archived": True})
        .eq("id", item_id)
        .eq("user_id", user_id)
        .execute()
    )
    if not result.data:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"status": "archived"}


@router.post("/upload")
async def upload_item_image(
    file: UploadFile = File(...),
    user_id: str = Depends(get_current_user_id),
):
    """Upload an item image to Supabase Storage and return the URL."""
    supabase = get_supabase()
    contents = await file.read()
    file_path = f"{user_id}/{file.filename}"

    supabase.storage.from_("wardrobe-images").upload(
        file_path, contents, {"content-type": file.content_type or "image/jpeg"}
    )

    url = supabase.storage.from_("wardrobe-images").get_public_url(file_path)
    return {"image_url": url}
