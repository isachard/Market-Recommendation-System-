import urllib.request
import json 
import time


class Today ():

	urllib.request.urlretrieve("https://www.sportsline.com/sportsline-web/service/v1/oddsPageContent?league=mlb&auth=3", "lines.json")

	def __init__(self):
		self.mlbLines = json.loads(open('lines.json').read()) 
		self.mlbAwayName = []
		self.mlbAwayLine = []



	def parsingTodaysGame(self):

		def oddsSize():
			size = len(self.mlbLines['odds'])
			return size

		def todaysDate():
			dt = time.strftime('%Y%m%d')
			return dt

		todaysDate = todaysDate()

		for i in range(oddsSize()):
			gameDate = self.mlbLines['odds'][i]['cbsGameAbbrv'][4:12]

			if ( todaysDate == gameDate) :
				self.mlbAwayName.append(self.mlbLines['odds'][i]['awayTeamName'])
				self.mlbAwayLine.append(self.mlbLines['odds'][i]['ouTotal'])


	def print(self):

		for i in range(len(self.mlbAwayName)):
			print(self.mlbAwayName[i] + " " + self.mlbAwayLine[i])



	def appendToText(self):
		file = open('daily_lines.txt','a')
		file.write( time.strftime('%Y%m%d'))
		for i in range(len(self.mlbAwayName)):
			file.write('\n')
			file.write( self.mlbAwayName[i] + " " + self.mlbAwayLine[i])
		
			




oop = Today()
oop.parsingTodaysGame()
oop.print()
oop.appendToText()
