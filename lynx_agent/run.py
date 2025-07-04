import requests
import time
import json

# Load token from secrets.json
try:
    with open("secrets.json") as f:
        secrets = json.load(f)
        TOKEN = secrets.get("token")
except Exception as e:
    print(f"❌ Error loading secrets.json: {e}")
    TOKEN = None

BASE_URL = "http://homeassistant.local:8123"  # Use your IP if needed, like http://192.168.4.144:8123

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

def test_connection():
    if not TOKEN:
        print("❌ No token loaded.")
        return

    try:
        response = requests.get(f"{BASE_URL}/api/", headers=HEADERS)
        if response.status_code == 200:
            print("✅ Successfully connected to Home Assistant API")
        else:
            print(f"❌ Failed. Status code: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    while True:
        test_connection()
        time.sleep(30)
