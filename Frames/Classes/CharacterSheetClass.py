import csv
from levelClass import Level


class Charactersheet:


	def __init__(self,name = 'default', experience = 0, strength = 0, dexterity = 0, 
	 constitution = 0, intelligence = 0, wisdom = 0, charisma = 0):
		self.name = name
		self.xp = experience
		self.level = self.cal_level(self.xp)

		#cores 
		self.strength = strength 
		self.dexterity = dexterity
		self.constitution = constitution
		self.intelligence = intelligence 
		self.wisdom = wisdom 
		self.charisma = charisma
		self.profbonus = self.level.getbonus()



	def cal_level(self, xp):
		level = open('..\\resources\\levels.csv','r')
		level_reader = csv.reader(level,delimiter=',')

		levels_holder = []
		linecount = 0 
		for row in level_reader:
			new = []
			if linecount == 0:
				linecount+=1
			else:
				for j in range(3):
					new.append(row[j])
				linecount+=1
				levels_holder.append(new)
		level.close()

		levels = []
		for i in levels_holder:
			levels.append(Level(i[0],i[1],i[2]))


		for i in range(len(levels)):
			if levels[i].getlevel() != levels[-1].getlevel():
				if xp >= levels[i].getxp() and xp <= levels[i+1].getxp():
					return levels[i]
			elif xp >= levels[-1].getxp():
				return levels[-1]

	def getlevel(self):
		return self.level.getlevel()
	def getprofbon(self):
		return self.profbonus


character = Charactersheet()