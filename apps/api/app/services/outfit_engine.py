"""Outfit Engine - Generates outfit combinations from wardrobe items."""

from typing import Optional


def generate_outfit_candidates(
    items: list[dict],
    occasion: Optional[str] = None,
    season: Optional[str] = None,
    exclude_recently_worn: list[str] | None = None,
) -> list[dict]:
    """Generate candidate outfits from wardrobe items.

    Basic algorithm:
    1. Filter items by occasion and season
    2. Group by category (need at least top + bottom or dress)
    3. Score combinations by color harmony and style matching
    4. Return top candidates
    """
    exclude_ids = set(exclude_recently_worn or [])

    # Filter available items
    available = [
        item for item in items
        if item["id"] not in exclude_ids and not item.get("is_archived", False)
    ]

    if occasion:
        available = [
            item for item in available
            if not item.get("occasion_tags") or occasion in item.get("occasion_tags", [])
        ]

    if season:
        available = [
            item for item in available
            if not item.get("season_tags")
            or season in item.get("season_tags", [])
            or "all-season" in item.get("season_tags", [])
        ]

    # Group by category
    by_category: dict[str, list[dict]] = {}
    for item in available:
        cat = item.get("category", "other")
        by_category.setdefault(cat, []).append(item)

    outfits = []

    # Strategy 1: Top + Bottom (+ optional outerwear, footwear, accessory)
    tops = by_category.get("top", [])
    bottoms = by_category.get("bottom", [])
    shoes = by_category.get("footwear", [])

    for top in tops[:10]:
        for bottom in bottoms[:10]:
            outfit = {
                "item_ids": [top["id"], bottom["id"]],
                "items": [top, bottom],
                "score": _score_combination([top, bottom]),
            }
            if shoes:
                outfit["item_ids"].append(shoes[0]["id"])
                outfit["items"].append(shoes[0])
            outfits.append(outfit)

    # Strategy 2: Dresses
    dresses = by_category.get("dress", [])
    for dress in dresses[:5]:
        outfit = {
            "item_ids": [dress["id"]],
            "items": [dress],
            "score": _score_combination([dress]),
        }
        if shoes:
            outfit["item_ids"].append(shoes[0]["id"])
            outfit["items"].append(shoes[0])
        outfits.append(outfit)

    # Sort by score
    outfits.sort(key=lambda x: x["score"], reverse=True)
    return outfits[:5]


def _score_combination(items: list[dict]) -> float:
    """Score an outfit combination (0-100).

    Factors: color harmony, formality consistency, variety.
    """
    if not items:
        return 0.0

    score = 50.0  # Base score

    # Formality consistency bonus
    formality_levels = [
        item.get("formality_level", 3) for item in items if item.get("formality_level")
    ]
    if formality_levels:
        spread = max(formality_levels) - min(formality_levels)
        score += max(0, 20 - spread * 10)  # Closer formality = higher score

    # Color variety bonus (not all same color)
    all_colors = []
    for item in items:
        all_colors.extend(item.get("dominant_colors", []))
    unique_colors = len(set(all_colors))
    if unique_colors >= 2:
        score += 15
    if unique_colors >= 3:
        score += 10

    return min(100, max(0, score))
