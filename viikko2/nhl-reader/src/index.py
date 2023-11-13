import requests
from player import Player, PlayerReader, PlayerStats

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")
    # response = requests.get(url).json()

    # print("JSON-muotoinen vastaus:")
    # print(response)

    # players = []

    # for player_dict in response:
    #     player = Player(player_dict)
    #     players.append(player)

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
