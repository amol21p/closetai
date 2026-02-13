-- AI Recommendations
CREATE TABLE recommendations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES profiles(id) ON DELETE CASCADE,
    type TEXT NOT NULL,
    title TEXT,
    description TEXT,
    data JSONB NOT NULL,
    occasion TEXT,
    reasoning TEXT,
    status TEXT DEFAULT 'pending',
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_recommendations_user ON recommendations(user_id, type, status);

ALTER TABLE recommendations ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can view their own recommendations"
    ON recommendations FOR SELECT
    USING (auth.uid() = user_id);

CREATE POLICY "Users can update their own recommendations"
    ON recommendations FOR UPDATE
    USING (auth.uid() = user_id);

-- Shopping Wishlist & Recommendations
CREATE TABLE shopping_items (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES profiles(id) ON DELETE CASCADE,
    category TEXT NOT NULL,
    subcategory TEXT,
    description TEXT,
    reason TEXT,
    min_price NUMERIC,
    max_price NUMERIC,
    product_links JSONB,
    priority TEXT DEFAULT 'medium',
    is_purchased BOOLEAN DEFAULT FALSE,
    purchased_item_id UUID REFERENCES wardrobe_items(id) ON DELETE SET NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

ALTER TABLE shopping_items ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can view their own shopping items"
    ON shopping_items FOR SELECT
    USING (auth.uid() = user_id);

CREATE POLICY "Users can insert their own shopping items"
    ON shopping_items FOR INSERT
    WITH CHECK (auth.uid() = user_id);

CREATE POLICY "Users can update their own shopping items"
    ON shopping_items FOR UPDATE
    USING (auth.uid() = user_id);

CREATE POLICY "Users can delete their own shopping items"
    ON shopping_items FOR DELETE
    USING (auth.uid() = user_id);
