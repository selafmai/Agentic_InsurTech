import aiohttp
import os
from typing import Dict, Any

async def get_weather_data(location: str) -> Dict[str, Any]:
    """Pridobi vremenske podatke za lokacijo."""
    api_key = os.getenv("WEATHER_API_KEY")
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    async with aiohttp.ClientSession() as session:
        params = {
            "q": location,
            "appid": api_key,
            "units": "metric"
        }
        
        async with session.get(base_url, params=params) as response:
            data = await response.json()
            
            return {
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "conditions": data["weather"][0]["main"],
                "risk_factor": calculate_weather_risk_factor(data)
            }

def calculate_weather_risk_factor(weather_data: Dict[str, Any]) -> float:
    """Izračuna faktor tveganja na podlagi vremenskih podatkov."""
    risk_factor = 1.0
    
    # Implementacija izračuna vremenskega faktorja tveganja
    conditions = weather_data["weather"][0]["main"].lower()
    
    if "storm" in conditions:
        risk_factor *= 1.5
    elif "rain" in conditions:
        risk_factor *= 1.2
    elif "snow" in conditions:
        risk_factor *= 1.3
        
    return risk_factor 