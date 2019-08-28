from bs4 import BeautifulSoup
import requests
import json
from player import Player

url = "https://www.espn.com/fantasy/hockey/story/_/id/27155014/early-fantasy-hockey-rankings-2019-20"
response = requests.get(url,timeout=5)
content = BeautifulSoup(response.content,"html.parser")
playerArr = []
for playerStats in content.findAll('tr', attrs= {"class":"last"}): #change to findAll
    stats = playerStats.findAll('td')
    parsed = stats[0].text.split(',')
    rank_name = parsed[0].split('.',1)
    player = Player(rank_name[0],rank_name[1],parsed[2].upper(),parsed[1].split()[0])
    playerArr.append(player)

'''
player = {
        "Name" : stats[1].text,
        "Rank" : stats[0].text,
        "Team" : stats[2].text,
        "Position" : stats[3].text
    }

with open('NHLFantasyRankings.json','w') as outfile:
    json.dump(playerArr,outfile)
'''

