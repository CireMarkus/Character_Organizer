from tkinter import *
from tkinter import ttk
from Classes.characterClass import *
from Classes.skillClass import *
import csv
class CharacterSheet(Frame):

	#function that calculates the characters core modifier
	def cal_modifier(self, score):
		modifier = 0

		if score == 1:
			modifier = -5
		elif score <= 3:
			modifier = -4
		elif score <= 5:
			modifier = -3
		elif score <= 7:
			modifier = -2
		elif score <= 9:
			modifier = -1
		elif score <= 11:
			modifier = 0
		elif score <= 13:
			modifier = 1
		elif score <= 15:
			modifier = 2
		elif score <= 17:
			modifier = 3
		elif score <= 19: 
			modifier = 4
		elif score <= 21:
			modifier = 5
		elif score <= 23:
			modifier = 6
		elif score <= 25:
			modifier = 7
		elif score <= 27:
			modifier = 8
		elif score <= 29:
			modifier = 9
		elif score >= 30:
			modifier = 10

		return '{0:+}'.format(modifier)
	
	#Function that holds the character meta data
	def meta_data(self,parent,player):

		name_Label = ttk.Label(parent, text = 'Name')
		name_Label.grid(column = 1, row = 0, sticky = 'w')
		name_Holder = ttk.Entry(parent)
		name_Holder.insert(0,player.getname())
		name_Holder.grid(column = 2, row = 0, sticky = 'w')

		level_Label = ttk.Label(parent, text = 'Level')
		level_Label.grid(column = 1, row = 1, sticky = 'w')
		level_Holder = ttk.Entry(parent)
		level_Holder.insert(0,player.getlevel())
		level_Holder.grid(column = 2, row = 1, sticky = 'w')

		alignment_Label  = ttk.Label(parent, text = 'Alignment')
		alignment_Label.grid(column = 3, row = 0, sticky = 'w')
		alignment_Holder = ttk.Entry(parent)
		alignment_Holder.insert(0, player.getalignment())
		alignment_Holder.grid(column = 4, row = 0, sticky = 'w')

		exp_Label = ttk.Label(parent, text = 'Exp')
		exp_Label.grid(column = 3, row = 1, sticky = 'w')
		exp_Holder = ttk.Entry(parent)
		exp_Holder.insert(0, player.getexp())
		exp_Holder.grid(column = 4, row = 1, sticky = 'w')

		race_Label = ttk.Label(parent,text = 'Race')
		race_Label.grid(column = 5, row = 0)
		race_Holder = ttk.Entry(parent)
		race_Holder.insert(0, player.getrace().getrace())
		race_Holder.grid(column =6,row = 0)

		class_Label = ttk.Label(parent, text = 'Class')
		class_Label.grid(column = 5, row = 1)
		class_Holder = ttk.Entry(parent)
		class_Holder.insert(0, player.getclass())
		class_Holder.grid(column = 6, row = 1)



	#function that populates the skills frame
	def skills (self,parent,itemList,player):
		skill = []
		k = 0
		for i in range (len(itemList)):
			#creates skills based on the items from the skills file
			skill.append(Skill(name = str(itemList[i])))

		#Function that copies the core score to the skill
		for i in range(len(skill)):
			if skill[i].getskillName() == 'Athletics':
				skill[i].setScore(self.cal_modifier(player.getstrength())) 
			elif skill[i].getskillName() == 'Acrobatics' or	skill[i].getskillName() == 'Sleight of Hand' or skill[i].getskillName() == 'Stealth':
				skill[i].setScore(self.cal_modifier(player.getdexterity()))
			elif skill[i].getskillName() == 'History' or skill[i].getskillName() == 'Nature' or skill[i].getskillName() == 'Arcana' or skill[i].getskillName() == 'Investigation' or skill[i].getskillName() == 'Religion':
				skill[i].setScore(self.cal_modifier(player.getintelligence()))
			elif skill[i].getskillName() == 'Animal Handling' or skill[i].getskillName() == 'Insight' or skill[i].getskillName() == 'Medicine' or skill[i].getskillName() == 'Perception' or skill[i].getskillName() == 'Survival':
				skill[i].setScore(self.cal_modifier(player.getwisdom()))
			elif skill[i].getskillName() == 'Deception' or skill[i].getskillName() == 'Intimidation' or skill[i].getskillName() == 'Performance' or skill[i].getskillName() == 'Persuasion':
				skill[i].setScore(self.cal_modifier(player.getcharisma()))

		#checks to see if the player if proficent in a skill and sets the bonus
		#bool to true so it can be calculated and added to the player's score
		for i in range(len(skill)):
			for j in range(len(player.getskills())):
				if skill[i].getskillName() == player.getskills()[j]:
					skill[i].setProficent(True)

		core = ['(Dex)','(Wis)','(Int)','(Str)','(Cha)','(Int)','(Wis)','(Cha)','(Int)','(Wis)','(Int)','(Wis)','(Cha)','(Cha)','(Int)','(Dex)','(Dex)','(Wis)']

		#populates the for that contains the skills 
		for i in range (0, 1): #Columns 
			for j in range (0,18):
					holder = ttk.Entry(parent, width = 3, justify = 'right')
					ttk.Label(parent, text = skill[k].getskillName()+core[k], relief = RAISED,width = 20).grid(column =i , row =j, sticky = 'w')
					holder.grid(column = i+1, row = j,sticky = 'e')
					if(skill[k].getProficent() == True):
						profscore = int(skill[k].getScore()) + player.getprofbonus()
						holder.insert(0,'{0:+}'.format(profscore))  
					else:
						holder.insert(0, skill[k].getScore())
					k +=1

	#function that hold the characters cores and core modifiers
	def cores(self, parent,player):
		#cores and modifiers 
		#player strength
		str_Label = ttk.Label(parent, text ='Strength').grid(column = 1, row = 0, sticky = 'w')
		str_score = ttk.Entry(parent)
		str_score.insert(0,player.getstrength())
		str_score.grid(column = 2, row = 0)
		#str modifier
		str_mod = ttk.Entry(parent)
		str_mod.insert(0, self.cal_modifier(player.getstrength()))
		str_mod.grid(column = 4, row = 0)

		#player Dexterity
		dex_Label = ttk.Label(parent, text= 'Dexterity').grid(column = 1, row = 2, sticky = 'w')
		dex_score = ttk.Entry(parent)
		dex_score.insert(0, player.getdexterity())
		dex_score.grid(column = 2, row = 2)
		#dex modifier
		dex_mod = ttk.Entry(parent)
		dex_mod.insert(0, self.cal_modifier(player.getdexterity()))
		dex_mod.grid(column = 4, row = 2)

		#player Constitution
		con_Label = ttk.Label(parent, text = 'Constitution').grid(column = 1, row = 4, sticky = 'w')
		con_score = ttk.Entry(parent)
		con_score.insert(0, player.getconstitution())
		con_score.grid(column = 2, row = 4)
		#con modifier
		con_mod = ttk.Entry(parent)
		con_mod.insert(0, self.cal_modifier(player.getconstitution()))
		con_mod.grid(column = 4, row = 4)

		#player Intelligence
		int_Label = ttk.Label(parent, text = 'Intelligence').grid(column = 1, row = 6, sticky = 'w')
		int_score = ttk.Entry(parent)
		int_score.insert(0, player.getintelligence())
		int_score.grid(column = 2, row = 6)
		#int modifier
		int_mod = ttk.Entry(parent)
		int_mod.insert(0, self.cal_modifier(player.getintelligence()))
		int_mod.grid(column = 4, row = 6)

		#player Wisdom
		wis_Label = ttk.Label(parent, text = 'Wisdom').grid(column = 1, row = 8, sticky = 'w')
		wis_score = ttk.Entry(parent)
		wis_score.insert(0, player.getwisdom())
		wis_score.grid(column = 2, row = 8)
		#str modifier
		wis_mod = ttk.Entry(parent)
		wis_mod.insert(0, self.cal_modifier(player.getwisdom()))
		wis_mod.grid(column = 4, row = 8)

		#player Charisma
		cha_Label = ttk.Label(parent, text = 'Charisma').grid(column = 1, row = 10, sticky = 'w')
		cha_score = ttk.Entry(parent)
		cha_score.insert(0, player.getcharisma())
		cha_score.grid(column = 2, row = 10)
		#str modifier
		cha_mod = ttk.Entry(parent)
		cha_mod.insert(0, self.cal_modifier(player.getcharisma()))
		cha_mod.grid(column = 4, row = 10)

	def top_frame_holder(self,parent,player):
		meta_frame = ttk.LabelFrame(parent, text = 'Meta')
		meta_frame.place(x = 0, y = 0, width = parent.winfo_screenwidth(), height = parent.winfo_screenheight())
		self.meta_data(meta_frame, player)

	def left_frame_holder(self, parent,skill_names,player):
		

		# Label Frame that stores the character's core stats
		cores_frame = ttk.LabelFrame(parent, text = 'Cores', height = (parent.winfo_screenheight()/2) , width =(parent.winfo_screenwidth()))
		cores_frame.place(x = 0, y= 0, width = parent.winfo_screenwidth()/4.32 , height = parent.winfo_screenheight()/4)

		#Label frame that stores the character's skills 
		skill_frame = ttk.LabelFrame(parent, text ='Skills', height = (parent.winfo_screenheight()/2), width = (parent.winfo_screenwidth()))
		skill_frame.place(x = cores_frame.winfo_reqwidth()/4.32, y= cores_frame.winfo_reqheight()/2.1)

		#Label and holder that hold the chracters profbonus
		prof_bonus = ttk.Label(parent, text = 'Proficiency\nBonus', justify = 'left')
		prof_bonus.place(x = cores_frame.winfo_reqwidth()/4.25,y=cores_frame.winfo_reqheight()/12)
		prof_bonus_holder = ttk.Entry(parent,width = 3,font = 70, justify = 'center')
		prof_bonus_holder.insert(0,'{0:+}'.format(player.getprofbonus()))
		prof_bonus_holder.place(x=cores_frame.winfo_reqwidth()/3.60,y=cores_frame.winfo_reqheight()/11.5)

		#Cores widgets
		self.cores(cores_frame, player)

		#Skills widgets 
		self.skills(skill_frame,skill_names,player)

	def center_frame_holder(self, parent,player):
		#Holder frames
		above_health = ttk.LabelFrame(parent,text = 'Above health')
		above_health.place(x=0,y=0,width = parent.winfo_screenwidth()/4,height = parent.winfo_screenheight()/8)

		health_frame = ttk.LabelFrame(parent, text = 'Health')
		health_frame.place(x=0,y=parent.winfo_screenheight()/8,width= parent.winfo_screenwidth()/4,height=parent.winfo_screenheight()/4)
		
		#Frame data
		self.health_data(health_frame,player)
		self.above_health_data(above_health,player)

	def right_frame_holder(self, parent,player):
		pass
		#Function that holds the data that is right above hitpoints and hit dice
	def above_health_data(self,parent,player):
		armor_class_Label = ttk.Label(parent, text ='Armor\n Class')
		armor_class_Label.place(relx = .22, rely = 0.60, anchor = 'center')
		armor_class_holder = ttk.Entry(parent,width = 3,font = 70,justify = 'center')
		armor_class_holder.insert(0,player.getarmor()+int(self.cal_modifier(player.getdexterity())))
		armor_class_holder.place(relx = .22, rely = .25, anchor = 'center')

		initiative_label = ttk.Label(parent, text = 'Initiative')
		initiative_label.place(relx = .44, rely = 0.6, anchor = 'center')
		initiative_holder = ttk.Entry(parent,width = 3,font = 70, justify = 'center')
		initiative_holder.insert(0, self.cal_modifier(player.getdexterity()))
		initiative_holder.place(relx = .44, rely = 0.25, anchor = 'center')

		speed_label = ttk.Label(parent, text = 'Speed')
		speed_label.place(relx = .66, rely = 0.6, anchor = 'center')
		speed_holder = ttk.Entry(parent, width = 3,font = 70, justify = 'center')
		speed_holder.insert(0,player.getrace().getspeed())
		speed_holder.place(relx = .66, rely = 0.25, anchor = 'center')

		#Function that holds the characters hitpoints, hit dice, and death saves
	def health_data(self,parent,player):
		pass
		

	def __init__(self, parent,character,controller = None,):
		Frame.__init__(self, parent)
		self.place(width =parent.winfo_screenwidth() , height = parent.winfo_screenheight())
		self.controller =controller 

		self.character = character 		


		#==========
		#resource files 
		#==========
		skill_names_file = open('resources\\skillnames.txt', 'r')


		#==========
		#file manipulation
		#==========

		skill_names = []
		for i in skill_names_file.readlines():skill_names.append(i.rstrip())


		
		

		skill_names_file.close()
		


		#=============
		#Label Frames
		#=============
		top_frame = ttk.LabelFrame(self, text = 'top_frame')
		top_frame.place(x=0, y = 0, width = parent.winfo_screenwidth(), height = parent.winfo_screenheight()/8)

		left_frame = ttk.LabelFrame(self, text = 'left_frame')
		left_frame.place(x=0,y=parent.winfo_screenheight()/8,width = parent.winfo_screenwidth(), height = parent.winfo_screenheight())
		
		center_frame = ttk.LabelFrame(self, text = 'center_frame')
		center_frame.place(x=parent.winfo_screenwidth()/3,y=parent.winfo_screenheight()/8,width = parent.winfo_screenwidth()/3, height = parent.winfo_screenheight())

		right_frame = ttk.LabelFrame(self, text = 'right_frame')
		right_frame.place(x = (parent.winfo_screenwidth()/3)*2, y = parent.winfo_screenheight()/8, width = (parent.winfo_screenwidth()/3)*2, height = parent.winfo_screenheight())
		
		#==============
		#Widgets
		#==============

		#Widget holders
		self.top_frame_holder(top_frame, player)
		self.left_frame_holder(left_frame,skill_names,player)
		self.right_frame_holder(right_frame,player)
		self.center_frame_holder(center_frame, player)

		



win = Tk()
win.geometry('960x540')

races_file = open('resources\\races.csv')
races_reader = csv.reader(races_file,delimiter=',')

level_file = open('resources\\levels.csv')
level_reader = csv.reader(level_file,delimiter=',')

races = []
linecount = 0
for row in races_reader:
	new = []
	if linecount == 0:
		linecount+=1
	else:
		for j in range(12):
			new.append(row[j])
		linecount+=1
		races.append(new)

races_file.close()


levels = []
linecount = 0
for row in level_reader:
	new1 = []
	if linecount == 0:
		linecount+=1
	else:
		for j in range(3):
			new1.append(row[j])
		linecount+=1
		levels.append(new1)

level_file.close()

choosableraces = []
level_range = []

for i in races:
	choosableraces.append(Race(name = i[0], subrace = i[1],size =i[2],speed = i[3], language = i[4], stren = i[5], dex = i[6], con = i[7], intl = i[8], wis = i[9], cha = i[10], dv = i[11]))

for i in levels:
	level_range.append(Level(i[0],i[1],i[2]))


proficent_skills = ['Arcana','Insight','Medicine','Persuasion','Religion']
player = Character( name = 'Eric',alignment = 'Chaotic Evil', level =level_range[4],
	stren = 0,dex=0,con = 0,intel = 0, wis = 0, cha = 0,   
	skills = proficent_skills,
	charRace = choosableraces[11],charClass = 'Cleric')
#player = Character()
character = CharacterSheet(win,player)


win.mainloop()