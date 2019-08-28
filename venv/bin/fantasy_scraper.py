from bs4 import BeautifulSoup
import requests
from player import Player

# Scrapes data using Beautiful Soup from the espn fantasy hockey rankings site and creates an array of all the players

# Assign url to be scraped from
url = "https://www.espn.com/fantasy/hockey/story/_/id/27155014/early-fantasy-hockey-rankings-2019-20"

# Makes sure site is accessible
response = requests.get(url,timeout=5)

# Parses the data from the site using BeautifulSoup
content = BeautifulSoup(response.content,"html.parser")
playerArr = []

# Loops through the correct tables and parses the data from the tables by ',' or '.' accordingly
for playerStats in content.findAll('tr', attrs= {"class":"last"}): 
    stats = playerStats.findAll('td')
    parsed = stats[0].text.split(',')
    rank_name = parsed[0].split('.',1)
    # Create a new Player
    player = Player(rank_name[0],rank_name[1],parsed[2].upper(),parsed[1].split()[0])
    # Add Player to the array
    playerArr.append(player)


