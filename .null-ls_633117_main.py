import json
import os
from argparse import ArgumentParser

from dotenv import load_dotenv

import ballchasing
from src.config_loader import load_yaml

player_map = load_yaml("player_map.yaml")


def arguments():
    parser = ArgumentParser()
    parser.add_argument("--replay", help="Replay ID", required=True)
    parser.add_argument(
        "--team",
        choices=[i.lower() for i in player_map.get("teams", {}).keys()],
        required=True,
    )
    return parser.parse_args()


if __name__ == "__main__":
    load_dotenv()
    args = arguments()
    players = player_map.get("teams", {}).get(args.team, [])
    if not players:
        raise ValueError(f"Team {args.team} not found in player_map.yaml")

    print(f"Team {args.team} players: ")
    print(" - " + "\n - ".join(players))

    key = os.getenv("BALLCHASING_KEY")

    api = ballchasing.Api(key)
    replay = api.get_replay(args.replay)
    if not replay:
        raise ValueError(f"Replay {args.replay} not found")
    if not replay.get("blue") or not replay.get("orange"):
        raise ValueError(f"Replay {args.replay} is missing team data")



    blue_team = replay.get("blue", {}).get("players", [])
    orange_team = replay.get("orange", {}).get("players", [])
    
    # It doesnt really matter which the team is, we just need to know which team the players are on
    both_teams = blue_team + orange_team


    # print(json.dumps(replay, indent=4))


#
# replays = ["28209ed2-c8f7-4473-91a8-1afeb65ca0c1"]
# for i in replays:
#     resp = get_replay(i)
#     with open("replay.json", "w") as outfile:
#         json.dump(resp, outfile, indent=4)
#     print(json.dumps(resp, indent=4))
