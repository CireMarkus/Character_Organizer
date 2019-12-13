class Profession():
	def __init__(self, name, hit_die, primary_abilities,saving_throws,
	 armor_prof, weapon_prof, level, prof_bonus,class_features):
		
		#holds the name of the class the player can be
		self.name = name
		self.level = level
		self.prof_bonus = prof_bonus
		#Tracks the hit die for the characers health 
		self.hit_die = hit_die

		self.primary_abilities = self.datasplitter(primary_abilities)
		self.saving_throws = self.datasplitter(saving_throws)

		#holds what armor proficencies the class has.
		self.armor_prof = self.datasplitter(armor_prof)
		self.weapon_prof = self.datasplitter(weapon_prof)

		self.features = self.datasplitter(class_features)

	#splits multidata into a list
	def datasplitter(self,data):
		newdata = data.strip()
		return newdata.split(',')
		
	#getters 
	def getname(self):
		return self.name
	def getlevel(self):
		return self.level
	def getprof_bonus(self):
		return self.prof_bonus
	def gethit_die(self):
		return self.hit_die
	def getprimary_abilities(self):
		return self.primary_abilitites
	def getsaving_throws(self):
		return self.saving_throws
	def getarmor_prof(self):
		return self.armor_prof
	def getweapon_prof(self):
		return self.weapon_prof
	def getfeatures(self):
		return self.features

	#setters
	def setname(self,name):
		self.name = name
	def setlevel(self,level):
		self.level = level
	def setprof_bonus(self,bonus):
		self.prof_bonus = bonus
	def sethit_die(self,die):
		self.hit_die = die
	def setprimary_abilities(self,abilities):
		self.primaryabilities = self.abilities

	#adders
	#adds ablilites or feauture to a class
	def add_armor_prof(self,armor):
		self.armor_prof.append(armor)
	def add_weapon_prof(self,weapon):
		self.weapon_prof.append(weapon)
	def add_feature(self,feature):
		self.features.append(feature)
