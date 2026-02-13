"""Style DNA - Computes and evolves user style profiles."""


def compute_style_dna(
    wardrobe_items: list[dict],
    outfit_history: list[dict],
    style_profile: dict,
) -> dict:
    """Compute the Style DNA from wardrobe data and usage patterns.

    Returns a style DNA object with:
    - dominant_style: most common style archetype
    - color_palette: frequently used colors
    - formality_distribution: casual vs formal ratio
    - category_balance: how balanced the wardrobe is
    - wear_frequency: usage patterns
    - gaps: identified wardrobe gaps
    """
    dna: dict = {}

    # Color palette from wardrobe
    color_counts: dict[str, int] = {}
    for item in wardrobe_items:
        for color in item.get("dominant_colors", []):
            color_counts[color] = color_counts.get(color, 0) + 1
    dna["color_palette"] = sorted(
        color_counts.keys(), key=lambda c: color_counts[c], reverse=True
    )[:8]

    # Category balance
    category_counts: dict[str, int] = {}
    for item in wardrobe_items:
        cat = item.get("category", "other")
        category_counts[cat] = category_counts.get(cat, 0) + 1
    dna["category_balance"] = category_counts

    # Formality distribution
    formality = [
        item.get("formality_level", 3)
        for item in wardrobe_items
        if item.get("formality_level")
    ]
    if formality:
        avg = sum(formality) / len(formality)
        dna["formality_avg"] = round(avg, 1)
        dna["formality_label"] = (
            "casual" if avg < 2.5 else "balanced" if avg < 3.5 else "formal"
        )

    # Wear frequency
    total_items = len(wardrobe_items)
    worn_items = sum(1 for item in wardrobe_items if item.get("times_worn", 0) > 0)
    dna["wardrobe_utilization"] = round(worn_items / total_items * 100, 1) if total_items else 0

    # Never worn items
    dna["never_worn_count"] = total_items - worn_items

    # Gap analysis
    dna["gaps"] = _identify_gaps(category_counts, wardrobe_items)

    return dna


def _identify_gaps(category_counts: dict[str, int], items: list[dict]) -> list[str]:
    """Identify wardrobe gaps."""
    gaps = []

    essential_categories = {
        "top": 5,
        "bottom": 3,
        "footwear": 2,
        "outerwear": 1,
    }

    for category, minimum in essential_categories.items():
        count = category_counts.get(category, 0)
        if count < minimum:
            gaps.append(
                f"Only {count} {category}(s) — consider adding {minimum - count} more"
            )

    # Check occasion coverage
    occasion_coverage: set[str] = set()
    for item in items:
        occasion_coverage.update(item.get("occasion_tags", []))

    important_occasions = {"office", "casual", "party"}
    missing = important_occasions - occasion_coverage
    for occ in missing:
        gaps.append(f"No items tagged for '{occ}' occasions")

    return gaps
