from player import Player
class NHLTeam:

    def __init__(self, name, abbreviation):
        self.name = name
        self.abbreviation = abbreviation
        self.totalFantasyPlayers = 0
        self.numForwards = 0
        self.numDefense = 0
        self.numGoalies = 0
        self.players = []

    def add_forward(self,player):
        self.totalFantasyPlayers += 1
        self.numForwards += 1
        self.players.append(Player(player.rank,player.name,player.team,player.position))

    def add_defense(self,player):
        self.totalFantasyPlayers += 1
        self.numDefense += 1
        self.players.append(Player(player.rank,player.name,player.team,player.position))

    def add_goalie(self,player):
        self.totalFantasyPlayers += 1
        self.numGoalies += 1
        self.players.append(Player(player.rank,player.name,player.team,player.position))
