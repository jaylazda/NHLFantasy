class Player:
    def __init__(self,rank,name,team,position):
        self.name = name
        self.rank = rank
        if team == "":
            self.team = "UFA"
        else:
            self.team = team.split()[0]
        self.position = position
