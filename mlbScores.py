import urllib.request
import json 

urllib.request.urlretrieve("https://statsapi.mlb.com/api/v1/schedule?sportId=1&date?&hydrate=team(leaders(showOnPreview(leaderCategories=[homeRuns,runsBattedIn,battingAverage],statGroup=[pitching,hitting]))),linescore(matchup,runners),flags,liveLookin,review,broadcasts(all),decisions,person,probablePitcher,stats,homeRuns,previousPlay,game(content(media(featured,epg),summary),tickets),seriesStatus(useOverride=true)&language=en", "mlb.json")
mlbData = json.loads(open('mlb.json').read())

games = mlbData['totalItems']

homeTeams = []
awayTeams = []#call once from the api
homeScore = []
awayScore = []
status = []
venue = []
awayRecord = []
homeRecord = []


for n in range(games):
	awayTeams.append ( mlbData['dates'][0]['games'][n]['teams']['away']['team']['name'])
	homeTeams.append ( mlbData['dates'][0]['games'][n]['teams']['home']['team']['name'])
	awayScore.append ( mlbData['dates'][0]['games'][n]['teams']['away']['score'])
	homeScore.append ( mlbData['dates'][0]['games'][n]['teams']['home']['score'])
	status.append( mlbData['dates'][0]['games'][n]['status']['detailedState'])
	awayRecord.append( '(' +str(mlbData['dates'][0]['games'][n]['teams']['away']['leagueRecord']['wins']) + '-' + str(mlbData['dates'][0]['games'][n]['teams']['away']['leagueRecord']['losses']) + ')')
	homeRecord.append( '(' + str(mlbData['dates'][0]['games'][n]['teams']['home']['leagueRecord']['wins'])+ '-' + str(mlbData['dates'][0]['games'][n]['teams']['home']['leagueRecord']['losses']) + ')')
	venue.append     ( mlbData['dates'][0]['games'][n]['venue']['name'])

def printMatchups():
	for n in range(games):
		print(awayTeams[n] + ' ' + str(awayScore[n]) + ' at ' + str(homeScore[n]) + ' ' + homeTeams[n])
		print(awayRecord[n] + '   ' + status[n]+ '   ' + homeRecord[n] )
		print(venue[n] + '\n')
printMatchups()