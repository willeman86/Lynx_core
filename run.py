import time
import requests

TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhYTA1ZjY5NDlhZDY0OTBhODA5ODMzNTkxYzRkYjZiNCIsImlhdCI6MTc1MTYwMTEyNiwiZXhwIjoyMDY2OTYxMTI2fQ.Lzolm9SXUbQ5IjltklmaQqd4Lt4cee5xlVY-GLVN-q8"
HA_URL = "http://homeassistant.local:8123"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

def announce_start():
    data = {
        "message": "LYNX Agent has awakened and is ready for command input.",
        "title": "Project LYNX"
    }
    try:
        requests.post(f"{HA_URL}/api/services/persistent_notification/create", json=data, headers=headers)
    except Exception as e:
        print("Failed to send announcement:", e)

if __name__ == "__main__":
    while True:
        announce_start()
        time.sleep(3600)