import os
import time
import hmac
import hashlib
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
BASE_URL = os.getenv("BASE_URL")


def _sign(params):
    query = "&".join([f"{k}={v}" for k, v in params.items()])
    signature = hmac.new(
        API_SECRET.encode(),
        query.encode(),
        hashlib.sha256
    ).hexdigest()
    return query + "&signature=" + signature


def send_request(endpoint, params):
    params["timestamp"] = int(time.time() * 1000)

    query = _sign(params)
    url = BASE_URL + endpoint + "?" + query

    headers = {
        "X-MBX-APIKEY": API_KEY
    }

    for _ in range(3):
        try:
            response = requests.post(url, headers=headers, timeout=5)
            return response.json()
        except Exception:
            time.sleep(1)

    return {"error": "Request failed"}