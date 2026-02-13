"""Weather Service - Fetches weather data for outfit context."""

import httpx
from app.config import get_settings


async def get_weather(lat: float, lon: float) -> dict:
    """Get current weather from OpenWeatherMap API."""
    settings = get_settings()
    if not settings.openweathermap_api_key:
        return {"available": False}

    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params={
                "lat": lat,
                "lon": lon,
                "appid": settings.openweathermap_api_key,
                "units": "metric",
            },
        )
        data = response.json()

    return {
        "available": True,
        "temp_c": data.get("main", {}).get("temp"),
        "feels_like_c": data.get("main", {}).get("feels_like"),
        "humidity": data.get("main", {}).get("humidity"),
        "condition": data.get("weather", [{}])[0].get("main", ""),
        "description": data.get("weather", [{}])[0].get("description", ""),
    }


def weather_to_season_hint(temp_c: float | None) -> str:
    """Convert temperature to a season hint for outfit filtering."""
    if temp_c is None:
        return "all-season"
    if temp_c >= 30:
        return "summer"
    if temp_c >= 20:
        return "all-season"
    if temp_c >= 10:
        return "winter"
    return "winter"
