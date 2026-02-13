export interface Profile {
  id: string
  name: string
  email: string | null
  avatar_url: string | null
  gender: string | null
  age_group: string | null
  created_at: string
  updated_at: string
}

export interface StyleProfile {
  id: string
  user_id: string
  height_cm: number | null
  weight_kg: number | null
  body_type: string | null
  body_measurements: Record<string, number> | null
  skin_tone: string | null
  skin_undertone: string | null
  power_colors: string[]
  avoid_colors: string[]
  style_archetypes: string[]
  preferred_fit: string | null
  comfort_level: string | null
  primary_occasions: string[]
  climate: string | null
  budget_range: string | null
  monthly_clothing_budget: number | null
  style_dna: Record<string, unknown> | null
}

export interface WardrobeItem {
  id: string
  user_id: string
  name: string | null
  category: string
  subcategory: string | null
  image_url: string
  thumbnail_url: string | null
  dominant_colors: string[]
  pattern: string | null
  brand: string | null
  size: string | null
  material: string | null
  occasion_tags: string[]
  season_tags: string[]
  formality_level: number | null
  times_worn: number
  last_worn_at: string | null
  purchase_date: string | null
  purchase_price: number | null
  is_favorite: boolean
  is_archived: boolean
  ai_tags: Record<string, unknown> | null
  ai_description: string | null
  created_at: string
}

export interface Outfit {
  id: string
  user_id: string
  name: string | null
  item_ids: string[]
  occasion: string | null
  season: string | null
  style_score: number | null
  color_harmony_score: number | null
  source: 'ai' | 'user_created' | 'community'
  is_favorite: boolean
  times_worn: number
  last_worn_at: string | null
  created_at: string
}

export interface OutfitHistory {
  id: string
  user_id: string
  outfit_id: string | null
  item_ids: string[]
  worn_date: string
  occasion: string | null
  rating: number | null
  feedback: string | null
  weather_conditions: Record<string, unknown> | null
  created_at: string
}

export interface Recommendation {
  id: string
  user_id: string
  type: 'daily_outfit' | 'shopping' | 'style_tip' | 'complete_look'
  title: string | null
  description: string | null
  data: Record<string, unknown>
  occasion: string | null
  reasoning: string | null
  status: 'pending' | 'accepted' | 'rejected' | 'saved'
  created_at: string
}

export interface ShoppingItem {
  id: string
  user_id: string
  category: string
  subcategory: string | null
  description: string | null
  reason: string | null
  min_price: number | null
  max_price: number | null
  product_links: Array<{
    store: string
    url: string
    price: number
    image: string
  }> | null
  priority: 'high' | 'medium' | 'low'
  is_purchased: boolean
  purchased_item_id: string | null
  created_at: string
}

export interface Subscription {
  id: string
  user_id: string
  plan: 'free' | 'pro' | 'premium'
  status: string
  stripe_customer_id: string | null
  stripe_subscription_id: string | null
  current_period_start: string | null
  current_period_end: string | null
  created_at: string
}
