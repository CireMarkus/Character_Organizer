from CharacterSheetClass import Charactersheet

class Race(Charactersheet):
	def __init__(self,name, subrace, size, speed, language,
		stren, dex, con, intel, wis, cha, dv):
		super(self,Race).__init__(name = name,strength = stren, dexterity = dex, intelligence = intel, 
			wisdom = wis, charisma = cha)
		self.subrace = subrace
		self.size = size
		self.speed = speed
		self.language.append(language)
		self.darkvision = dv