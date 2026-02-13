from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime


class WardrobeItemCreate(BaseModel):
    name: Optional[str] = None
    category: str
    subcategory: Optional[str] = None
    image_url: str
    thumbnail_url: Optional[str] = None
    dominant_colors: list[str] = []
    pattern: Optional[str] = None
    brand: Optional[str] = None
    size: Optional[str] = None
    material: Optional[str] = None
    occasion_tags: list[str] = []
    season_tags: list[str] = []
    formality_level: Optional[int] = None
    purchase_date: Optional[date] = None
    purchase_price: Optional[float] = None


class WardrobeItemUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    subcategory: Optional[str] = None
    dominant_colors: Optional[list[str]] = None
    pattern: Optional[str] = None
    brand: Optional[str] = None
    size: Optional[str] = None
    material: Optional[str] = None
    occasion_tags: Optional[list[str]] = None
    season_tags: Optional[list[str]] = None
    formality_level: Optional[int] = None
    is_favorite: Optional[bool] = None
    is_archived: Optional[bool] = None
    purchase_date: Optional[date] = None
    purchase_price: Optional[float] = None


class WardrobeItemResponse(BaseModel):
    id: str
    user_id: str
    name: Optional[str] = None
    category: str
    subcategory: Optional[str] = None
    image_url: str
    thumbnail_url: Optional[str] = None
    dominant_colors: list[str] = []
    pattern: Optional[str] = None
    brand: Optional[str] = None
    size: Optional[str] = None
    material: Optional[str] = None
    occasion_tags: list[str] = []
    season_tags: list[str] = []
    formality_level: Optional[int] = None
    times_worn: int = 0
    last_worn_at: Optional[datetime] = None
    purchase_date: Optional[date] = None
    purchase_price: Optional[float] = None
    is_favorite: bool = False
    is_archived: bool = False
    ai_tags: Optional[dict] = None
    ai_description: Optional[str] = None
    created_at: datetime


class AITaggingResponse(BaseModel):
    category: str
    subcategory: Optional[str] = None
    dominant_colors: list[str]
    pattern: Optional[str] = None
    material: Optional[str] = None
    formality_level: int
    occasion_tags: list[str]
    season_tags: list[str]
    description: str
