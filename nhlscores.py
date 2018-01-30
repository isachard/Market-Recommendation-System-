import urllib.request
import json 


urllib.request.urlretrieve("https://statsapi.web.nhl.com/api/v1/schedule?expand=schedule.teams,schedule.scoringplays", "nhlScores.json")




config = json.loads(open('nhlScores.json').read())# change var nam

a = config['dates'][0]

todayGames = config['dates'][0]['totalItems']

#print ( type(config) )#dic
#print ( type(config['dates']) )#list
#print ( type(config['dates'][0]) )# dic

#print (type (a))
print ()

for n in range(todayGames):


	away = config['dates'][0]['games'][n]['teams']['away']
	home = config['dates'][0]['games'][n]['teams']['home']

	print (away['team']['name'],":", away['score'], "vs ", home['score'], ":", home['team']['name'] )
	print (" (",away['leagueRecord']['wins'], " - " , away['leagueRecord']['losses'], ")" "               (",home['leagueRecord']['wins'], " - " , home['leagueRecord']['losses'], ")" )

