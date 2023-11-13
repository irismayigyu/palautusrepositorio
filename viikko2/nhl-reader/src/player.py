import requests
class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.team = dict["team"]
        self.goals = dict["goals"]
        self.assists = dict["assists"]
        self.points = self.assists + self.goals
    
    def __str__(self):
        return f"{self.name} {self.team} {self.goals} + {self.assists} = {self.points}"

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        self.players = []
        self.response=requests.get(self.url).json()

        for player_dict in self.response:
            player = Player(player_dict)
            self.players.append(player)
        return self.players

class PlayerStats:
    def __init__(self, reader):
        self.players=reader.get_players()
        print("Suomalaiset pelaajat:")

    def top_scorers_by_nationality(self,nat):
        self.players = list(filter(lambda player: player.nationality == nat, self.players))
        self.players = sorted(self.players, key=lambda player: player.points, reverse=True)
        return self.players
