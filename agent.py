from typing import Dict, Any, List
from src.utils.helpers import process_image, analyze_risk
from src.utils.weather_api import get_weather_data
from src.utils.stripe_handler import process_payment
from src.utils.document_generator import generate_policy_document
import uuid

class InsuranceAgent:
    def __init__(self):
        self.memory = {}
        
    async def process_insurance_request(self, image_path: str, location: str, coverage_type: str) -> Dict[Any, Any]:
        # Analiza slike in identifikacija predmetov
        items = await process_image(image_path)
        
        # Ocena tveganja
        risk_assessment = analyze_risk(items, location)
        
        # Pridobivanje vremenskih podatkov
        weather_data = await get_weather_data(location)
        
        # Izračun premije
        premium = self.calculate_premium(risk_assessment, weather_data)
        
        return {
            "items": items,
            "risk_assessment": risk_assessment,
            "premium": premium,
            "weather_data": weather_data
        }
    
    def calculate_premium(self, risk_assessment: Dict, weather_data: Dict) -> float:
        # Implementacija izračuna premije
        base_premium = risk_assessment["base_rate"]
        weather_factor = weather_data["risk_factor"]
        return base_premium * weather_factor 

    def process_claim(self, claim_data: Dict[str, Any]) -> Dict[str, Any]:
        """Procesira škodni zahtevek."""
        # Implementacija procesiranja škodnega zahtevka
        claim_assessment = self._assess_claim(claim_data)
        estimated_payout = self._calculate_payout(claim_assessment)
        
        return {
            "claim_id": str(uuid.uuid4()),
            "status": "processing",
            "assessment": claim_assessment,
            "estimated_payout": estimated_payout
        }

    def generate_prevention_plan(self, risk_assessment: Dict[str, Any]) -> Dict[str, Any]:
        """Generira preventivni načrt na podlagi ocene tveganja."""
        recommendations = []
        
        # Analiza tveganj in generiranje priporočil
        if risk_assessment["risk_factors"].get("valuable_items", 0) > 0.3:
            recommendations.append({
                "type": "security",
                "description": "Namestitev varnostnega sistema",
                "priority": "high"
            })
        
        if risk_assessment["risk_factors"].get("hazardous_items", 0) > 0.2:
            recommendations.append({
                "type": "safety",
                "description": "Namestitev detektorjev dima",
                "priority": "high"
            })
        
        return {
            "recommendations": recommendations,
            "risk_reduction_potential": self._calculate_risk_reduction(recommendations)
        }

    def _calculate_risk_reduction(self, recommendations: List[Dict[str, Any]]) -> float:
        """Izračuna potencialno zmanjšanje tveganja."""
        reduction = 0.0
        for rec in recommendations:
            if rec["priority"] == "high":
                reduction += 0.2
            elif rec["priority"] == "medium":
                reduction += 0.1
            else:
                reduction += 0.05
        return min(reduction, 0.5)  # Maksimalno 50% zmanjšanje