class Background():
	def __init__(self,name, skill_proficencies, tool_proficencies,
		equipment,personality_traits,ideals,flaws):

		self.name = name
		self.skill_proficencies = skill_proficencies
		self.equipment = equipment
		self.personality_traits = personality_traits
		self.ideals = ideals
		self.flaws = flaws 

	#getters 
	def getname(self):
		return self.name
	def getskill_proficencies(self):
		return self.skill_proficencies
	def getequipment(self):
		return self.equipment
	def getpersonality_traits(self):
		return self.personality_traits
	def getideals(self):
		return self.ideals
	def getflaws(self):
		return self.flaws

	#setters
	def setname(self, name):
		self.name = name 
	def setskill_proficenceis(self,skills):
		self.skill_proficencies = skills
	def setequipment(self,equipment):
		self.equipment = equipmento
	def setpersonality_traits(self,traits):
		self.personality_traits = traits
	def setideals(self, ideals):
		self.ideals = ideals
	def setflaws(self, flaws):
		self.flaws = flaws
