-- Wardrobe Items
CREATE TABLE wardrobe_items (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES profiles(id) ON DELETE CASCADE,
    name TEXT,
    category TEXT NOT NULL,
    subcategory TEXT,
    image_url TEXT NOT NULL,
    thumbnail_url TEXT,
    dominant_colors TEXT[],
    pattern TEXT,
    brand TEXT,
    size TEXT,
    material TEXT,
    occasion_tags TEXT[],
    season_tags TEXT[],
    formality_level INTEGER,
    times_worn INTEGER DEFAULT 0,
    last_worn_at TIMESTAMPTZ,
    purchase_date DATE,
    purchase_price NUMERIC,
    is_favorite BOOLEAN DEFAULT FALSE,
    is_archived BOOLEAN DEFAULT FALSE,
    ai_tags JSONB,
    ai_description TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_wardrobe_user ON wardrobe_items(user_id);
CREATE INDEX idx_wardrobe_category ON wardrobe_items(user_id, category);
CREATE INDEX idx_wardrobe_tags ON wardrobe_items USING GIN (occasion_tags);
CREATE INDEX idx_wardrobe_ai ON wardrobe_items USING GIN (ai_tags);

-- RLS
ALTER TABLE wardrobe_items ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can view their own items"
    ON wardrobe_items FOR SELECT
    USING (auth.uid() = user_id);

CREATE POLICY "Users can insert their own items"
    ON wardrobe_items FOR INSERT
    WITH CHECK (auth.uid() = user_id);

CREATE POLICY "Users can update their own items"
    ON wardrobe_items FOR UPDATE
    USING (auth.uid() = user_id);

CREATE POLICY "Users can delete their own items"
    ON wardrobe_items FOR DELETE
    USING (auth.uid() = user_id);

-- Helper function to increment times_worn
CREATE OR REPLACE FUNCTION increment_times_worn(item_id UUID)
RETURNS VOID AS $$
BEGIN
    UPDATE wardrobe_items
    SET times_worn = times_worn + 1,
        last_worn_at = NOW()
    WHERE id = item_id;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;
