from ProfessionClass import Profession

class Magicalprofession(Profession):
	def __init__(self,name ='default',hit_die = 0, primary_abilities = ['None'], 
		saving_throws = ['None'],armor_prof = ['None'],weapon_prof = ['None'],
		level = 0, prof_bonus = 0, class_features=['None'],
	  cantrips = 0, first= 0, second = 0, third = 0, fourth = 0, fifth = 0,
		sixth = 0, seventh = 0, eighth = 0, ninth = 0):
		
		super(self,Magicalprofession).__init__(name=name, hit_die = hit_die, saving_throws = saving_throws,
		 armor_prof = armor_prof, weapon_prof = weapon_prof, level = level, prof_bonus = prof_bonus,
		 class_features = class_features)

		self.cantrips = self.slotChecker(cantrips)
		self.firstlvlslots = self.slotChecker(first)
		self.secondlvlslots = self.slotChecker(second)
		self.thirdlvlslots = self.slotChecker(third)
		self.fourthlvlslots = self.slotChecker(fourth)
		self.fifthlvlslots = self.slotChecker(fifth)
		self.sixthlvlslots = self.slotChecker(sixth)
		self.seventhlvlslots = self.slotChecker(seventh)
		self.eighthlvlslots = self.slotChecker(eighth)
		self.ninthlvlslots = self.slotChecker(ninth)

	def slotChecker(self,slot):
		if slot == '-':
			return 0
		else:
			return slot

	#getters
	def getcantrips(self):
		return self.cantrips
	def getfirstlvlslots(self):
		return self.firstlvlslots
	def getsecondlvlslots(self):
		return self.secondlvlslots
	def getthirdlvlslots(self):
		return self.thirdlvlslots
	def getfourthlvlslots(self):
		return self.fourthlvlslots
	def getfifthlvlslots(self):
		return self.fifthlvlslots
	def getsixthlvlslots(self):
		return self.sixthlvlslots
	def getseventhlvlslots(self):
		return self.seventhlvlslots
	def geteighthlvlslots(self):
		return self.eighthlvlslots
	def getninthlvlslots(self):
		return self.ninthlvlslots

	