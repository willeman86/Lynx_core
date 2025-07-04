import json
import requests
import os
import time

CONFIG_PATH = "/config/lynx_agent/secrets.json"
API_URL = "http://supervisor/core/api/states"

def load_token():
    try:
        with open(CONFIG_PATH, "r") as f:
            secrets = json.load(f)
            return secrets.get("token")
    except Exception as e:
        print(f"[ERROR] Failed to load token: {e}")
        return None

def test_connection(token):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    try:
        response = requests.get(API_URL, headers=headers)
        if response.status_code == 200:
            print("[OK] Connected to Home Assistant API")
            return True
        else:
            print(f"[FAIL] API Error {response.status_code}: {response.text}")
            return False
    except Exception as e:
        print(f"[ERROR] Connection failed: {e}")
        return False

if __name__ == "__main__":
    print("[INFO] Starting Lynx Agent bridge test...")
    
    token = load_token()
    if not token:
        print("[ERROR] No token found.")
        exit(1)

    while True:
        if test_connection(token):
            print("[INFO] Success. Agent is connected.")
        else:
            print("[WARN] Failed to connect. Retrying in 30 seconds...")
        
        time.sleep(30)
