"""Shopping Intelligence - Gap analysis and purchase recommendations."""


def analyze_wardrobe_gaps(items: list[dict], style_profile: dict) -> list[dict]:
    """Analyze wardrobe for gaps and suggest purchases.

    Each suggestion includes:
    - category/subcategory to buy
    - reason (why it's missing)
    - outfit_unlock_count (how many new outfits it enables)
    - priority (high/medium/low)
    """
    suggestions = []

    # Category counts
    categories: dict[str, int] = {}
    for item in items:
        cat = item.get("category", "other")
        categories[cat] = categories.get(cat, 0) + 1

    # Basic category gaps
    if categories.get("top", 0) > 5 and categories.get("bottom", 0) < 3:
        suggestions.append({
            "category": "bottom",
            "description": "You have many tops but few bottoms, limiting outfit variety",
            "reason": f"You have {categories.get('top', 0)} tops but only {categories.get('bottom', 0)} bottoms",
            "outfit_unlock_count": categories.get("top", 0),
            "priority": "high",
        })

    if categories.get("bottom", 0) > 5 and categories.get("top", 0) < 3:
        suggestions.append({
            "category": "top",
            "description": "More tops would dramatically increase your outfit options",
            "reason": f"You have {categories.get('bottom', 0)} bottoms but only {categories.get('top', 0)} tops",
            "outfit_unlock_count": categories.get("bottom", 0),
            "priority": "high",
        })

    if not categories.get("outerwear"):
        suggestions.append({
            "category": "outerwear",
            "subcategory": "jacket",
            "description": "A versatile jacket adds layering options to every outfit",
            "reason": "No outerwear in your closet",
            "outfit_unlock_count": min(len(items), 10),
            "priority": "medium",
        })

    if not categories.get("footwear") or categories.get("footwear", 0) < 2:
        suggestions.append({
            "category": "footwear",
            "description": "A second pair of shoes doubles your outfit finishing options",
            "reason": f"Only {categories.get('footwear', 0)} pair(s) of shoes",
            "outfit_unlock_count": 5,
            "priority": "medium",
        })

    # Color gap analysis
    all_colors = []
    for item in items:
        all_colors.extend(item.get("dominant_colors", []))
    if all_colors:
        neutral_colors = {"black", "white", "grey", "gray", "navy", "beige", "cream"}
        has_neutrals = any(c.lower() in neutral_colors for c in all_colors)
        if not has_neutrals:
            suggestions.append({
                "category": "top",
                "description": "A neutral-colored basic would pair with most of your wardrobe",
                "reason": "No neutral basics found in your closet",
                "outfit_unlock_count": len(items) // 2,
                "priority": "medium",
            })

    return suggestions


def check_duplicate(new_item_tags: dict, existing_items: list[dict]) -> list[dict]:
    """Check if a potential purchase is similar to items already owned.

    Returns list of similar existing items.
    """
    similar = []
    new_category = new_item_tags.get("category", "")
    new_colors = set(new_item_tags.get("dominant_colors", []))

    for item in existing_items:
        if item.get("category") != new_category:
            continue

        item_colors = set(item.get("dominant_colors", []))
        color_overlap = len(new_colors & item_colors)
        same_pattern = item.get("pattern") == new_item_tags.get("pattern")
        same_sub = item.get("subcategory") == new_item_tags.get("subcategory")

        if (color_overlap >= 1 and same_pattern) or (same_sub and color_overlap >= 2):
            similar.append(item)

    return similar
