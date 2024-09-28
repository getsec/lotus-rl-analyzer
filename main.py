'''program'''
import json
import os
import time
from argparse import ArgumentParser

import pandas as pd
from dotenv import load_dotenv
from pandas import json_normalize

import ballchasing
from ballchasing.config_loader import load_yaml
from ballchasing.lotus import GameData

player_map = load_yaml("player_map.yaml")


def arguments():
    parser = ArgumentParser()
    parser.add_argument("--replay", nargs="+", help="Replay ID", required=True)
    parser.add_argument(
        "--team",
        choices=[i.lower() for i in player_map.get("teams", {}).keys()],
        required=True,
    )
    parser.add_argument("--filename", help="Filename to save to", default="output.csv")
    return parser.parse_args()


if __name__ == "__main__":
    load_dotenv()
    args = arguments()
    players = player_map.get("teams", {}).get(args.team, [])
    if not players:
        raise ValueError(f"Team {args.team} not found in player_map.yaml")

    print(f"Team {args.team} players: ")
    print(" - " + "\n - ".join(players))
    print(players)
    key = os.getenv("BALLCHASING_KEY")
    api = ballchasing.Api(key)
    team_ids = players.values()
    print(team_ids)
    print(args.replay)
    alloutput_player_data = []
    timeout = False
    if len(args.replay) > 2:
        timeout = True
    for replay in args.replay:
        ballchasing_replay_content = api.get_replay(replay)
        # if were missing needed data skip.
        all_player_data = ballchasing_replay_content.get("blue", {}).get(
            "players", []
        ) + ballchasing_replay_content.get("orange", {}).get("players", [])
        for player_name, player_id in players.items():
            for content in all_player_data:
                if content["id"]["id"] == str(player_id):
                    print(f"Found {player_name} in replay")
                    alloutput_player_data.append(
                        GameData(
                            name=player_name,
                            player_id=player_id,
                            replay_id=replay,
                            shots=content["stats"]["core"]["shots"],
                            goals=content["stats"]["core"]["goals"],
                            saves=content["stats"]["core"]["saves"],
                            score=content["stats"]["core"]["score"],
                            shooting_percentage=content["stats"]["core"][
                                "shooting_percentage"
                            ],
                            bpm=content["stats"]["boost"]["bpm"],
                            bcpm=content["stats"]["boost"]["bcpm"],
                            avg_amount=content["stats"]["boost"]["avg_amount"],
                            time_boost_zero=content["stats"]["boost"][
                                "time_zero_boost"
                            ],
                            avg_speed=content["stats"]["movement"]["avg_speed"],
                            total_distance=content["stats"]["movement"][
                                "total_distance"
                            ],
                            time_supersonic_speed=content["stats"]["movement"][
                                "time_supersonic_speed"
                            ],
                            time_boost_speed=content["stats"]["movement"][
                                "time_boost_speed"
                            ],
                            time_slow_speed=content["stats"]["movement"][
                                "time_slow_speed"
                            ],
                            demo_inflicted=content["stats"]["demo"]["inflicted"],
                            demo_taken=content["stats"]["demo"]["taken"],
                        )
                    )
                    # all_player_data.append(u)
        time.sleep(2) if timeout else None

    list_of_dicts = [i.__dict__ for i in alloutput_player_data]
    flat_dicts = []

    for data_dict in list_of_dicts:
        flat_data = json_normalize(data_dict)
        flat_dicts.append(flat_data)

    df = pd.concat(flat_dicts, ignore_index=True)

    # Write the DataFrame to a CSV file
    df.to_csv(args.filename, index=False)
