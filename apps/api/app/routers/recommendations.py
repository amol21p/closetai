from fastapi import APIRouter, Depends, HTTPException
from app.utils.auth import get_current_user_id
from app.database import get_supabase
from app.models.recommendation import RecommendationResponse, RecommendationFeedback

router = APIRouter()


@router.get("/daily", response_model=list[RecommendationResponse])
async def get_daily_outfits(user_id: str = Depends(get_current_user_id)):
    """Get today's outfit recommendations."""
    supabase = get_supabase()
    result = (
        supabase.table("recommendations")
        .select("*")
        .eq("user_id", user_id)
        .eq("type", "daily_outfit")
        .eq("status", "pending")
        .order("created_at", desc=True)
        .limit(5)
        .execute()
    )
    return result.data


@router.get("/tips", response_model=list[RecommendationResponse])
async def get_style_tips(user_id: str = Depends(get_current_user_id)):
    """Get style tips."""
    supabase = get_supabase()
    result = (
        supabase.table("recommendations")
        .select("*")
        .eq("user_id", user_id)
        .eq("type", "style_tip")
        .order("created_at", desc=True)
        .limit(10)
        .execute()
    )
    return result.data


@router.post("/{rec_id}/feedback")
async def submit_feedback(
    rec_id: str,
    data: RecommendationFeedback,
    user_id: str = Depends(get_current_user_id),
):
    """Submit feedback on a recommendation (accept/reject/save)."""
    if data.status not in ("accepted", "rejected", "saved"):
        raise HTTPException(status_code=400, detail="Invalid status")

    supabase = get_supabase()
    result = (
        supabase.table("recommendations")
        .update({"status": data.status})
        .eq("id", rec_id)
        .eq("user_id", user_id)
        .execute()
    )
    if not result.data:
        raise HTTPException(status_code=404, detail="Recommendation not found")
    return {"status": "updated"}
