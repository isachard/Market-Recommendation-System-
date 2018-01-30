#! /usr/bin/env python3
#--------------------------------#
#__author__ = "Isachard Rodriguez"
#__version__ = "1.0.1"
#__maintainer__ = "Rob Knight"
#__email__ = "isachard@uoregon.edu"
#__status__ = "Pre - Alpha"
#__Version__ = "1.0.0"
#__Python Version: "3.4x"
#__date__ = "9-1-2017"
#--------------------------------#
""" 
Description:
"""
import datetime
import json 
import urllib.request



#Requesting Data for nba and nhl lines and scores
def webRequest (file):


	if ( )

	try :
		urllib.request.urlretrieve("http://www.sportsline.com/sportsline-web/service/v1/oddsPageContent?league=nba&auth=3", "nba.json")
		urllib.request.urlretrieve("http://www.sportsline.com/sportsline-web/service/v1/oddsPageContent?league=nhl&auth=3", "nhl.json")
		urllib.request.urlretrieve("https://data.nba.com/data/5s/v2015/json/mobile_teams/nba/2017/scores/00_todays_scores.json", "nbafinal.json")
		urllib.request.urlretrieve("https://statsapi.web.nhl.com/api/v1/schedule?expand=schedule.teams,schedule.scoringplays", "nhlScores.json")

	#parsing json files 
	configNBA = json.loads(open('nba.json').read())
	configNHL = json.loads(open('nhl.json').read())
	configNBAFinal = json.loads(open('nbafinal.json').read())
	configNHLFinal = json.loads(open('nhlScores.json').read())
