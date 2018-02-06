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


	away.append(a[i].contents[3].text)
	home.append(b[i].contents[3].text)
	spreadA.append(a[i].contents[31].text)
	spreadH.append(b[i].contents[31].text)
	ouA.append(a[i].contents[33].text)
	ouH.append(b[i].contents[33].text)





print (away[0])
print (spreadA[0])
print (ouA[0])





