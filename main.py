# Import necessary libraries
import os
import json
import time
from dotenv import load_dotenv
import sseclient
import pygame
import requests

load_dotenv()

LNBITS_HOST = os.getenv("LNBITS_HOST")
API_KEY = os.getenv("API_KEY")
SSE_ENDPOINT = f"{LNBITS_HOST}/api/v1/payments/sse?api-key={API_KEY}"
PING_SOUND = "ping.mp3"
RECONNECT_DELAY = 5  # seconds

def play_ping():
    """Play the ping sound."""
    pygame.mixer.init()
    pygame.mixer.music.load(PING_SOUND)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

def listen_to_sse():
    """Connect to the SSE endpoint and process messages."""
    while True:
        try:
            print(f"Connecting to SSE endpoint: {SSE_ENDPOINT}")
            # Use requests to handle response encoding explicitly
            with requests.get(SSE_ENDPOINT, stream=True, timeout=30) as response:
                response.encoding = 'utf-8'
                client = sseclient.SSEClient(response)
                for event in client.events():
                    if event.data:
                        message = json.loads(event.data)
                        if message.get("status") == "success":
                            print(f"Received successful payment: {message}")
                            play_ping()
        except requests.exceptions.ReadTimeout:
            print("Connection timed out. Reconnecting in 5 seconds...")
            time.sleep(RECONNECT_DELAY)
        except requests.exceptions.ConnectionError:
            print("Network connection lost. Reconnecting in 5 seconds...")
            time.sleep(RECONNECT_DELAY)
        except Exception as e:
            print(f"Unexpected error: {e}. Reconnecting in 5 seconds...")
            time.sleep(RECONNECT_DELAY)

if __name__ == "__main__":
    # Check if the ping sound file exists
    if not os.path.exists(PING_SOUND):
        print(f"Error: {PING_SOUND} not found in the current directory.")
    else:
        listen_to_sse()
