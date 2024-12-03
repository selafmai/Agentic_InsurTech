import cv2
import numpy as np
from typing import Dict, List, Any
import torch
from PIL import Image

class ImageProcessor:
    def __init__(self):
        # Naložimo YOLO model za detekcijo objektov
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
        
    async def process_image(self, image_path: str) -> Dict[str, Any]:
        """Procesira sliko in identificira predmete."""
        try:
            # Preberi sliko
            if isinstance(image_path, str):
                image = Image.open(image_path)
            else:
                image = Image.open(image_path.file)
            
            # Detekcija objektov
            results = self.model(image)
            
            # Procesiranje rezultatov
            detected_objects = self._process_detections(results)
            
            return {
                "detected_objects": detected_objects,
                "count": len(detected_objects),
                "risk_factors": self._calculate_risk_factors(detected_objects)
            }
        except Exception as e:
            return {
                "error": str(e),
                "detected_objects": [],
                "count": 0,
                "risk_factors": {}
            }
    
    def _process_detections(self, results) -> List[Dict[str, Any]]:
        """Procesira rezultate detekcije."""
        detected_objects = []
        
        for pred in results.pred[0]:
            obj = {
                "class": results.names[int(pred[5])],
                "confidence": float(pred[4]),
                "bbox": pred[:4].tolist()
            }
            detected_objects.append(obj)
            
        return detected_objects
    
    def _calculate_risk_factors(self, objects: List[Dict[str, Any]]) -> Dict[str, float]:
        """Izračuna faktorje tveganja na podlagi zaznanih objektov."""
        risk_factors = {
            "valuable_items": 0.0,
            "hazardous_items": 0.0,
            "safety_equipment": 0.0
        }
        
        for obj in objects:
            if obj["class"] in ["laptop", "tv", "phone"]:
                risk_factors["valuable_items"] += 0.1
            elif obj["class"] in ["oven", "stove"]:
                risk_factors["hazardous_items"] += 0.2
            elif obj["class"] in ["smoke_detector", "security_camera"]:
                risk_factors["safety_equipment"] -= 0.1
                
        return risk_factors 