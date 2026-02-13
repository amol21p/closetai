from fastapi import APIRouter, Depends
from app.utils.auth import get_current_user_id

router = APIRouter()


@router.get("/me")
async def get_current_user(user_id: str = Depends(get_current_user_id)):
    """Get the current authenticated user's ID."""
    return {"user_id": user_id}
