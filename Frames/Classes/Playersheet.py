from CharacterSheetClass import Charactersheet
from magicalprofessions import Magicalprofession
from nonmagical import Nonmagical

class Player(Charactersheet):
	"""docstring for Player"""
	def __init__(self, arg):
		super(Player, self).__init__()
		self.arg = arg
		
