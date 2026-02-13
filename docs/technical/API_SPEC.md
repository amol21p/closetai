# ClosetAI - API Specification

Base URL: `https://api.closetai.app/api` (production) / `http://localhost:8000/api` (local)

All endpoints require authentication via Bearer token (Supabase JWT) unless noted.

---

## Health Check

### `GET /api/health`
No auth required.

**Response:**
```json
{
  "status": "healthy",
  "version": "0.1.0"
}
```

---

## Auth

### `GET /api/auth/me`
Get current authenticated user's ID.

**Response:**
```json
{
  "user_id": "uuid-string"
}
```

---

## Profile

### `GET /api/profile/`
Get user profile.

**Response:**
```json
{
  "id": "uuid",
  "name": "Priya Sharma",
  "email": "priya@example.com",
  "avatar_url": "https://...",
  "gender": "female",
  "age_group": "25-34"
}
```

### `POST /api/profile/`
Create user profile (called after signup if auto-creation trigger fails).

**Body:**
```json
{
  "name": "Priya Sharma",
  "gender": "female",
  "age_group": "25-34"
}
```

### `PATCH /api/profile/`
Update user profile. Only send fields being updated.

**Body:**
```json
{
  "name": "Priya S.",
  "avatar_url": "https://..."
}
```

### `GET /api/profile/style`
Get user's Style DNA profile.

**Response:**
```json
{
  "id": "uuid",
  "user_id": "uuid",
  "height_cm": 165,
  "weight_kg": 58,
  "body_type": "hourglass",
  "skin_tone": "medium",
  "skin_undertone": "warm",
  "power_colors": ["navy", "emerald", "cream", "coral", "gold"],
  "avoid_colors": ["neon green", "orange"],
  "style_archetypes": ["classic_minimalist", "modern_elegant"],
  "preferred_fit": "regular",
  "comfort_level": "moderate",
  "primary_occasions": ["office", "casual", "date-night", "ethnic"],
  "climate": "tropical",
  "budget_range": "mid-range",
  "monthly_clothing_budget": 5000,
  "style_dna": {
    "color_palette": ["navy", "white", "black", "beige"],
    "category_balance": {"top": 18, "bottom": 8, "dress": 5},
    "formality_avg": 2.8,
    "formality_label": "balanced",
    "wardrobe_utilization": 72.3,
    "never_worn_count": 8,
    "gaps": ["Only 2 outerwear pieces"]
  }
}
```

### `POST /api/profile/style`
Create or update style profile (upsert).

**Body:**
```json
{
  "height_cm": 165,
  "weight_kg": 58,
  "body_type": "hourglass",
  "skin_tone": "medium",
  "skin_undertone": "warm",
  "power_colors": ["navy", "emerald", "cream"],
  "style_archetypes": ["classic_minimalist"],
  "primary_occasions": ["office", "casual"],
  "climate": "tropical",
  "budget_range": "mid-range",
  "monthly_clothing_budget": 5000
}
```

---

## Wardrobe

### `GET /api/wardrobe/`
List all wardrobe items (non-archived).

**Query params:**
- `category` (optional): Filter by category (top, bottom, dress, etc.)

**Response:** Array of wardrobe items.
```json
[
  {
    "id": "uuid",
    "user_id": "uuid",
    "name": "Blue Oxford Shirt",
    "category": "top",
    "subcategory": "shirt",
    "image_url": "https://supabase.storage/.../shirt.jpg",
    "thumbnail_url": "https://...",
    "dominant_colors": ["blue", "white"],
    "pattern": "solid",
    "brand": "Uniqlo",
    "size": "M",
    "material": "cotton",
    "occasion_tags": ["office", "casual"],
    "season_tags": ["all-season"],
    "formality_level": 3,
    "times_worn": 12,
    "last_worn_at": "2024-01-15T10:00:00Z",
    "purchase_date": "2023-06-01",
    "purchase_price": 1999,
    "is_favorite": true,
    "is_archived": false,
    "ai_tags": {"style": "classic", "fit": "regular"},
    "ai_description": "Classic blue oxford button-down shirt in regular fit cotton",
    "created_at": "2024-01-01T00:00:00Z"
  }
]
```

### `POST /api/wardrobe/`
Add a new wardrobe item.

**Body:**
```json
{
  "name": "Blue Oxford Shirt",
  "category": "top",
  "subcategory": "shirt",
  "image_url": "https://supabase.storage/.../shirt.jpg",
  "dominant_colors": ["blue", "white"],
  "pattern": "solid",
  "brand": "Uniqlo",
  "occasion_tags": ["office", "casual"],
  "season_tags": ["all-season"],
  "formality_level": 3
}
```

### `GET /api/wardrobe/{item_id}`
Get a single wardrobe item.

### `PATCH /api/wardrobe/{item_id}`
Update a wardrobe item. Only send fields being updated.

**Body:**
```json
{
  "name": "Navy Oxford Shirt",
  "occasion_tags": ["office", "casual", "date-night"],
  "is_favorite": true
}
```

### `DELETE /api/wardrobe/{item_id}`
Archive a wardrobe item (soft delete).

**Response:**
```json
{"status": "archived"}
```

### `POST /api/wardrobe/upload`
Upload an item image to storage.

**Body:** `multipart/form-data` with `file` field.

**Response:**
```json
{
  "image_url": "https://supabase.storage/.../uploaded-image.jpg"
}
```

---

## Outfits

### `GET /api/outfits/`
List all saved outfits.

**Response:**
```json
[
  {
    "id": "uuid",
    "user_id": "uuid",
    "name": "Monday Office Look",
    "item_ids": ["item-uuid-1", "item-uuid-2", "item-uuid-3"],
    "occasion": "office",
    "season": "all-season",
    "style_score": 87.5,
    "color_harmony_score": 92.0,
    "source": "ai",
    "is_favorite": true,
    "times_worn": 3,
    "last_worn_at": "2024-01-15T10:00:00Z",
    "created_at": "2024-01-01T00:00:00Z"
  }
]
```

### `POST /api/outfits/`
Create a new outfit.

**Body:**
```json
{
  "name": "Casual Friday",
  "item_ids": ["uuid-1", "uuid-2", "uuid-3"],
  "occasion": "casual",
  "season": "summer",
  "source": "user_created"
}
```

### `GET /api/outfits/{outfit_id}`
Get a single outfit.

### `DELETE /api/outfits/{outfit_id}`
Delete an outfit.

### `POST /api/outfits/history`
Log that an outfit was worn. Also increments `times_worn` on each item.

**Body:**
```json
{
  "outfit_id": "uuid",
  "item_ids": ["uuid-1", "uuid-2", "uuid-3"],
  "worn_date": "2024-01-15",
  "occasion": "office",
  "rating": 4,
  "feedback": "Felt great, got compliments"
}
```

### `GET /api/outfits/history/?limit=30`
Get outfit wearing history.

---

## Recommendations

### `GET /api/recommendations/daily`
Get today's outfit recommendations (up to 5).

**Response:** Array of recommendation objects with outfit data in `data` field.
```json
[
  {
    "id": "uuid",
    "user_id": "uuid",
    "type": "daily_outfit",
    "title": "Smart Casual Monday",
    "description": "A polished look for your office day",
    "data": {
      "item_ids": ["uuid-1", "uuid-2", "uuid-3"],
      "style_score": 87,
      "color_harmony": "complementary"
    },
    "occasion": "office",
    "reasoning": "Navy shirt + beige chinos is a classic office combo. Weather is 28°C so cotton is ideal. You haven't worn this shirt in 2 weeks.",
    "status": "pending",
    "created_at": "2024-01-15T06:00:00Z"
  }
]
```

### `GET /api/recommendations/tips`
Get style tips (up to 10).

### `POST /api/recommendations/{rec_id}/feedback`
Submit feedback on a recommendation.

**Body:**
```json
{
  "status": "accepted"
}
```
Valid values: `accepted`, `rejected`, `saved`

---

## Shopping

### `GET /api/shopping/gaps`
Get wardrobe gap analysis.

**Response:**
```json
[
  {
    "id": "uuid",
    "user_id": "uuid",
    "category": "bottom",
    "subcategory": "chinos",
    "description": "A pair of beige chinos would unlock 8 new outfit combinations",
    "reason": "You have 18 tops but only 4 bottoms",
    "min_price": 1500,
    "max_price": 3500,
    "product_links": [
      {
        "store": "Myntra",
        "url": "https://myntra.com/...",
        "price": 1999,
        "image": "https://..."
      }
    ],
    "priority": "high",
    "is_purchased": false,
    "purchased_item_id": null,
    "created_at": "2024-01-15T00:00:00Z"
  }
]
```

### `GET /api/shopping/wishlist`
Get shopping wishlist (all unpurchased items).

### `POST /api/shopping/{item_id}/purchased`
Mark a shopping item as purchased.

**Query params:**
- `wardrobe_item_id` (optional): Link to the newly added wardrobe item.

---

## Error Responses

All errors follow this format:
```json
{
  "detail": "Human-readable error message"
}
```

| Status Code | Meaning |
|-------------|---------|
| 400 | Bad request (validation error) |
| 401 | Unauthorized (missing/invalid token) |
| 404 | Resource not found |
| 422 | Unprocessable entity (Pydantic validation) |
| 500 | Internal server error |
