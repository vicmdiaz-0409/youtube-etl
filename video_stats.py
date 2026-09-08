import requests
import json
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")

PART = 'contentDetails'
API_KEY = os.getenv("API_KEY")
CHANNEL_HANDLE = os.getenv("CHANNEL_HANDLE")

def get_playlist_id():
    try:
        url = f"https://youtube.googleapis.com/youtube/v3/channels?part={PART}&forHandle={CHANNEL_HANDLE}&key={API_KEY}"
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        
        channel_items = data["items"][0]
        channel_playlistID = channel_items["contentDetails"]["relatedPlaylists"]["uploads"]
        return channel_playlistID
    except requests.exceptions.RequestException as e:
        raise e
         
if __name__ == "__main__":
    get_playlist_id()