from CharacterSheetClass import Charactersheet

class Race(Charactersheet):
	def __init__(self,race, subrace, size, speed, language,
		stren, dex, con, intel, wis, cha, dv):
		super(self,Race).__init__(name = race,strength = stren, dexterity = dex, intelligence = intel, 
			wisdom = wis, charisma = cha)
		self.subrace = subrace
		self.size = size
		self.speed = speed
		self.language.append(language)
		self.darkvision = dv
	
	#getters for the variables 
	def getsubrace(self):
		if self.subrace != 'none':
			return self.subrace
		else:
			return ''
			
	def getsize(self):
		return self.size
	def getspeed(self):
		return self.speed
	def getlanguages(self):
		return self.language
	def getdarkvision(self):
		return self.darkvision

	#setters for variables
	def setspeed(self,speed):
		self.speed = speed
	def setdarkvison(self,darkvision):
		self.darkvision = darkvision
	#manipulation functions
	def addlanguages(self,language):
		self.language.append(language)
