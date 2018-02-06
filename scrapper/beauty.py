from urllib.request import urlopen
from bs4 import BeautifulSoup

page = 'https://www.covers.com/Sports/nba/PrintSheetHtml?isPrevious=False'
page = urlopen(page)
soup = BeautifulSoup(page,'html.parser')


topTable = soup.find('tr', attrs={'class':'topbord'}) #701


bottomTable = topTable.next_sibling.next_sibling #702
#bottomTeamName = bottomTable.find('td').next_sibling.next_sibling
#topTeamName = topTable.find('td').next_sibling.next_sibling

a= []
b = []
c=[]
home= []
away = []
spreadA= []
spreadH = []
ouA = []
ouH = []


end = True
for i in range(9):



	if ( i < 1):
		a.append(topTable)
		b.append(bottomTable)
		c.append(topTable.find('td').next_sibling.next_sibling)

		
	else :
		
		topTable = bottomTable.next_sibling.next_sibling
		bottomTable = topTable.next_sibling.next_sibling
		a.append(topTable)
		b.append(bottomTable)
		c.append(topTable.find('td').next_sibling.next_sibling)




for i in range(len(a) -1):


	home.append(a[i].contents[3].string)
	away.append(b[i].contents[3].string)
	print (b[i].contents[3].string)






