import csv
import os

class Charactersheet:


	def __init__(self,name = 'default', strength = 0, dexterity = 0, 
	 constitution = 0, intelligence = 0, wisdom = 0, charisma = 0):
		#meta data
		self.name = name

		#cores 
		self.strength = strength 
		self.dexterity = dexterity
		self.constitution = constitution
		self.intelligence = intelligence 
		self.wisdom = wisdom 
		self.charisma = charisma

	#getters for the class variables

	#meta data getters
	def getname(self):
		return self.name

	#cores data getters
	def getstrength(self):
		return self.strength
	def getdexterity(self):
		return self.dexterity
	def getconstitution(self):
		return self.constitution
	def getintelligence(self):
		return self.intelligence
	def getwisdom(self):
		return self.wisdom
	def getcharisma(self):
		return self.charisma
	




