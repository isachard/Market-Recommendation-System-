
import urllib.request
import json 
import datetime

#Requesting Data for nba and nhl lines and scores
urllib.request.urlretrieve("http://www.sportsline.com/sportsline-web/service/v1/oddsPageContent?league=nba&auth=3", "nba.json")
urllib.request.urlretrieve("http://www.sportsline.com/sportsline-web/service/v1/oddsPageContent?league=nhl&auth=3", "nhl.json")
urllib.request.urlretrieve("https://data.nba.com/data/5s/v2015/json/mobile_teams/nba/2017/scores/00_todays_scores.json", "nbafinal.json")
urllib.request.urlretrieve("https://statsapi.web.nhl.com/api/v1/schedule?expand=schedule.teams,schedule.scoringplays", "nhlScores.json")

#parsing json files 
configNBA = json.loads(open('nba.json').read())# change var nam
configNBAFinal = json.loads(open('nbafinal.json').read())# change var nam
configNHLFinal = json.loads(open('nhlScores.json').read())# change var nam
configNHL = json.loads(open('nhl.json').read())

#configLoadsNHL = json.dumps(open('nhl.json 
#**COMEBACK READ DOCUMENTAION .dumps documentation

#NBA parsing variables
stackNamesNBAToday = []
stackNamesNBATomorrow = []
stackNBASpreadToday = []
stackNBASpreadTomorrow = []
stackNBATotal = []
stackNBASeo = []

#NBAstreaks
nbaSheet = {}
nbaLines = []

#NHL parsing variables
stackNamesNHLToday = []#change 'N'
stackNamesNHLTomorrow = []
stackNHLSpreadToday = []
stackNHLSpreadTomorrow = []
stackNHLSeo = []
stackNHLTotal = []

#NBA Scores variable
nbaScoreAname = []
nbaScoreHname = []
nbaScoreA = []
nbaScoreH = []
periodNba = []

#NHL Scores variable
nhlScoreAname = []
nhlScoreHname = []
nhlScoreA = []
nhlScoreH = []
periodNhl = []

#NBAStreaksSpread
nbaStreakSpread = {}

dateGame = 'cbsGameAbbrv' #"NBA_20171128_MIA@CLE",
todayGames = []
tomGames = []
space = '   '
stcAway = 'awayTeamAbbrv'
stcHome = 'homeTeamAbbrv' # var move 
awayNBA = 'awayTeamName'
awayNHL = 'awayTeamName'
homeNBA = 'homeTeamName'
homeNHL = 'homeTeamName'
atsNBA = 'atsHandicap'
atsNHL = 'atsHandicap'
ouNBA = 'ouTotal'
ouNHL = 'ouTotal'
seoNBA = 'seoName'
seoNHL = 'seoName'
oddsNBA = configNBA['odds']
oddsNHL = configNHL['odds']
oddsNBAFinal =configNBAFinal['gs']['g']
nhlGames = configNHLFinal['dates'][0]['totalItems']

""" TO DO :
		KEY ERROR FIX
		OVER UNDER SHOWING SCORE
		SPREAD SHOWING SCORE
		ALG AND STORE VALUES FOR LOSERS AND WINNERS AND O/U
		STORE PROPER MATCHUPS AND AFTER RESULTS (MORE JSON I GUESS GOOGLE IT)
		LINE DRIFT ( TONIGHT)
		REMEMBER AWAY TEAMS FIRST ON STACK
		BETTER NAMES!!!!****ASAP
		ERROR HANDELING
		URL LINKS
		LINES DRIFT ( VALUE PLUS VALUES)
		SPREAD LIKE TEAM RANKINGS (OPEN LINES VS CLOSING LINES  ANY VALUE RETURN?)
		AUTOMATED TRENDS AND STREAKS WITH %
		DATABASES
		NHL SCORES Done, more testing with the call for the json file (1<)
		QUARTERS RESULTS BETER CLI LINE 
		TIME FOR THE MATCH 
		NCAA SCORES
		SCORE WITH COVERING RESULTS 
		AVERAGE COVERING RESULTS (O/U)
		WIN -LOSS STATS
		O-U STATS
		FINALLY STREAKS
		HISTORY OF LINES SINCE OPENING
		$ PERC. OVER PLUS UNDERS
"""
#print (type (oddsNBA)) #list
#print (type (oddsNBA[1]))#dict
#print (type (oddsNBA[1][homeNBA]))#string
#print (oddsNBA[6].get(atsNBA,None))

def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

def nbaView():
	print ("********************************NBA SCORES ************************************")

	for m in range(len(oddsNBAFinal)):
		print(nbaScoreAname[m],nbaScoreA[m]," at ",nbaScoreHname[m],nbaScoreH[m] )
		print (periodNba[m])
		print()
		
def nhlView():

	print ("********************************NHL SCORES ************************************")

	for m in range(nhlGames):
		print(nhlScoreHname[m],nhlScoreH[m]," at ",nhlScoreAname[m],nhlScoreA[m] )
		print(periodNhl[m])
		print()

def nbaLinesSelection():
	for n in range(len(oddsNBA)):
		print ( "Pick: (1) for " ,spreadLines.keys() )
		print ( "Pick: (2) for " , spreadLines.keys())
		print ()
		print ( "Pick: (3) for Over: " , oddsNBA[n][ouNBA] )
		print ( "Pick: (4) for Under: " , oddsNBA[n][ouNBA] )
		print ()

def parsingValuesNBA():
	
	for n in range(len(oddsNBA)):
		#temp variables and some string manipulation from json
		tempDate = oddsNBA[n][dateGame]
		tempDate = tempDate[4:12]
		tempOdds = oddsNBA[n]['atsFavoredTeamAbbrv']
		now = datetime.datetime.now().strftime("%Y%m%d")

		#Separate today and tomorrow lines and adjusting some spread underdog *see json*
		if ( tempDate == now):

			stackNamesNBAToday.append(oddsNBA[n][stcAway])
			stackNamesNBAToday.append(oddsNBA[n][stcHome])

			stackNBATotal.append(oddsNBA[n][ouNBA])
			stackNBASeo.append(oddsNBA[n][seoNBA])
				
			if (tempOdds == oddsNBA[n][stcAway]):#COMEBACK
				#nbaLines[tempOdds] = oddsNBA[n][atsNBA]
				stackNBASpreadToday.append( num (oddsNBA[n][atsNBA]))
				stackNBASpreadToday.append( num (oddsNBA[n][atsNBA]) *-1)

			else:
				stackNBASpreadToday.append( num( oddsNBA[n][atsNBA] )*-1)
				stackNBASpreadToday.append( num (oddsNBA[n][atsNBA]) )

		else :
			stackNamesNBATomorrow.append(oddsNBA[n][awayNBA])
			stackNamesNBATomorrow.append(oddsNBA[n][homeNBA])

			if (tempOdds == oddsNBA[n][stcAway]):
				stackNBASpreadTomorrow.append( num (oddsNBA[n][atsNBA]))
				stackNBASpreadTomorrow.append( num (oddsNBA[n][atsNBA]) *-1)

			else:
				stackNBASpreadTomorrow.append( num( oddsNBA[n][atsNBA] )*-1)
				stackNBASpreadTomorrow.append( num (oddsNBA[n][atsNBA]) )

	
def nbaLinesS():


	for n in range(len(oddsNBA)):

		tempDate = oddsNBA[n][dateGame]
		tempDate = tempDate[4:12]
		tempOdds = oddsNBA[n]['atsFavoredTeamAbbrv']
		now = datetime.datetime.now().strftime("%Y%m%d")

		#if ( tempDate == now):
		nbaLines.append(tempOdds)
		nbaLines.append(oddsNBA[n][atsNBA])


	print ("her!!!!!e")
	print (nbaLines)





def parsingValuesNHL():#parameter leng?

	for n in range(len(oddsNHL)):

		#temp variables and some string manipulation from json
		tempDate = oddsNHL[n][dateGame]
		tempDate = tempDate[4:12]
		tempOdds = oddsNHL[n]['atsFavoredTeamAbbrv']
		now = datetime.datetime.now().strftime("%Y%m%d")

		#Separate today and tomorrow lines and adjusting some spread underdog *see json*
		if (tempDate == now):

			stackNamesNHLToday.append(oddsNHL[n][stcAway])
			stackNamesNHLToday.append(oddsNHL[n][stcHome])

			stackNHLTotal.append(oddsNHL[n][ouNHL])
			stackNHLSeo.append(oddsNHL[n][seoNHL])

			if (tempOdds == oddsNHL[n][stcAway]):#COMEBACK
				stackNHLSpreadToday.append( num (oddsNHL[n][atsNHL]))
				stackNHLSpreadToday.append( num (oddsNHL[n][atsNHL]) *-1)
			else:
				stackNHLSpreadToday.append( num( oddsNHL[n][atsNHL] )*-1)
				stackNHLSpreadToday.append( num (oddsNHL[n][atsNHL]) )
		else :
			stackNamesNHLTomorrow.append(oddsNHL[n][awayNHL])
			stackNamesNHLTomorrow.append(oddsNHL[n][homeNHL])

			if (tempOdds == oddsNHL[n][stcAway]):
				stackNHLSpreadTomorrow.append( num (oddsNHL[n][atsNHL]))
				stackNHLSpreadTomorrow.append( num (oddsNHL[n][atsNHL]) *-1)
			else:
				stackNHLSpreadTomorrow.append( num( oddsNHL[n][atsNHL] )*-1)
				stackNHLSpreadTomorrow.append( num (oddsNHL[n][atsNHL]) )

	print(stackNamesNHLToday)
	print(stackNHLTotal)
	print(stackNHLSeo)
	print(stackNHLSpreadToday)

def parsingScoreNBA():

	for n in range(len(oddsNBAFinal)):#comeback

		nbaScoreAname.append(oddsNBAFinal[n]['v']['tc'])
		nbaScoreA.append(oddsNBAFinal[n]['v']['s'])

		nbaScoreHname.append(oddsNBAFinal[n]['h']['tc'])
		nbaScoreH.append(oddsNBAFinal[n]['h']['s'])

		periodNba.append(oddsNBAFinal[n]['stt'])

def parsingScoreNHL():

	for n in range(nhlGames):
		away = configNHLFinal['dates'][0]['games'][n]['teams']['away']
		home = configNHLFinal['dates'][0]['games'][n]['teams']['home']
		periodNhl.append(configNHLFinal['dates'][0]['games'][n]['status']['detailedState'])

		
		nhlScoreAname.append(away['team']['name'])
		nhlScoreA.append(away['score'])

		nhlScoreHname.append(home['team']['name'])
		nhlScoreH.append(home['score'])


def sheets():

	for n in range(len(oddsNBAFinal)):#comeback

		away = oddsNBAFinal[n]['v']['ta']
		home = oddsNBAFinal[n]['h']['ta']
		awayF = oddsNBAFinal[n]['v']['s']
		homeF = oddsNBAFinal[n]['h']['s']

		if (oddsNBAFinal[n]['stt'] == 'Final' ):
			print ("Final")
			nbaSheet[oddsNBAFinal[n]['v']['ta']]= oddsNBAFinal[n]['v']['s']
			nbaSheet[oddsNBAFinal[n]['h']['ta']]= oddsNBAFinal[n]['h']['s']

			#if (nbaLines[n] in nbaSheet):
			#	print ('true')

		
	#print (nbaSheet)


parsingValuesNHL()
parsingValuesNBA()
parsingScoreNBA()
parsingScoreNHL()
nbaView()
nhlView()
sheets()
nbaLinesS()

print ("lineass!!!!!")
print (nbaLines)
print ( len(nbaLines))
nbaLinesView()
nhlLinesView()

#nbaLinesSelection()



"""

def streaks():

	#
	#stc or name check json value between moneyline and espn 
	#dic for stc or name ask key and value would be ... -1

	for n in range(len(oddsNBAFinal)):











f = open("dicLines.txt","w")
f.write((str(nbad)))
f = open("dicOU.txt","w")
f.write((str(nbad2)))
f.close

print("What would you like to bet today?")
show lines
store user input 
final result how to? 
time how to ^
final show result and store result txt?
covering? during game?



"""