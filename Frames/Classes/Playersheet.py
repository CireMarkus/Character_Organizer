from raceClass import Race
from magicalprofessions import Magicalprofession
from nonmagical import Nonmagical
from ProfessionClass import Profession

class Player(Race):
	"""docstring for Player"""
	def __init__(self,name, level, race, profession, background,strength, 
		dexterity, constitution, intelligence, 
		wisdom, charisma):

		#player core values passed to the race class
		Race.__init__(name = name,strength = strength, dexterity = dexterity, 
			constitution = constitution,intelligencel = intelligence, 
			wisdom = wisdom, charisma = charisma)

		#palyer specific variables
		self.name_of_race = race
		self.name_of_profession = profession
		self.name_of_background = background
		self.level = level

		self.languages = None
		self.proficent_skills = None
		self.weapon_prof = None
		self.armor_prof = None
	
	#getters
	def getrace(self):
		return self.race
	def getprofession(self):
		return self.profession
	def getbackground(self):
		return self.background 
	def getlevel(self):
		return self.level
	def getlanguages(self):
		return self.languages
	def getproficent_skills(self):
		return self.proficent_skills
	def getweapon_prof(self):
		return self.weapon_prof
	def getarmor_prof(self):
		return self.armor_prof

	#setters 
	def setlevel(self, level):
		self.level = level
	def setlanguages(self,languages):
		self.languages = languages
	def setproficent_skills(self,skills):
		self.proficent_skills = skills
	def setweapon_prof(self,weapons):
		self.weapon_prof = weapons
	def setarmor_prof(self,armors):
		self.armor_prof = armors


