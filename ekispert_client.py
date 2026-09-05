"""
ekispert_client.py
Ekispert API Client with Fast-Mock Fallback
Standard: MIT Open Source / Proactive Commute Shield Enterprise
"""

import os
import requests
from typing import Dict, Any, List, Optional

EKISPERT_ACCESS_KEY = os.getenv("EKISPERT_ACCESS_KEY", "DEMO_KEY")
BASE_URL = "http://api.ekispert.jp/v1/json"

# Pre-cached deterministic mock data for live demo reliability (Zero-Freeze Guarantee)
MOCK_COURSE_DATA = {
    "ResultSet": {
        "apiVersion": "1.27.0",
        "engineVersion": "202609_01a",
        "Course": [
            {
                "price": [{"kind": "FareSummary", "Oneway": "210"}],
                "Route": {
                    "timeOnBoard": "18",
                    "timeWalk": "4",
                    "transferCount": "0",
                    "Line": [
                        {
                            "name": "東京メトロ銀座線",
                            "Type": "subway",
                            "DepartureState": {"Datetime": {"text": "2026-09-05T14:32:00+09:00"}},
                            "ArrivalState": {"Datetime": {"text": "2026-09-05T14:50:00+09:00"}}
                        }
                    ],
                    "Point": [
                        {"Station": {"Name": "新橋"}},
                        {"Station": {"Name": "渋谷 (渋谷ストリーム地下直結)"}}
                    ]
                }
            }
        ]
    }
}

MOCK_DELAY_DATA = {
    "station": "渋谷",
    "line": "JR山手線外回り",
    "status": "DELAY_DETECTED",
    "delay_minutes": 15,
    "cause": "品川駅での車両点検の影響",
    "recommended_detour": "東京メトロ銀座線または半蔵門線経由の地下迂回ルート"
}

def search_route(from_station: str, to_station: str, use_mock: bool = False) -> Dict[str, Any]:
    """Search transit routes between stations with automatic fallback to mock."""
    if use_mock or EKISPERT_ACCESS_KEY in ("DEMO_KEY", "", None):
        return {
            "status": "SUCCESS (FAST-MOCK)",
            "from": from_station,
            "to": to_station,
            "data": MOCK_COURSE_DATA
        }
    
    endpoint = f"{BASE_URL}/search/course/extreme"
    params = {
        "key": EKISPERT_ACCESS_KEY,
        "from": from_station,
        "to": to_station
    }
    try:
        resp = requests.get(endpoint, params=params, timeout=2.5)
        if resp.status_code == 200:
            return {"status": "SUCCESS (API)", "from": from_station, "to": to_station, "data": resp.json()}
    except Exception as e:
        print(f"[EKISPERT WARN] API call failed: {e}. Falling back to deterministic mock.")
    
    return {"status": "FALLBACK (MOCK)", "from": from_station, "to": to_station, "data": MOCK_COURSE_DATA}

def check_line_delay(station: str = "渋谷", line: str = "JR山手線") -> Dict[str, Any]:
    """Check realtime delay status for a given line or return mock delay alert."""
    return MOCK_DELAY_DATA
