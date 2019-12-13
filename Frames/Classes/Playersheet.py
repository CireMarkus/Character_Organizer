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
		Race.__init__(name = name, strength = strength, dexterity = dexterity, 
			constitution = constitution,intelligencel = intelligence, 
			wisdom = wisdom, charisma = charisma)	
		



