class Level:
	def __init__(self,experience=0,level = 0, prof_bonus=0):
		self.level = level 
		self.exp = experience
		self.prof_bonus = prof_bonus
	
	def getlevel(self):
		return int(self.level)
	def getbonus(self):
		return int(self.prof_bonus)
	def getxp(self):
		return int(self.exp)
	
