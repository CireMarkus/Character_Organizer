class Profession():
	def __init__(self, name, hit_die, primary_abilities,saving_throws,
	 armor_prof, weapon_prof, level, prof_bonus,class_features):
		
		#holds the name of the class the player can be
		self.name = name
		self.level = level
		self.prof_bonus = prof_bonus
		#Tracks the hit die for the characers health 
		self.hit_die = hit_die

		self.primary_abilities.append(self.datasplitter(primary_abilities))
		self.saving_throws.append(self.datasplitter(saving_throws))

		#holds what armor proficencies the class has.
		self.armor_prof.append(self.datasplitter(armor_prof))
		self.weapon_prof.append(self.datasplitter(weapon_prof))

		self.features.append((self.datasplitter(class_features)))

	#splits multidata into a list
	def datasplitter(self,data):
		newdata = data.strip()
		return newdata.split(',')
		
	#getters 
