import json
from datetime import datetime, timedelta


def get_last_sync_time():
    try:
        with open('last_sync_time.json', 'r') as file:
            last_sync_time = json.load(file)
            return datetime.fromisoformat(last_sync_time['last_sync'])
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        return None


def update_last_sync_time():
    with open('last_sync_time.json', 'w') as file:
        json.dump({'last_sync': datetime.now().isoformat()}, file)
