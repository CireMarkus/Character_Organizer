from CharacterSheetClass import Charactersheet

class Race(Charactersheet):
	def __init__(self,race = None, subrace = None, size = None, speed = None, language = None,
		strength = None, dexterity = None, constitution = None, intelligence = None, wisdom = None, charisma = None, dv = None):
		super(self,Race).__init__(name = race,strength = stren, dexterity = dex, intelligence = intel, 
			wisdom = wis, charisma = cha)
		self.subrace = subrace
		self.size = size
		self.speed = speed
		self.language.append(language)
		self.darkvision = dv
	
	#getters for the variables 
	def getsubrace(self):
		if self.subrace.lower() != 'none':
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
	def setrace(self,race):
		self.name =race
	def setsize(self,size):
		self.size = size
	def setspeed(self,speed):
		self.speed = speed
	def setdarkvison(self,darkvision):
		self.darkvision = darkvision
	def setlanguages(self,languages):
		self.language = languages
	
	#manipulation functions
	def addlanguages(self,language):
		if language.lower() != 'none':
			self.language.append(language)
		else:
			self.language = 'You must chose your language(s)'