import json
import os

import requests
from dotenv import load_dotenv

from src.config_loader import load_yaml

load_dotenv()
player_map = load_yaml("player_map.yaml")
print(player_map)
key = os.getenv("BALLCHASING_KEY")
ROOT = "https://ballchasing.com/api"


def get_replay(replay_id: str) -> dict:
    return requests.get(
        f"{ROOT}/replays/{replay_id}", headers={"Authorization": key}
    ).json()


replays = ["28209ed2-c8f7-4473-91a8-1afeb65ca0c1"]
for i in replays:
    resp = get_replay(i)
    with open("replay.json", "w") as outfile:
        json.dump(resp, outfile, indent=4)
    print(json.dumps(resp, indent=4))
