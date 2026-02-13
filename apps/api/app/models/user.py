from pydantic import BaseModel
from typing import Optional


class ProfileCreate(BaseModel):
    name: str
    gender: Optional[str] = None
    age_group: Optional[str] = None


class ProfileUpdate(BaseModel):
    name: Optional[str] = None
    avatar_url: Optional[str] = None
    gender: Optional[str] = None
    age_group: Optional[str] = None


class ProfileResponse(BaseModel):
    id: str
    name: str
    email: Optional[str] = None
    avatar_url: Optional[str] = None
    gender: Optional[str] = None
    age_group: Optional[str] = None


class StyleProfileCreate(BaseModel):
    height_cm: Optional[float] = None
    weight_kg: Optional[float] = None
    body_type: Optional[str] = None
    body_measurements: Optional[dict] = None
    skin_tone: Optional[str] = None
    skin_undertone: Optional[str] = None
    power_colors: list[str] = []
    avoid_colors: list[str] = []
    style_archetypes: list[str] = []
    preferred_fit: Optional[str] = None
    comfort_level: Optional[str] = None
    primary_occasions: list[str] = []
    climate: Optional[str] = None
    budget_range: Optional[str] = None
    monthly_clothing_budget: Optional[float] = None


class StyleProfileResponse(StyleProfileCreate):
    id: str
    user_id: str
    style_dna: Optional[dict] = None
