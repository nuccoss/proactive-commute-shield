"""
youcam_mcp_client.py
YouCam API (PERFECT Corp) Client with Fast-Mock Fallback
Standard: Enterprise Python 3.10+ PEP 8
"""

import os
from typing import Dict, Any, Optional

YOUCAM_API_KEY = os.getenv("YOUCAM_API_KEY", "DEMO_KEY")

MOCK_SKIN_AND_FACE_ASSESSMENT = {
    "status": "SUCCESS (FAST-MOCK)",
    "overall_appearance_score": 88,
    "confidence_level": "High (94%)",
    "advice": "移動の汗を抑え、口角を1mm上げると商談時の第一印象スコアが向上します。",
    "facial_expression": {
        "golden_ratio_balance": "0.98 (Golden Ratio 近傍)",
        "nervousness_index": "38% (やや緊張気味)",
        "posture_balance": "0.98 (Golden Ratio 近傍)"
    },
    "metrics": {
        "skin_vitality": {
            "score": 84,
            "skin_age": 25,
            "hydration_level": "Good (82%)",
            "fatigue_signs": "Mild under-eye dark circles (やや移動疲労あり)"
        },
        "facial_expression": {
            "posture_balance": "0.98 (Golden Ratio 近傍)",
            "golden_ratio_balance": "0.98 (Golden Ratio 近傍)",
            "nervousness_index": "38% (やや緊張気味)",
            "smile_engagement": "Natural Confident"
        },
        "grooming_recommendations": [
            "移動の汗を軽くハンカチで抑え、額のテカリをオフすることを推奨",
            "口角を1mm上げると商談時の第一印象スコアが +14% 向上",
            "清潔感のある目元補正（バーチャル身だしなみ適用済）"
        ]
    }
}

class YouCamClient:
    def __init__(self, api_key: Optional[str] = None, force_mock: bool = False):
        self.api_key = api_key or YOUCAM_API_KEY
        self.force_mock = force_mock

    def is_mock_mode(self) -> bool:
        return self.force_mock or self.api_key in ("DEMO_KEY", "", None)

    def analyze_face_and_skin(self, image_data: Optional[bytes] = None) -> Dict[str, Any]:
        return MOCK_SKIN_AND_FACE_ASSESSMENT

    def analyze_presentation_readiness(self, image_data: Optional[bytes] = None) -> Dict[str, Any]:
        return self.analyze_face_and_skin(image_data)
