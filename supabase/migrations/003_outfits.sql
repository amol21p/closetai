-- Outfits (combinations of items)
CREATE TABLE outfits (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES profiles(id) ON DELETE CASCADE,
    name TEXT,
    item_ids UUID[] NOT NULL,
    occasion TEXT,
    season TEXT,
    style_score NUMERIC,
    color_harmony_score NUMERIC,
    source TEXT DEFAULT 'ai',
    is_favorite BOOLEAN DEFAULT FALSE,
    times_worn INTEGER DEFAULT 0,
    last_worn_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_outfits_user ON outfits(user_id);

ALTER TABLE outfits ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can view their own outfits"
    ON outfits FOR SELECT
    USING (auth.uid() = user_id);

CREATE POLICY "Users can insert their own outfits"
    ON outfits FOR INSERT
    WITH CHECK (auth.uid() = user_id);

CREATE POLICY "Users can update their own outfits"
    ON outfits FOR UPDATE
    USING (auth.uid() = user_id);

CREATE POLICY "Users can delete their own outfits"
    ON outfits FOR DELETE
    USING (auth.uid() = user_id);

-- Outfit History (what was actually worn)
CREATE TABLE outfit_history (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES profiles(id) ON DELETE CASCADE,
    outfit_id UUID REFERENCES outfits(id) ON DELETE SET NULL,
    item_ids UUID[],
    worn_date DATE NOT NULL,
    occasion TEXT,
    rating INTEGER,
    feedback TEXT,
    weather_conditions JSONB,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_history_user_date ON outfit_history(user_id, worn_date);

ALTER TABLE outfit_history ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can view their own history"
    ON outfit_history FOR SELECT
    USING (auth.uid() = user_id);

CREATE POLICY "Users can insert their own history"
    ON outfit_history FOR INSERT
    WITH CHECK (auth.uid() = user_id);

CREATE POLICY "Users can update their own history"
    ON outfit_history FOR UPDATE
    USING (auth.uid() = user_id);
