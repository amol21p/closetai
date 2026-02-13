from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class RecommendationResponse(BaseModel):
    id: str
    user_id: str
    type: str
    title: Optional[str] = None
    description: Optional[str] = None
    data: dict
    occasion: Optional[str] = None
    reasoning: Optional[str] = None
    status: str = "pending"
    created_at: datetime


class RecommendationFeedback(BaseModel):
    status: str  # accepted, rejected, saved


class ShoppingItemResponse(BaseModel):
    id: str
    user_id: str
    category: str
    subcategory: Optional[str] = None
    description: Optional[str] = None
    reason: Optional[str] = None
    min_price: Optional[float] = None
    max_price: Optional[float] = None
    product_links: Optional[list[dict]] = None
    priority: str = "medium"
    is_purchased: bool = False
    purchased_item_id: Optional[str] = None
    created_at: datetime
