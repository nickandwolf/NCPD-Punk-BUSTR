import TermTk as ttk
import punk as pp
import saveLoadExport as sle
import pytermtk.viewCharacters
import skill as ss
from random import randint as r

class FullSheet:
	def __init__(self, punk=pp.Punk()):
		self.punk = punk
		
		root = ttk.TTk()
		self.root = ttk.TTkScrollArea(parent=root, size=(97, 100), pos=(0, 0))
		self.root._horizontalScrollBar.hide()

		self.healthArray = []
		
		self.BuildStats()
		self.BuildHealth()
		self.BuildBio()
		self.BuildDerivedStats()
		self.BuildArmor()
		self.BuildSkills()
		self.BuildNotesBeta()
		self.SaveLoadExport()
		
		root.mainloop()

	def BuildBio(self): #TODO: Autosave is a mess
		def NameSave(v=""):
			v = str(v)
			if v == "": return

			self.punk.firstName = v.split(" ")[0]
			if " " in v:
				self.punk.lastName = v.split(" ")[1]
			
		def HandleSave(v=""):
			v = str(v)
			self.punk.handle = v
			
		bioFrame = ttk.TTkFrame(parent=self.root.viewport(), title="BIO",
								border=True, pos=(0, 0), size=(49, 4))

		ttk.TTkLabel(parent=bioFrame, text="[Handle:", pos=(0, 0), size=(8, 1))
		self.handle = ttk.TTkLineEdit(parent=bioFrame, text=self.punk.handle,
									  pos=(8, 0), size=(12, 1))
		self.handle.textChanged.connect(HandleSave)
		
		ttk.TTkLabel(parent=bioFrame, text="][Role:", pos=(20, 0), size=(7, 1))
		
		self.role = ttk.TTkLineEdit(parent=bioFrame, pos=(27, 0), size=(12, 1), 
									text=self.punk.role)
		#self.role.textChanged.connect(lambda : self.punk.role = str(self.role._text))
		
		ttk.TTkLabel(parent=bioFrame, text="][Rep:", pos=(38, 0), size=(6, 1))
		self.rep = ttk.TTkLineEdit(parent=bioFrame, text=self.punk.reputation,
								   pos=(44, 0), size=(2, 1))
		ttk.TTkLabel(parent=bioFrame, text="]", pos=(46, 0), size=(1, 1))

		ttk.TTkLabel(parent=bioFrame, text="[Name:", pos=(0, 1), size=(6, 1))
		self.name = ttk.TTkLineEdit(parent=bioFrame, text=(self.punk.firstName + 
									" " + self.punk.lastName).strip(), pos=(6, 1), size=(14, 1))
		self.name.textChanged.connect(NameSave)

		ttk.TTkLabel(parent=bioFrame, text="][Age:", pos=(20, 1), size=(6, 1))
		self.age = ttk.TTkLineEdit(parent=bioFrame, text=self.punk.age, pos=(26, 1),
								   size=(3, 1))

		ttk.TTkLabel(parent=bioFrame, text="][Pts:", pos=(29, 1), size=(6, 1))
		self.pts = ttk.TTkLabel(parent=bioFrame, text=str(self.punk.GetTotalStatPoints()),
								pos=(35, 1), size=(3, 1), inputType=ttk.TTkK.Input_Number)

		ttk.TTkLabel(parent=bioFrame, text="][HL:", pos=(38, 1), size=(5, 1))
		self.humanity = ttk.TTkLineEdit(parent=bioFrame, text=self.punk.humanity,
										pos=(43, 1), size=(3, 1))
		ttk.TTkLabel(parent=bioFrame, text="]", pos=(46, 1), size=(1, 1))

		def HumanityChanged(v=-1):
			try:
				v = int(v._text)
			except:
				v = 0
			self.currentEmp.setValue(self.punk.GetCurrentEMP(int(v), self.punk.EMP))
		self.humanity.textEdited.connect(HumanityChanged)

	def BuildStats(self): #TODO: Clean out unnecessary variables
		def ChangeMA(v=-1):
			self.run.setText(str(self.punk.GetRun()))
			self.leap.setText(str(self.punk.GetLeap()))
			self.swim.setText(str(self.punk.GetSwim()))
		def StatChanged(v=-1):
			self.punk.SetStat(None,[self.attr.value(), self.body.value(), self.cool.value(),
									self.emp.value(), self.int.value(), self.ref.value(),
									self.tech.value(), self.MA.value(), self.luck.value()])
			self.pts.setText(str(self.punk.GetTotalStatPoints()))
		
		statFrame = ttk.TTkFrame(parent=self.root.viewport(), title="STATS", 
								 pos=(0, 4), size=(10, 37))

		self.int = ttk.TTkSpinBox(parent=ttk.TTkFrame(parent=statFrame, border=True,
													  title="INT", pos=(0, 0), size=(8, 3)),
								  value=self.punk.INT, pos=(1, 0), size=(4, 1))
		self.int.valueChanged.connect(StatChanged)

		self.ref = ttk.TTkSpinBox(parent=ttk.TTkFrame(parent=statFrame, border=True,
													  title="REF",  pos=(0, 3), size=(8, 3)),
								  value=self.punk.REF, pos=(1, 0), size=(4, 1))
		self.ref.valueChanged.connect(StatChanged)
		self.currentRef = ttk.TTkSpinBox(parent=ttk.TTkFrame(parent=statFrame, border=True,
															 pos=(2, 5), size=(6, 3)),
										 value=self.punk.GetCurrentREF(), pos=(0, 0),
										 size=(4, 1))
		
		self.tech = ttk.TTkSpinBox(parent=ttk.TTkFrame(parent=statFrame, border=True,
													   title="TECH", pos=(0, 8), size=(8, 3)),
								   value=self.punk.TECH, pos=(1, 0), size=(4, 1))
		self.tech.valueChanged.connect(StatChanged)

		self.cool = ttk.TTkSpinBox(parent=ttk.TTkFrame(parent=statFrame, border=True,
													   title="COOL", pos=(0, 11), size=(8, 3)),
								   value=self.punk.COOL, pos=(1, 0), size=(4, 1))
		self.cool.valueChanged.connect(StatChanged)

		self.attr = ttk.TTkSpinBox(parent=ttk.TTkFrame(parent=statFrame, border=True,
													   title="ATTR", pos=(0, 14), size=(8, 3)),
								   value=self.punk.ATTR, pos=(1, 0), size=(4, 1))
		self.attr.valueChanged.connect(StatChanged)

		self.luck = ttk.TTkSpinBox(parent=ttk.TTkFrame(parent=statFrame, border=True,
													   title="LUCK", pos=(0, 17), size=(8, 3)),
								   value=self.punk.LUCK, pos=(1, 0), size=(4, 1))
		self.luck.valueChanged.connect(StatChanged)
		self.currentLuck = ttk.TTkSpinBox(parent=ttk.TTkFrame(parent=statFrame, border=True,
															  pos=(2, 19), size=(6, 3)),
										  value=self.punk.LUCK, pos=(0, 0), size=(4, 1))
		self.MA = ttk.TTkSpinBox(parent=ttk.TTkFrame(parent=statFrame, border=True, title="MA",
								 pos=(0, 22), size=(8, 3)), value=self.punk.MA, pos=(1, 0),
								 size=(4, 1))  #this is more for the record than for automation
		self.MA.valueChanged.connect(StatChanged)
		 
		self.currentMA = ttk.TTkSpinBox(parent=ttk.TTkFrame(parent=statFrame,border=True,
															pos=(2, 24), size=(6, 3)),
										value=self.punk.GetCurrentMA(), pos=(0, 0),
										size=(4, 1))
		self.currentMA.valueChanged.connect(ChangeMA)

		self.body = ttk.TTkSpinBox(parent=ttk.TTkFrame(parent=statFrame, border=True,
													   title="BODY", pos=(0, 27), size=(8, 3)),
								   value=self.punk.BODY, pos=(1, 0), size=(4, 1))
		self.body.valueChanged.connect(StatChanged)
		self.body.valueChanged.connect(self.ChangeBody)
		

		self.emp = ttk.TTkSpinBox(parent=ttk.TTkFrame(parent=statFrame, border=True,
													  title="EMP", pos=(0, 30), size=(8, 3)),
								  value=self.punk.EMP, pos=(1, 0), size=(4, 1))
		self.emp.valueChanged.connect(StatChanged)
		self.currentEmp = ttk.TTkSpinBox(parent=ttk.TTkFrame(parent=statFrame, border=True,
															 pos=(2, 32), size=(6, 3)),
										 value=self.punk.GetCurrentEMP(), pos=(0, 0),
										 size=(4, 1))

		maFrame = ttk.TTkFrame(parent=self.root.viewport(), pos=(0, 41), size=(10, 5),
							   border=False)

		ttk.TTkLabel(parent=maFrame, text="[RUN:", pos=(2, 0), size=(5, 1))
		self.run = ttk.TTkLabel(parent=maFrame, text=str(self.punk.GetRun()),
								pos=(7, 0), size=(2, 1))
		ttk.TTkLabel(parent=maFrame, text="]", pos=(9, 0), size=(1, 1))

		ttk.TTkLabel(parent=maFrame, text="[LEAP:", pos=(1, 1), size=(6, 1))
		self.leap = ttk.TTkLabel(parent=maFrame, text=str(self.punk.GetLeap()),
								 pos=(7, 1), size=(2, 1))
		ttk.TTkLabel(parent=maFrame, text="]", pos=(9, 1), size=(1, 1))

		ttk.TTkLabel(parent=maFrame, text="[SWIM:", pos=(1, 2), size=(6, 1))
		self.swim = ttk.TTkLabel(parent=maFrame, text=str(self.punk.GetCurrentMA()),
								pos=(7, 2), size=(2, 1))
		ttk.TTkLabel(parent=maFrame, text="]", pos=(9, 2), size=(1, 1))

		ttk.TTkLabel(parent=maFrame, text="[HOLD:", pos=(0, 3), size=(7, 1))
		self.carry = ttk.TTkLabel(parent=maFrame, text=str(self.punk.GetCarryWeight()),
								pos=(6, 3), size=(2, 1))
		ttk.TTkLabel(parent=maFrame, text="]", pos=(9, 3), size=(1, 1))

		ttk.TTkLabel(parent=maFrame, text="[LIFT:", pos=(0, 4), size=(6, 1))
		self.lift = ttk.TTkLabel(parent=maFrame, text=str(self.punk.GetMaxCarryWeight()),
								pos=(6, 4), size=(3, 1))
		ttk.TTkLabel(parent=maFrame, text="]", pos=(9, 4), size=(1, 1))

	def BuildDerivedStats(self):
		derivedFrame = ttk.TTkFrame(parent=self.root.viewport(), pos=(49, 0), size=(40, 4),
								border=False)
		saveFrame = ttk.TTkFrame(parent=derivedFrame, pos=(0, 0), size=(8, 4), title="SAVE")

		def MakeBodySave(v=None):  #TODO: make sure to add mods later
			result = ""
			sym = ""
			roll = self.punk.MakeBodySave()
			if roll[0]:
				result = "STILL KICKIN"
				sym = "✅"
			else:
				result = "DOWN AND OUT"
				sym = "❌"
			popUp = ttk.TTkWindow(parent=self.root.viewport(), title=sym, pos=(40, 4),
								  size=(11, 7), border=True)
			ttk.TTkLabel(parent=popUp, text="d10 = " + str(roll[1]), pos=(0, 0))
			ttk.TTkLabel(parent=popUp, text="--------", pos=(0, 1))
			ttk.TTkLabel(parent=popUp, text="   VS " +
						 str(self.punk.GetBodySave()), pos=(0, 2))
			popUp.raiseWidget()
			
		gg = str(self.punk.GetBodySave(body=None, health=self.punk.health))
		if int(gg) < 10: #some nice formatting
			gg = " " + gg
		self.save = ttk.TTkLabel(parent=saveFrame, text=gg, pos=(1, 0), size=(2, 1))
		self.saveRoll = ttk.TTkButton(parent=saveFrame, border=False, text="ROLL",
					  pos=(0, 1), size=(6, 1))
		self.saveRoll.clicked.connect(MakeBodySave)

		btmFrame = ttk.TTkFrame(parent=derivedFrame, pos=(8, 1), title="BTM",
								size=(8, 3))
		self.BTM = ttk.TTkLabel(parent=btmFrame, text=self.punk.GetBTM(),
								pos=(2, 0), size=(2, 1))

		dmgFrame = ttk.TTkFrame(parent=derivedFrame, pos=(16, 1),
								title="DMG+", size=(8, 3))
		self.DMG = ttk.TTkLabel(parent=dmgFrame, text=self.punk.GetDamageBonus(),
								pos=(2, 0), size=(2, 1))

		def GotADoc(v=None):
			self.healRate.setText(str(self.punk.GetHealRate(gotMedTech.checkState())))
			
		healFrame = ttk.TTkFrame(parent=derivedFrame, pos=(24, 0),
								 title="HEAL", size=(8, 4))
		ttk.TTkLabel(parent=healFrame, text="+", pos=(1, 0), size=(1, 0))
		gotMedTech = ttk.TTkCheckbox(parent=healFrame, text="🩺",
										  pos=(0, 1), size=(5, 1))
		self.healRate = ttk.TTkLabel(parent=healFrame, text=str(
									 self.punk.GetHealRate(
									 gotMedTech.checkState())),
									 pos=(2, 0), size=(2, 1))
		gotMedTech.clicked.connect(GotADoc)
	def BuildArmor(self): #TODO: Link this when combat is implemented
		armorFrame = ttk.TTkFrame(parent=self.root.viewport(), pos=(10, 4),
								  size=(72, 4), title="ARMOR")

		self.headSP = ttk.TTkSpinBox(parent=ttk.TTkFrame(
									 parent=armorFrame, pos=(0, 0),
									 size=(10, 3), title="Head 1"),
									 pos=(2, 0), size=(4, 1))

		self.torsoSP = ttk.TTkSpinBox(parent=ttk.TTkFrame(
									  parent=armorFrame, pos=(10, 0),
									  size=(13, 3), title="Torso 2-4"),
									  pos=(4, 0), size=(4, 1))
		#right arm
		self.RArmSP = ttk.TTkSpinBox(parent=ttk.TTkFrame(
									 parent=armorFrame, pos=(23, 0),
									 size=(11, 3), title="R.Arm 5"),
									 pos=(3, 0), size=(4, 1))
		#left arm
		self.LArmSP = ttk.TTkSpinBox(parent=ttk.TTkFrame(
									 parent=armorFrame, pos=(34, 0),
									 size=(11, 3), title="L.Arm 6"),
									 pos=(3, 0), size=(4, 1))
		#right leg
		self.RLegSP = ttk.TTkSpinBox(parent=ttk.TTkFrame(
									 parent=armorFrame, pos=(45, 0),
									 size=(13, 3), title="R.Leg 7-8"),
									 pos=(3, 0), size=(4, 1))
		#left leg
		self.LLegSP = ttk.TTkSpinBox(parent=ttk.TTkFrame(
									 parent=armorFrame, pos=(57, 0),
									 size=(13, 3), title="L.Leg 9-0"),
									 pos=(3, 0), size=(4, 1))
	def BuildHealth(self):
		def CalcHP(v=None):
			count = 40
			if v:
				for hp in reversed(self.healthArray):
					if hp.checkState() == 2:
						break
					else:
						count -= 1
				self.punk.health = count
	
				for i in range(40):
					if i < count:
						self.healthArray[i].setCheckState(2)
					else:
						self.healthArray[i].setCheckState(0)
			else:
				count = 0
				for hp in self.healthArray:
					if hp.checkState() == 0:
						break
					else:
						count += 1
				self.punk.health = count
	
				for i in reversed(range(40)):
					if i >= count:
						self.healthArray[i].setCheckState(0)
					else:
						self.healthArray[i].setCheckState(2)
			self.ChangeBody()

		def stackHP(frame):
			posX = 0
			for x in range(4):
				bs = ttk.TTkCheckbox(parent=frame, pos=(posX, 0), size=(3, 1))
				bs.clicked.connect(CalcHP)
				self.healthArray.append(bs)
				posX += 3

		hpFrame = ttk.TTkFrame(parent=self.root.viewport(),  pos=(10, 8),
							   size=(72, 8), title="HEALTH")

		lightHPFrame = ttk.TTkFrame(parent=hpFrame, pos=(0, 0),
									size=(14, 3), title="Light -0")
		stackHP(lightHPFrame)
		seriousHPFrame = ttk.TTkFrame(parent=hpFrame, pos=(14, 0),
									  size=(14, 3), title="Serious -1")
		stackHP(seriousHPFrame)
		critialHPFrame = ttk.TTkFrame(parent=hpFrame, pos=(28, 0),
									  size=(14, 3), title="Crit. -2")
		stackHP(critialHPFrame)
		mortal0HPFrame = ttk.TTkFrame(parent=hpFrame, pos=(42, 0),
									  size=(14, 3), title="Mortal0 -3")
		stackHP(mortal0HPFrame)
		mortal1HPFrame = ttk.TTkFrame(parent=hpFrame, pos=(56, 0),
									  size=(14, 3), title="Mortal1 -4")
		stackHP(mortal1HPFrame)
		mortal2HPFrame = ttk.TTkFrame(parent=hpFrame, pos=(0, 3),
									  size=(14, 3), title="Mortal2 -5")
		stackHP(mortal2HPFrame)
		mortal3HPFrame = ttk.TTkFrame(parent=hpFrame, pos=(14, 3),
									  size=(14, 3), title="Mortal3 -6")
		stackHP(mortal3HPFrame)
		mortal4HPFrame = ttk.TTkFrame(parent=hpFrame, pos=(28, 3),
									  size=(14, 3), title="Mortal4 -7")
		stackHP(mortal4HPFrame)
		mortal5HPFrame = ttk.TTkFrame(parent=hpFrame, pos=(42, 3),
									  size=(14, 3), title="Mortal5 -8")
		stackHP(mortal5HPFrame)
		mortal6HPFrame = ttk.TTkFrame(parent=hpFrame, pos=(56, 3),
									  size=(14, 3), title="Mortal6 -9")
		stackHP(mortal6HPFrame)

	def BuildSkills(self): #TODO: This whole thing is super fucked
		'''
  		for saving purposes, punk saves the skill objects as a list of dict
		we have to reconstruct the punk skills to skill objects
		'''
		skillFrame = ttk.TTkFrame(parent=self.root.viewport(),
								  pos=(10, 16),
								  size=(38, 30),
								  title="SKILLS")
		skillScroll = ttk.TTkScrollArea(parent=skillFrame,
										size=(36, 28),
										pos=(0, 0))
		skillScroll._horizontalScrollBar.hide()
		specSkillFrame = ttk.TTkFrame()
		attrSkillFrame = ttk.TTkFrame()
		bodySkillFrame = ttk.TTkFrame()
		coolSkillFrame = ttk.TTkFrame()
		empSkillFrame = ttk.TTkFrame()
		intSkillFrame = ttk.TTkFrame()
		refSkillFrame = ttk.TTkFrame()
		techSkillFrame = ttk.TTkFrame()

		def _rollSkillDice(btn):  #TODO, ADD ABILITY TO USE LUCK
			#TODO Add special abilities like COMBAT SENSE
			roll = r(1, 10)
			popWin = ttk.TTkWindow(
				parent=self.root.viewport(),
				pos=(35, 4),  #TODO make the window appear near the skill
				size=(14, 9),
				title=btn.name + " " + btn.reference,
				border=True)
			ttk.TTkLabel(parent=popWin,
						 text="  d10   " + str(roll),
						 pos=(0, 0),
						 size=(10, 1))
			ttk.TTkLabel(parent=popWin,
						 text=" Stat  +" + str(self.GetStat(btn.stat)),
						 pos=(0, 1),
						 size=(10, 1))
			ttk.TTkLabel(parent=popWin,
						 text="Skill  +" + str(btn.level),
						 pos=(0, 2),
						 size=(10, 1))
			ttk.TTkLabel(parent=popWin,
						 text="------------",
						 pos=(0, 3),
						 size=(12, 1))
			ttk.TTkLabel(parent=popWin,
						 text="	   =" +
						 str(roll + self.GetStat(btn.stat) + btn.level),
						 pos=(0, 4),
						 size=(10, 1))
			popWin.raiseWidget()
		
		def _skillButtonPull(btn):
			skillPopWin = ttk.TTkWindow(
				parent=self.root.viewport(),
				pos=(4, 4),
				size=(38, _textLabelHeight(36, btn['description'])),
				title=btn['name'] + " " + btn['reference'],
				border=True)
			desc = ""
			skillStat = self.GetStat(btn['stat'])
			#if btn.check.checkState(): desc += "[X] "
			#else: desc += "[ ] "
			#if btn.special: desc += "ROLE/" + btn.stat + " : "
			#else: desc += btn.stat + " : "

			desc += "d10 + " + str(skillStat) + " + " + str(btn['level'])
			ttk.TTkLabel(parent=skillPopWin, pos=(0, 0), text=desc)
			ttk.TTkButton(parent=skillPopWin, pos=(30, 0),
						  text="ROLL").clicked.connect(
							  lambda btn=btn: _rollSkillDice(btn))
			desc = ""
			cost = 0
			if btn['level'] < 1:
				cost = 1
			else:
				cost = btn['level']
			desc += "	Costs: " + str(
				cost * btn['cost']) + " IP (" + str(cost) + " x " + str(
					btn['cost']) + ")"
			ttk.TTkLabel(parent=skillPopWin, pos=(0, 1), text=desc)
			ttk.TTkButton(parent=skillPopWin, pos=(30, 1), text="BUY")
			_splitTextLabel([0, 3], 36, skillPopWin, btn['description'])
			skillPopWin.raiseWidget()
		
		def _updateSkill(btn):
			pop = ttk.TTkWindow(parent=self.root.viewport(),pos=(4,4),size=(38,10))
			ttk.TTkLabel(parent=pop,text=type(btn),pos=(0,3))
			ttk.TTkLabel(parent=pop,text=btn,pos=(0,0))
			#if v == "" or skl == None: return
			#for x in self.punk.skills:
			#	if x[name] == v.name:
			#		x[level] = v.level
			
		def _dynamicSkills(frame, stat):
			skillRowSize = 0
			for thing in self.punk.skills:
				if (stat == "SPECIAL" and thing['special'] == 'True') or (thing['stat'] == stat and thing['special'] == ''):
					row = 24 - len(thing['name'])
					dots = "." * row
					
					ttk.TTkLabel(parent=frame,
								 pos=(5 + len(thing['name']), skillRowSize),
								 text=dots)  #.menuButtonClicked.connect(_test)
					check = ttk.TTkCheckbox(parent=frame,
												  pos=(0, skillRowSize),
												  size=(3, 1))
					btton = ttk.TTkButton(parent=frame,
												 pos=(3, skillRowSize),
												 text=thing['name'])
					spin = ttk.TTkSpinBox(parent=frame,
												pos=(29, skillRowSize),
												size=(4, 1),
												value=thing['level'],
												minimum=0, maximum=10)
					
					#spin.valueChanged.connect(lambda btn=thing : _updateSkill(btn))##PROBLEM CHILD
					#btton.clicked.connect(
					#	lambda btn=thing: _skillButtonPull(btn))
					#ttk.TTkButton(parent=frame, pos=(29, skillRowSize),
					#			  text="🎲").clicked.connect(
					#				  lambda btn=thing: _rollSkillDice(name=btn))##TODO: FIX THIS
					skillRowSize += 1
		
		#SPECIAL ROLE SKILLS
		specSkillFrame = ttk.TTkFrame(parent=skillScroll.viewport(),
									  pos=(0, 0),
									  size=(35, 2 + len(ss.specSkillList)),
									  title="ROLES")
		frameRowSize = 2 + len(ss.specSkillList)
		_dynamicSkills(specSkillFrame, "SPECIAL")

		#ATTR
		attrSkillFrame = ttk.TTkFrame(parent=skillScroll.viewport(),
									  pos=(0, frameRowSize),
									  size=(35, 2 + len(ss.attrSkillList)),
									  title="ATTR")
		frameRowSize += 2 + len(ss.attrSkillList)
		_dynamicSkills(attrSkillFrame, "ATTR")

		#BODY
		bodySkillFrame = ttk.TTkFrame(parent=skillScroll.viewport(),
									  pos=(0, frameRowSize),
									  size=(35, 2 + len(ss.bodySkillList)),
									  title="BODY")
		frameRowSize += 2 + len(ss.bodySkillList)
		_dynamicSkills(bodySkillFrame, "BODY")

		#COOL
		coolSkillFrame = ttk.TTkFrame(parent=skillScroll.viewport(),
									  pos=(0, frameRowSize),
									  size=(35, 2 + len(ss.coolSkillList)),
									  title="COOL")
		frameRowSize += 2 + len(ss.coolSkillList)
		_dynamicSkills(coolSkillFrame, "COOL")

		#EMP
		empSkillFrame = ttk.TTkFrame(parent=skillScroll.viewport(),
									 pos=(0, frameRowSize),
									 size=(35, 2 + len(ss.empSkillList)),
									 title="EMP")
		frameRowSize += 2 + len(ss.empSkillList)
		_dynamicSkills(empSkillFrame, "EMP")

		#INT
		intSkillFrame = ttk.TTkFrame(parent=skillScroll.viewport(),
									 pos=(0, frameRowSize),
									 size=(35, 2 + len(ss.intSkillList)),
									 title="INT")
		frameRowSize += 2 + len(ss.intSkillList)
		_dynamicSkills(intSkillFrame, "INT")

		#REF
		refSkillFrame = ttk.TTkFrame(parent=skillScroll.viewport(),
									 pos=(0, frameRowSize),
									 size=(35, 2 + len(ss.refSkillList)),
									 title="REF")
		frameRowSize += 2 + len(ss.refSkillList)
		_dynamicSkills(refSkillFrame, "REF")

		#TECH
		techSkillFrame = ttk.TTkFrame(parent=skillScroll.viewport(),
									  pos=(0, frameRowSize),
									  size=(35, 2 + len(ss.techSkillList)),
									  title="TECH")
		_dynamicSkills(techSkillFrame, "TECH")
			
	def BuildNotesBeta(self):
		notesFrame = ttk.TTkFrame(parent=self.root.viewport(),
								title="NOTES/MISSING STUFF",
								border=True,
								pos=(48, 16),
								size=(34, 30))
		te = ttk.TTkTextEdit(parent= notesFrame,document=None,pos=(0,0),size=(32,28))
		te.setReadOnly(False)
		te.setLineWrapMode(ttk.TTkK.WidgetWidth)
		te.setWordWrapMode(ttk.TTkK.WordWrap)
		te.setText(self.punk.notes)

		def Save():
			self.punk.notes = "".join([str(l) for l in self.te.document()._dataLines])
		
		te.document().contentsChanged.connect(Save)
		
	def ChangeBody(self, v=-1):
		self.carry.setText(str(self.punk.GetCarryWeight()))
		self.lift.setText(str(self.punk.GetMaxCarryWeight()))
		gg = str(self.punk.GetBodySave())

		if int(gg) < 0:
			pass
		elif int(gg) < 10:
			gg = " " + gg

		self.save.setText(gg)
		self.BTM.setText(str(self.punk.GetBTM()))
		gg = str(self.punk.GetDamageBonus())
		if int(gg) > -1:
			gg = "+" + gg
		self.DMG.setText(gg)
	def SaveLoadExport(self): ##THIS IS TEMPORARY UNTIL VIEW CHARACTERS WORKS
		def Save():
			sle.SaveCharacterDB(self.punk,self.punk.handle)
			
		saveFrame = ttk.TTkFrame(parent=self.root.viewport(), border=False, 
								 pos=(0, 46), size=(60, 7))
		saveB = ttk.TTkButton(parent=saveFrame,pos=(0,0),text="SAVE",border=True,size=(10,3))
		saveB.clicked.connect(Save)

		quitB = ttk.TTkButton(parent=saveFrame,pos=(10,0),text="QUIT",border=True,size=(10,3))
		quitB.clicked.connect(pytermtk.viewCharacters.ShowCharacters)

'''
def _dynamicSkills(frame, list):
			skillRowSize = 0
			for thing in list:
				row = 22 - len(thing.name)
				dots = "." * row
				ttk.TTkLabel(parent=frame,
							 pos=(5 + len(thing.name), skillRowSize),
							 text=dots)  #.menuButtonClicked.connect(_test)
				check = ttk.TTkCheckbox(parent=frame,
											  pos=(0, skillRowSize),
											  size=(3, 1))
				btton = ttk.TTkButton(parent=frame,
											 pos=(3, skillRowSize),
											 text=thing.name)
				spin = ttk.TTkSpinBox(parent=frame,
										  	pos=(25, skillRowSize),
										  	size=(4, 1),
										  	value=thing.level,##THIS
										 	minimum=0, maximum=10)
				spin.valueChanged.connect()##PROBLEM CHILD
				btton.clicked.connect(
					lambda btn=thing: _skillButtonPull(btn))
				ttk.TTkButton(parent=frame, pos=(29, skillRowSize),
							  text="🎲").clicked.connect(
								  lambda btn=thing: _rollSkillDice(btn))##TODO: FIX THIS
				skillRowSize += 1
	'''