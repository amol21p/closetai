"""AI Stylist Service - Claude Vision for item recognition, Claude for outfit advice."""

import anthropic
from app.config import get_settings


async def analyze_clothing_image(image_base64: str) -> dict:
    """Use Claude Vision to analyze a clothing item photo.

    Returns detected attributes: category, subcategory, colors, pattern,
    material, formality, occasion tags, season tags, and description.
    """
    settings = get_settings()
    client = anthropic.Anthropic(api_key=settings.anthropic_api_key)

    message = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg",
                            "data": image_base64,
                        },
                    },
                    {
                        "type": "text",
                        "text": """Analyze this clothing item photo and return a JSON object with:
{
  "category": "top|bottom|dress|outerwear|footwear|accessory|bag|jewelry|ethnic",
  "subcategory": "specific type (e.g., t-shirt, blouse, jeans, sneakers)",
  "dominant_colors": ["list of 1-3 main colors"],
  "pattern": "solid|striped|plaid|floral|printed|geometric|abstract|none",
  "material": "best guess (cotton, denim, silk, polyester, leather, etc.)",
  "formality_level": 1-5 (1=very casual, 5=very formal),
  "occasion_tags": ["appropriate occasions: office, casual, date-night, party, gym, travel, ethnic"],
  "season_tags": ["appropriate seasons: summer, winter, monsoon, all-season"],
  "description": "brief natural description of the item"
}
Return ONLY the JSON object, no other text.""",
                    },
                ],
            }
        ],
    )

    import json
    return json.loads(message.content[0].text)


async def get_styling_advice(
    wardrobe_summary: str, occasion: str, weather: str, preferences: str
) -> str:
    """Get personalized styling advice from Claude."""
    settings = get_settings()
    client = anthropic.Anthropic(api_key=settings.anthropic_api_key)

    message = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"""You are a personal stylist. Based on the user's wardrobe and context, suggest an outfit.

Wardrobe: {wardrobe_summary}
Occasion: {occasion}
Weather: {weather}
Style preferences: {preferences}

Suggest a complete outfit using items from their wardrobe. Explain why the combination works (color harmony, occasion appropriateness, weather suitability). Be specific about which items to pair.""",
            }
        ],
    )

    return message.content[0].text
