"""Closet Graph - Models relationships between wardrobe items."""


def build_pairing_graph(items: list[dict], outfits: list[dict]) -> dict:
    """Build a graph of which items pair well together based on outfit history.

    Returns a dict mapping item_id -> list of {paired_item_id, pair_count}.
    """
    pair_counts: dict[tuple[str, str], int] = {}

    for outfit in outfits:
        item_ids = outfit.get("item_ids", [])
        for i, id_a in enumerate(item_ids):
            for id_b in item_ids[i + 1:]:
                pair = (min(id_a, id_b), max(id_a, id_b))
                pair_counts[pair] = pair_counts.get(pair, 0) + 1

    # Build adjacency list
    graph: dict[str, list[dict]] = {}
    for (id_a, id_b), count in pair_counts.items():
        graph.setdefault(id_a, []).append({"item_id": id_b, "pair_count": count})
        graph.setdefault(id_b, []).append({"item_id": id_a, "pair_count": count})

    # Sort by pair count
    for item_id in graph:
        graph[item_id].sort(key=lambda x: x["pair_count"], reverse=True)

    return graph


def find_versatile_items(items: list[dict], outfits: list[dict]) -> list[dict]:
    """Find the most versatile items (appear in most outfits)."""
    appearance_count: dict[str, int] = {}
    for outfit in outfits:
        for item_id in outfit.get("item_ids", []):
            appearance_count[item_id] = appearance_count.get(item_id, 0) + 1

    item_map = {item["id"]: item for item in items}
    versatile = []
    for item_id, count in sorted(
        appearance_count.items(), key=lambda x: x[1], reverse=True
    ):
        if item_id in item_map:
            versatile.append({**item_map[item_id], "outfit_count": count})

    return versatile[:10]


def find_isolated_items(items: list[dict], outfits: list[dict]) -> list[dict]:
    """Find items that don't appear in any outfit."""
    used_ids: set[str] = set()
    for outfit in outfits:
        used_ids.update(outfit.get("item_ids", []))

    return [item for item in items if item["id"] not in used_ids]
