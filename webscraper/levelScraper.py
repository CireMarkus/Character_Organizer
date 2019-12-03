from bs4 import BeautifulSoup
import requests



advancement_page = requests.get('https://roll20.net/compendium/dnd5e/Character%20Advancement#content')

soup = BeautifulSoup(advancement_page.text,'html.parser')
table=soup.find('table')

holder = []

for row in table.findAll('tr'):
	for cell in row.findAll('th') or row.findAll('td'):
			holder.append(cell.text.replace(',',''))

level_table = open('..\\Frames\\resources\\levels.csv','w')
k = 0
for row in range(20):
	for column in range(3):
		level_table.write(holder[k])
		level_table.write(',')
		k+=1
	level_table.write('\n')

level_table.close()