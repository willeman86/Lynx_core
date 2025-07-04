import os
import time
import requests

TOKEN = os.getenv("LYNX_TOKEN")
HA_URL = "http://homeassistant.local:8123"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

def announce_start():
    data = {
        "message": "LYNX Agent has awakened and is active.",
        "title": "Project LYNX"
    }
    try:
        requests.post(f"{HA_URL}/api/services/persistent_notification/create", headers=headers, json=data)
    except Exception as e:
        print("Failed to send announcement:", e)

if __name__ == "__main__":
    while True:
        announce_start()
        time.sleep(3600)