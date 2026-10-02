"""Minimal Example Freight Co. client (demo only)."""
import time

import requests

BASE_URL = "https://sandbox.api.example-freight.test/v1"


def create_shipment(api_key: str, origin: str, destination: str, weight_kg: float) -> dict:
    payload = {"origin": origin, "destination": destination, "weight_kg": weight_kg}
    for _ in range(3):
        resp = requests.post(f"{BASE_URL}/shipments", json=payload,
                             headers={"Authorization": f"Bearer {api_key}"}, timeout=10)
        if resp.status_code != 429:
            resp.raise_for_status()
            return resp.json()
        time.sleep(int(resp.headers.get("Retry-After", "1")))
    raise RuntimeError("rate limited after 3 attempts")
