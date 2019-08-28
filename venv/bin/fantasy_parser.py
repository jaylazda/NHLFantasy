from fantasy_scraper import playerArr
from hockeyTeam import NHLTeam

file = open("NHLFantasyRankings.txt","w")
file.write("This file contains data taken from the top 250 players in the 2019-2020 ESPN NHL fantasy hockey rankings.\n\n")
#initialize all 31 teams
nhl_teams = []
nhl_teams.append(NHLTeam("Anaheim Ducks","ANA"))
nhl_teams.append(NHLTeam("Arizona Coyotes","ARI"))
nhl_teams.append(NHLTeam("Boston Bruins","BOS"))
nhl_teams.append(NHLTeam("Buffalo Sabres","BUF"))
nhl_teams.append(NHLTeam("Calgary Flames","CGY"))
nhl_teams.append(NHLTeam("Carolina Hurricanes","CAR"))
nhl_teams.append(NHLTeam("Chicago Blackhawks","CHI"))
nhl_teams.append(NHLTeam("Colorado Avalance","COL"))
nhl_teams.append(NHLTeam("Columbus Blue Jackets","CLS"))
nhl_teams.append(NHLTeam("Dallas Stars","DAL"))
nhl_teams.append(NHLTeam("Detroit Red Wings","DET"))
nhl_teams.append(NHLTeam("Edmonton Oilers","EDM"))
nhl_teams.append(NHLTeam("Florida Panthers","FLA"))
nhl_teams.append(NHLTeam("Los Angeles Kings","LA"))
nhl_teams.append(NHLTeam("Minnesota Wild","MIN"))
nhl_teams.append(NHLTeam("Montreal Canadiens","MON"))
nhl_teams.append(NHLTeam("Nashville Predators","NSH"))
nhl_teams.append(NHLTeam("New Jersey Devils","NJ"))
nhl_teams.append(NHLTeam("New York Islanders","NYI"))
nhl_teams.append(NHLTeam("New York Rangers","NYR"))
nhl_teams.append(NHLTeam("Ottawa Senators","OTT"))
nhl_teams.append(NHLTeam("Philadelphia Flyers","PHI"))
nhl_teams.append(NHLTeam("Pittsburgh Penguins","PIT"))
nhl_teams.append(NHLTeam("St-Louis Blues","STL"))
nhl_teams.append(NHLTeam("San Jose Sharks","SJ"))
nhl_teams.append(NHLTeam("Tampa Bay Lightning","TB"))
nhl_teams.append(NHLTeam("Toronto Maple Leafs","TOR"))
nhl_teams.append(NHLTeam("Vancouver Canucks","VAN"))
nhl_teams.append(NHLTeam("Vegas Golden Knights","VGS"))
nhl_teams.append(NHLTeam("Washington Capitals","WAS"))
nhl_teams.append(NHLTeam("Winnipeg Jets","WPG"))

for player in playerArr:
    for team in nhl_teams:
        if player.team == team.abbreviation:
            if player.position == 'D':
                team.add_defense(player)
            elif player.position == 'G':
                team.add_goalie(player)
            else:
                team.add_forward(player)

file.write("Number of players ranked in the top 250 ESPN Fantasy Rankings per team:\n")
for team in nhl_teams:
    file.writelines([team.name,": ",str(team.totalFantasyPlayers),"\n"])

file.write("\nTop ranked player per team:\n")
for team in nhl_teams:
    if team is not None:
        file.writelines([team.name,":",team.players[0].name," rank ",str(team.players[0].rank),"\n"])

#SORT BY TOP PLAYER RANK
#SORT BY TOTAL PLAYERS

def sort_by_rank(teams): #Writes to file sorted list of each teams top player by overall rank
    teams_by_rank = []
    for i in range(31):
        highest_rank_index = 0
        for j in range(len(teams)):
            if (int)(teams[highest_rank_index].players[0].rank) > (int)(teams[j].players[0].rank):
                highest_rank_index = j
        teams_by_rank.append(teams[highest_rank_index])
        teams.remove(teams[highest_rank_index]) #fix this
    for team in teams_by_rank:
        file.writelines([team.name,": ",team.players[0].name," rank ",str(team.players[0].rank),"\n"])
    return teams_by_rank

def sort_by_most_players(teams):
    teams_by_players = []
    for i in range(31):
        most_players_index = 0
        for j in range(len(teams)):
            if (int)(teams[most_players_index].totalFantasyPlayers) < (int)(teams[j].totalFantasyPlayers):
                most_players_index = j
        teams_by_players.append(teams[most_players_index])
        teams.remove(teams[most_players_index])
    for team in teams_by_players:
        file.writelines([team.name,": ",str(team.totalFantasyPlayers),"\n"])
    return teams_by_players

file.write("\nNHL teams ranked by their best player:\n")
nhl_teams = sort_by_rank(nhl_teams)
file.write("\nNHL teams ranked by total number of ranked fantasy players:\n")
nhl_teams = sort_by_most_players(nhl_teams)
