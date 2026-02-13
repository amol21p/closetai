from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime


class OutfitCreate(BaseModel):
    name: Optional[str] = None
    item_ids: list[str]
    occasion: Optional[str] = None
    season: Optional[str] = None
    source: str = "user_created"


class OutfitResponse(BaseModel):
    id: str
    user_id: str
    name: Optional[str] = None
    item_ids: list[str]
    occasion: Optional[str] = None
    season: Optional[str] = None
    style_score: Optional[float] = None
    color_harmony_score: Optional[float] = None
    source: str
    is_favorite: bool = False
    times_worn: int = 0
    last_worn_at: Optional[datetime] = None
    created_at: datetime


class OutfitHistoryCreate(BaseModel):
    outfit_id: Optional[str] = None
    item_ids: list[str]
    worn_date: date
    occasion: Optional[str] = None
    rating: Optional[int] = None
    feedback: Optional[str] = None


class OutfitHistoryResponse(BaseModel):
    id: str
    user_id: str
    outfit_id: Optional[str] = None
    item_ids: list[str]
    worn_date: date
    occasion: Optional[str] = None
    rating: Optional[int] = None
    feedback: Optional[str] = None
    weather_conditions: Optional[dict] = None
    created_at: datetime
