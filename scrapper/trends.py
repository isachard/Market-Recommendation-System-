from urllib.request import urlopen
from bs4 import BeautifulSoup

page = 'https://www.covers.com/Sports/nba/PrintSheetHtml?isPrevious=False'
page = urlopen(page)
soup = BeautifulSoup(page,'html.parser')

topTable = soup.find('tr', attrs={'class':'topbord'}) #701
bottomTable = topTable.next_sibling.next_sibling #702

a= []
b = []
c=[]
home= []
away = []
spreadA= []
spreadH = []
ouA = []
ouH = []

def tables( top, bot):
	while (bot != None):
		if not a:
			a.append(top)
			b.append(bot)
			c.append(top.find('td').next_sibling.next_sibling)
		else :
			top = bot.next_sibling.next_sibling
			bot = top.next_sibling.next_sibling
			a.append(top)
			b.append(bot)

def stacks():
	for i in range(len(a) -1):
		away.append(a[i].contents[3].text)
		home.append(b[i].contents[3].text)
		spreadA.append(a[i].contents[31].text)
		spreadH.append(b[i].contents[31].text)
		ouA.append(a[i].contents[33].text)
		ouH.append(b[i].contents[33].text)

def printTrends():
	for i in range (len(away)):
		print (away[i].replace('\r', '').replace('\n', '') + spreadA[i].replace('\r', '').replace('\n', '') + ouA[i].replace('\r', '').replace('\n', ''))
		print (home[i].replace('\r', '').replace('\n', '') + spreadH[i].replace('\r', '').replace('\n', '') + ouH[i].replace('\r', '').replace('\n', ''))


tables(topTable,bottomTable)
stacks()
printTrends()












