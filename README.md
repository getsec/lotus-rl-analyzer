# Rocket League Data Analyzer

## Requirements
Ensure you have git, and python installed.

```bash
# Clone the repo
git clone https://github.com/getsec/lotus-rl-analyzer && cd lotus-rl-analyzer

# Install dependencies
pip install -r requirements.txt

# Ur ready
```

## Configuration
### Setup Ballchasing API Key
Copy the .env.example file to a new file named .env. Open the .env file and 
replace the placeholder values with your corresponding API key 
from ballchasing.com.

```env
BALLCHASING_API_KEY=your_api_key_here
```

This API key is necessary for authenticating and retrieving Rocket League data from the ballchasing.com API.
### Setup your player map
To analyze Rocket League data from ballchasing.com, you need to specify 
the players in your teams along with their corresponding Ballchasing account IDs. 
This information is stored in the player_map.yaml file. Here's an example:

```yaml
teams:
  l8_nirvana_us:
    Dave: 76561198147545404
    Lock: 76561198832732509
    Happy: 76561198376718102

  l8_nirvana_can:
    Sleepy: 76561198179499362
    Garlic: c5026d752bc546c58fedb21bf3cd1c6c
    Jaw: 76561199047964745

  l8_zenith_us:
    Cloud: 76561198352320795
    Speed: 76561198413993679
    Silk: 76561198885334892

  l8_zenith_cam:
    Catman: 76561198807275226
    Jhn: 76561199062975842
    Kylar: 76561199053878748
    Sayzio: 76561198284776097
```
This structured YAML file allows for easy management and updating of player information.

## How to Run

The program is designed to be flexible, allowing you to analyze multiple 
replays for a specific team. Each run must be unique to a team, and you can 
supply any number of replays, as long as the same team member(s) are present in 
those replays.

To execute the program, use the following command template:

```bash
python main.py --replays <idN> --team <team_name_from_yaml>
```

For example, to analyze 10 replays for the team "l8_nirvana_us":

```bash
python main.py --replays <id1> <id2> <id3> ... <id10> --team l8_nirvana_us
```
This approach ensures that the analysis is accurate and specific to the selected 
team, and the output will be a comprehensive CSV file containing all relevant 
replay data. The modular design allows for scalability, making it easy to 
expand and analyze additional teams' data.

