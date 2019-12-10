from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


race_table = open('..\\Frames\\resources\\races.csv','a')

driver = webdriver.Chrome('C:\\webdrivers\\chromedriver')
driver.get('http://www.jsigvard.com/dnd/Races.html')

search_box = driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/div/label/input")
search_box.clear()
search_box.send_keys('PHB', Keys.RETURN)




soup = BeautifulSoup(driver.page_source,'html.parser')


driver.close()


table = soup.find('table', attrs = {'id':'example'})

holder = []

for row in table.findAll('tr'):
	for cell in row.findAll('td'):
		holder.append(cell.text)

k = 0
for row in range(15):
	for column in range (15):
		if holder[k] != '':
			race_table.write(holder[k])
		else:
			race_table.write(' ')
			
		race_table.write(',')

		k+=1
	race_table.write('\n')

