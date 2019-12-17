from raceClass import Race
from magicalprofessions import Magicalprofession
from nonmagical import Nonmagical
from ProfessionClass import Profession

class Player(Race, Profession):
	"""docstring for Player"""
	def __init__(self,name, level, race, profession, strength, 
		dexterity, constitution, intelligence, 
		wisdom, charisma):

		#player core values passed to the race class
		Race.__init__(name = name,strength = strength, dexterity = dexterity, 
			constitution = constitution,intelligencel = intelligence, 
			wisdom = wisdom, charisma = charisma)
		Profession.__init__(name, hit_die, primary_abilities, saving_throws, armor_prof, weapon_prof, level, prof_bonus, class_features)
		
		self.race = race
		self.profession = profession

	#returns the players selected race
	def getrace(self):
		return self.race
	#returns the players selected profession
	def getprofession(self):
		return self.profession
		