from ProfessionClass import Profession

class Nonmagical(Profession):
	"""docstring for nonmagical"""
	def __init__(self,name = 'default',hit_die = 0, primary_abilities = ['None'], 
		saving_throws = ['None'],armor_prof = ['None'],weapon_prof = ['None'],
		level = 0, prof_bonus = 0, class_features=['None'],attack = 0, damage = 0):
		
		super(nonmagical, self).__init__(name = name, hit_die=hit_die, primary_abilities = primary_abilities,
		saving_throws = saving_throws, armor_prof = armor_prof, weapon_prof = weapon_prof,
		level = level, prof_bonus = prof_bonus, class_features = class_features)
		

		self.attack = attack 
		self.damage = damage

	def getattack(self):
		return self.attack
	def getdamage(self):
		return self.damage

		