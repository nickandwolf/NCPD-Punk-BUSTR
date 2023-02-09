'''
JAN2023
Fair warning, this entire thing is fuq'd and long. It'll need to be redone at some point but for now we're aiming for v1.

Not gonna break it into multiple files yet...
'''
import TermTk as ttk
import skills.skills as ss
import characters.punk as cp
import characters.lifepath as cl

from random import randint as r
import os

#Universal Functions
def _textLabelHeight(length, text, tab=8):
	if text == "":
		return 6
	height = tab
	labelText = "	"
	for thing in text.split(" "):
		if "|" in thing:
			height += 2
		elif len(labelText + thing) <= length:
			labelText += thing + " "

		else:
			height += 1
			labelText = thing + " "
	return height

def _splitTextLabel(start, length, frame, text, tab=True, temp=[]):
		#go to index at length. see if it is a space. if not go backwards until there is a space. then clip there. make label, start next part
		posx = start[0]
		posy = start[1]
		ycount = 0
		if tab: labelText = "	"
		else: labelText=""
		for thing in text.split(" "):
			if "|" in thing:
				t = thing.split("|")
				labelText += t[0]
				temp.append(ttk.TTkLabel(parent=frame,
							 pos=(posx, posy + ycount),
							 size=(length, 1),
							 text=labelText))
				ycount += 2
				labelText = "	" + t[1] + " "
			elif len(labelText + thing) <= length:
				labelText += thing + " "
			else:
				temp.append(ttk.TTkLabel(parent=frame,
							 pos=(posx, posy + ycount),
							 size=(length, 1),
							 text=labelText))
				ycount += 1
				labelText = thing + " "
		temp.append(ttk.TTkLabel(parent=frame,
					 pos=(posx, posy + ycount),
					 size=(length, 1),
					 text=labelText))

def _splitText(length,text,tab):
	plot = ""
	templot = ""
	if tab: templot += "	"
	for thing in text.split(" "):
		if "|" in thing:
			t = thing.split("|")
			templot += t[0]
			plot += templot + "\n\n"
			templot = ""
			if tab: templot += "	"
			templot += t[1] + " "
		elif len(templot + thing) <= length:
			templot += thing + " "
		else:
			plot += templot.strip() + "\n"
			templot = thing + " "
	plot += templot[:-1]
	return plot
			
class FullSheet:
	def __init__(self, character=cp.Punk()):
		self.character = character
		cp._InitRoles()
		root = ttk.TTk()
		self.root = ttk.TTkScrollArea(parent=root, size=(97, 25), pos=(0, 0))
		#self.root.setHorizontalScrollBarPolicy(ttk.TTkK.ScrollBarAlwaysOff)
		self.root._horizontalScrollBar.hide()

		self.health = 0  #DEBUG
		self.healthArray = []

		ttk.TTkButton(parent=root,
					  pos=(98, 0),
					  size=(10, 3),
					  text="Resize",
					  border=True).clicked.connect(self.ToggleRoot)
		self.ToggleRoot()  #DEBUG
		self.BuildStats()
		self.BuildHealth()
		self.BuildBio()
		self.BuildDerivedStats()
		self.BuildArmor()
		self.BuildSkills()
		root.mainloop()

	def BuildBio(self):
		bioFrame = ttk.TTkFrame(parent=self.root.viewport(),
								title="BIO",
								border=True,
								pos=(0, 0),
								size=(49, 4))

		ttk.TTkLabel(parent=bioFrame, text="[Handle:", pos=(0, 0), size=(8, 1))
		self.handle = ttk.TTkLineEdit(parent=bioFrame,
									  text=self.character.handle,
									  pos=(8, 0),
									  size=(12, 1))

		ttk.TTkLabel(parent=bioFrame, text="][Role:", pos=(20, 0), size=(7, 1))

		self.role = ttk.TTkLineEdit(parent=bioFrame,
									pos=(27, 0),
									size=(12, 1),
									text=self.character.role)

		ttk.TTkLabel(parent=bioFrame, text="][Rep:", pos=(38, 0), size=(6, 1))
		self.rep = ttk.TTkLineEdit(parent=bioFrame,
								   text=self.character.reputation,
								   pos=(44, 0),
								   size=(2, 1))
		ttk.TTkLabel(parent=bioFrame, text="]", pos=(46, 0), size=(1, 1))

		ttk.TTkLabel(parent=bioFrame, text="[Name:", pos=(0, 1), size=(6, 1))
		self.name = ttk.TTkLineEdit(parent=bioFrame,
									text=self.character.firstName + " " + self.character.lastName,
									pos=(6, 1),
									size=(14, 1))

		ttk.TTkLabel(parent=bioFrame, text="][Age:", pos=(20, 1), size=(6, 1))
		self.age = ttk.TTkLineEdit(parent=bioFrame,
								   text=self.character.age,
								   pos=(26, 1),
								   size=(3, 1))

		ttk.TTkLabel(parent=bioFrame, text="][Pts:", pos=(29, 1), size=(6, 1))
		self.pts = ttk.TTkLabel(parent=bioFrame,
								text=str(self.character.GetTotalStatPoints()),
								pos=(35, 1),
								size=(3, 1),
								inputType=ttk.TTkK.Input_Number)

		ttk.TTkLabel(parent=bioFrame, text="][HL:", pos=(38, 1), size=(5, 1))
		self.humanity = ttk.TTkLineEdit(parent=bioFrame,
										text=self.character.humanity,
										pos=(43, 1),
										size=(3, 1))
		ttk.TTkLabel(parent=bioFrame, text="]", pos=(46, 1), size=(1, 1))

		self.humanity.textEdited.connect(self.HumanityChanged)

	def BuildStats(self):
		statFrame = ttk.TTkFrame(parent=self.root.viewport(),
								 title="STATS",
								 pos=(0, 4),
								 size=(10, 37))

		self.int = ttk.TTkSpinBox(parent=ttk.TTkFrame(parent=statFrame,
													  border=True,
													  title="INT",
													  pos=(0, 0),
													  size=(8, 3)),
								  value=self.character.INT,
								  pos=(1, 0),
								  size=(4, 1))
		self.int.valueChanged.connect(self.StatChanged)

		self.ref = ttk.TTkSpinBox(parent=ttk.TTkFrame(parent=statFrame,
													  border=True,
													  title="REF",
													  pos=(0, 3),
													  size=(8, 3)),
								  value=self.character.REF,
								  pos=(1, 0),
								  size=(4, 1))
		self.ref.valueChanged.connect(self.StatChanged)

		self.currentRef = ttk.TTkSpinBox(parent=ttk.TTkFrame(parent=statFrame,
															 border=True,
															 pos=(2, 5),
															 size=(6, 3)),
										 value=self.character.GetCurrentREF(),
										 pos=(0, 0),
										 size=(4, 1))
		self.tech = ttk.TTkSpinBox(parent=ttk.TTkFrame(parent=statFrame,
													   border=True,
													   title="TECH",
													   pos=(0, 8),
													   size=(8, 3)),
								   value=self.character.TECH,
								   pos=(1, 0),
								   size=(4, 1))
		self.tech.valueChanged.connect(self.StatChanged)

		self.cool = ttk.TTkSpinBox(parent=ttk.TTkFrame(parent=statFrame,
													   border=True,
													   title="COOL",
													   pos=(0, 11),
													   size=(8, 3)),
								   value=self.character.COOL,
								   pos=(1, 0),
								   size=(4, 1))
		self.cool.valueChanged.connect(self.StatChanged)

		self.attr = ttk.TTkSpinBox(parent=ttk.TTkFrame(parent=statFrame,
													   border=True,
													   title="ATTR",
													   pos=(0, 14),
													   size=(8, 3)),
								   value=self.character.ATTR,
								   pos=(1, 0),
								   size=(4, 1))
		self.attr.valueChanged.connect(self.StatChanged)

		self.luck = ttk.TTkSpinBox(parent=ttk.TTkFrame(parent=statFrame,
													   border=True,
													   title="LUCK",
													   pos=(0, 17),
													   size=(8, 3)),
								   value=self.character.LUCK,
								   pos=(1, 0),
								   size=(4, 1))
		self.luck.valueChanged.connect(self.StatChanged)
		self.currentLuck = ttk.TTkSpinBox(parent=ttk.TTkFrame(parent=statFrame,
															  border=True,
															  pos=(2, 19),
															  size=(6, 3)),
										  value=self.character.LUCK,
										  pos=(0, 0),
										  size=(4, 1))
		self.MA = ttk.TTkSpinBox(
			parent=ttk.TTkFrame(parent=statFrame,
								border=True,
								title="MA",
								pos=(0, 22),
								size=(8, 3)),
			value=self.character.MA,
			pos=(1, 0),
			size=(4, 1))  #this is more for the record than for automation
		self.MA.valueChanged.connect(self.StatChanged)
		#NOTE:Do we need this variable? We'll find out!
		self.currentMA = ttk.TTkSpinBox(parent=ttk.TTkFrame(parent=statFrame,
															border=True,
															pos=(2, 24),
															size=(6, 3)),
										value=self.character.GetCurrentMA(),
										pos=(0, 0),
										size=(4, 1))
		self.currentMA.valueChanged.connect(self.ChangeMA)

		self.body = ttk.TTkSpinBox(parent=ttk.TTkFrame(parent=statFrame,
													   border=True,
													   title="BODY",
													   pos=(0, 27),
													   size=(8, 3)),
								   value=self.character.BODY,
								   pos=(1, 0),
								   size=(4, 1))
		self.body.valueChanged.connect(self.ChangeBody)
		self.body.valueChanged.connect(self.StatChanged)

		self.emp = ttk.TTkSpinBox(parent=ttk.TTkFrame(parent=statFrame,
													  border=True,
													  title="EMP",
													  pos=(0, 30),
													  size=(8, 3)),
								  value=self.character.EMP,
								  pos=(1, 0),
								  size=(4, 1))
		self.emp.valueChanged.connect(self.StatChanged)
		self.currentEmp = ttk.TTkSpinBox(parent=ttk.TTkFrame(parent=statFrame,
															 border=True,
															 pos=(2, 32),
															 size=(6, 3)),
										 value=self.character.GetCurrentEMP(),
										 pos=(0, 0),
										 size=(4, 1))

		maFrame = ttk.TTkFrame(parent=self.root.viewport(),
							   pos=(0, 41),
							   size=(10, 5),
							   border=False)

		ttk.TTkLabel(parent=maFrame, text="[RUN:", pos=(2, 0), size=(5, 1))
		self.run = ttk.TTkLabel(parent=maFrame,
								text=str(self.character.GetRun()),
								pos=(7, 0),
								size=(2, 1))
		ttk.TTkLabel(parent=maFrame, text="]", pos=(9, 0), size=(1, 1))

		ttk.TTkLabel(parent=maFrame, text="[LEAP:", pos=(1, 1), size=(6, 1))
		self.leap = ttk.TTkLabel(parent=maFrame,
								 text=str(self.character.GetLeap()),
								 pos=(7, 1),
								 size=(2, 1))
		ttk.TTkLabel(parent=maFrame, text="]", pos=(9, 1), size=(1, 1))

		ttk.TTkLabel(parent=maFrame, text="[SWIM:", pos=(1, 2), size=(6, 1))
		self.swim = ttk.TTkLabel(parent=maFrame,
								text=str(self.character.GetCurrentMA()),
								pos=(7, 2),
								size=(2, 1))
		ttk.TTkLabel(parent=maFrame, text="]", pos=(9, 2), size=(1, 1))

		ttk.TTkLabel(parent=maFrame, text="[HOLD:", pos=(0, 3), size=(7, 1))
		self.carry = ttk.TTkLabel(parent=maFrame,
								text=str(self.character.GetCarryWeight()),
								pos=(6, 3),
								size=(2, 1))
		ttk.TTkLabel(parent=maFrame, text="]", pos=(9, 3), size=(1, 1))

		ttk.TTkLabel(parent=maFrame, text="[LIFT:", pos=(0, 4), size=(6, 1))
		self.lift = ttk.TTkLabel(parent=maFrame,
								text=str(self.character.GetMaxCarryWeight()),
								pos=(6, 4),
								size=(3, 1))
		ttk.TTkLabel(parent=maFrame, text="]", pos=(9, 4), size=(1, 1))

	def BuildDerivedStats(self):
		derivedFrame = ttk.TTkFrame(parent=self.root.viewport(),
								pos=(49, 0),
								size=(40, 4),
								border=False)
		saveFrame = ttk.TTkFrame(parent=derivedFrame,
								pos=(0, 0),
								size=(8, 4),
								title="SAVE")

		gg = str(self.character.GetBodySave(self.body.value(), self.health))
		if int(gg) < 10:
			gg = " " + gg
		self.save = ttk.TTkLabel(parent=saveFrame,
								 text=gg,
								 pos=(0, 0),
								 size=(2, 1))
		ttk.TTkLabel(parent=saveFrame, text="or", pos=(3, 0))
		ttk.TTkLabel(parent=saveFrame, text=" LESS", pos=(0, 1))
		'''self.saveRoll = ttk.TTkButton(parent=saveFrame,#Button keeps clicking, no clue why
					  border=False,#whatever, fuck this for now
					  text="ROLL",
					  pos=(0, 1),
					  size=(6, 1))
		self.saveRoll.clicked.connect(self.MakeBodySave(self.body.value()))'''

		btmFrame = ttk.TTkFrame(parent=derivedFrame,
								pos=(8, 1),
								title="BTM",
								size=(8, 3))
		self.BTM = ttk.TTkLabel(parent=btmFrame,
								text=self.character.GetBTM(self.body.value()),
								pos=(2, 0),
								size=(2, 1))

		dmgFrame = ttk.TTkFrame(parent=derivedFrame,
								pos=(16, 1),
								title="DMG+",
								size=(8, 3))
		self.DMG = ttk.TTkLabel(parent=dmgFrame,
								text=self.character.GetDamageBonus(
									self.body.value()),
								pos=(2, 0),
								size=(2, 1))

		healFrame = ttk.TTkFrame(parent=derivedFrame,
								 pos=(24, 0),
								 title="HEAL",
								 size=(8, 4))
		ttk.TTkLabel(parent=healFrame, text="+", pos=(1, 0), size=(1, 0))
		self.gotMedTech = ttk.TTkCheckbox(parent=healFrame,
										  text="🩺",
										  pos=(0, 1),
										  size=(5, 1))
		self.healRate = ttk.TTkLabel(
			parent=healFrame,
			text=str(self.character.GetHealRate(self.gotMedTech.checkState())),
			pos=(2, 0),
			size=(2, 1))
		self.gotMedTech.clicked.connect(self.GotADoc)

	def BuildArmor(self):
		armorFrame = ttk.TTkFrame(parent=self.root.viewport(),
								  pos=(10, 4),
								  size=(72, 4),
								  title="ARMOR")

		self.headSP = ttk.TTkSpinBox(parent=ttk.TTkFrame(parent=armorFrame,
														 pos=(0, 0),
														 size=(10, 3),
														 title="Head 1"),
									 pos=(2, 0),
									 size=(4, 1))

		self.torsoSP = ttk.TTkSpinBox(parent=ttk.TTkFrame(parent=armorFrame,
														  pos=(10, 0),
														  size=(13, 3),
														  title="Torso 2-4"),
									  pos=(4, 0),
									  size=(4, 1))
		#right arm
		self.RArmSP = ttk.TTkSpinBox(parent=ttk.TTkFrame(parent=armorFrame,
														 pos=(23, 0),
														 size=(11, 3),
														 title="R.Arm 5"),
									 pos=(3, 0),
									 size=(4, 1))
		#left arm
		self.LArmSP = ttk.TTkSpinBox(parent=ttk.TTkFrame(parent=armorFrame,
														 pos=(34, 0),
														 size=(11, 3),
														 title="L.Arm 6"),
									 pos=(3, 0),
									 size=(4, 1))
		#right leg
		self.RLegSP = ttk.TTkSpinBox(parent=ttk.TTkFrame(parent=armorFrame,
														 pos=(45, 0),
														 size=(13, 3),
														 title="R.Leg 7-8"),
									 pos=(3, 0),
									 size=(4, 1))
		#left leg
		self.LLegSP = ttk.TTkSpinBox(parent=ttk.TTkFrame(parent=armorFrame,
														 pos=(57, 0),
														 size=(13, 3),
														 title="L.Leg 9-0"),
									 pos=(3, 0),
									 size=(4, 1))

	def BuildHealth(self):
		def stackHP(frame):
			posX = 0
			for x in range(4):
				bs = ttk.TTkCheckbox(parent=frame, pos=(posX, 0), size=(3, 1))
				bs.clicked.connect(self.CalcHP)

				self.healthArray.append(bs)
				posX += 3

		hpFrame = ttk.TTkFrame(parent=self.root.viewport(),
							   pos=(10, 8),
							   size=(72, 8),
							   title="HEALTH")

		lightHPFrame = ttk.TTkFrame(parent=hpFrame,
									pos=(0, 0),
									size=(14, 3),
									title="Light -0")
		stackHP(lightHPFrame)
		seriousHPFrame = ttk.TTkFrame(parent=hpFrame,
									  pos=(14, 0),
									  size=(14, 3),
									  title="Serious -1")
		stackHP(seriousHPFrame)
		critialHPFrame = ttk.TTkFrame(parent=hpFrame,
									  pos=(28, 0),
									  size=(14, 3),
									  title="Crit. -2")
		stackHP(critialHPFrame)
		mortal0HPFrame = ttk.TTkFrame(parent=hpFrame,
									  pos=(42, 0),
									  size=(14, 3),
									  title="Mortal0 -3")
		stackHP(mortal0HPFrame)
		mortal1HPFrame = ttk.TTkFrame(parent=hpFrame,
									  pos=(56, 0),
									  size=(14, 3),
									  title="Mortal1 -4")
		stackHP(mortal1HPFrame)
		mortal2HPFrame = ttk.TTkFrame(parent=hpFrame,
									  pos=(0, 3),
									  size=(14, 3),
									  title="Mortal2 -5")
		stackHP(mortal2HPFrame)
		mortal3HPFrame = ttk.TTkFrame(parent=hpFrame,
									  pos=(14, 3),
									  size=(14, 3),
									  title="Mortal3 -6")
		stackHP(mortal3HPFrame)
		mortal4HPFrame = ttk.TTkFrame(parent=hpFrame,
									  pos=(28, 3),
									  size=(14, 3),
									  title="Mortal4 -7")
		stackHP(mortal4HPFrame)
		mortal5HPFrame = ttk.TTkFrame(parent=hpFrame,
									  pos=(42, 3),
									  size=(14, 3),
									  title="Mortal5 -8")
		stackHP(mortal5HPFrame)
		mortal6HPFrame = ttk.TTkFrame(parent=hpFrame,
									  pos=(56, 3),
									  size=(14, 3),
									  title="Mortal6 -9")
		stackHP(mortal6HPFrame)

	def BuildSkills(self):
		skillFrame = ttk.TTkFrame(parent=self.root.viewport(),
								  pos=(10, 16),
								  size=(38, 25),
								  title="SKILLS")
		skillScroll = ttk.TTkScrollArea(parent=skillFrame,
										size=(36, 23),
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

		def _dynamicSkills(frame, list):
			skillRowSize = 0
			for thing in list:
				row = 22 - len(thing.name)
				dots = "." * row
				ttk.TTkLabel(parent=frame,
							 pos=(5 + len(thing.name), skillRowSize),
							 text=dots)  #.menuButtonClicked.connect(_test)
				thing.check = ttk.TTkCheckbox(parent=frame,
											  pos=(0, skillRowSize),
											  size=(3, 1))
				thing.button = ttk.TTkButton(parent=frame,
											 pos=(3, skillRowSize),
											 text=thing.name)
				thing.spin = ttk.TTkLabel(parent=frame,
										  pos=(27, skillRowSize),
										  size=(2, 1),
										  text=str(thing.level))
				thing.button.clicked.connect(
					lambda btn=thing: _skillButtonPull(btn))
				ttk.TTkButton(parent=frame, pos=(29, skillRowSize),
							  text="🎲").clicked.connect(
								  lambda btn=thing: self._rollSkillDice(btn))
				skillRowSize += 1

		#SPECIAL ROLE SKILLS
		specSkillFrame = ttk.TTkFrame(parent=skillScroll.viewport(),
									  pos=(0, 0),
									  size=(35, 2 + len(ss.specSkillList)),
									  title="ROLES")
		frameRowSize = 2 + len(ss.specSkillList)
		_dynamicSkills(specSkillFrame, ss.specSkillList)

		#ATTR
		attrSkillFrame = ttk.TTkFrame(parent=skillScroll.viewport(),
									  pos=(0, frameRowSize),
									  size=(35, 2 + len(ss.attrSkillList)),
									  title="ATTR")
		frameRowSize += 2 + len(ss.attrSkillList)
		_dynamicSkills(attrSkillFrame, ss.attrSkillList)

		#BODY
		bodySkillFrame = ttk.TTkFrame(parent=skillScroll.viewport(),
									  pos=(0, frameRowSize),
									  size=(35, 2 + len(ss.bodySkillList)),
									  title="BODY")
		frameRowSize += 2 + len(ss.bodySkillList)
		_dynamicSkills(bodySkillFrame, ss.bodySkillList)

		#COOL
		coolSkillFrame = ttk.TTkFrame(parent=skillScroll.viewport(),
									  pos=(0, frameRowSize),
									  size=(35, 2 + len(ss.coolSkillList)),
									  title="COOL")
		frameRowSize += 2 + len(ss.coolSkillList)
		_dynamicSkills(coolSkillFrame, ss.coolSkillList)

		#EMP
		empSkillFrame = ttk.TTkFrame(parent=skillScroll.viewport(),
									 pos=(0, frameRowSize),
									 size=(35, 2 + len(ss.empSkillList)),
									 title="EMP")
		frameRowSize += 2 + len(ss.empSkillList)
		_dynamicSkills(empSkillFrame, ss.empSkillList)

		#INT
		intSkillFrame = ttk.TTkFrame(parent=skillScroll.viewport(),
									 pos=(0, frameRowSize),
									 size=(35, 2 + len(ss.intSkillList)),
									 title="INT")
		frameRowSize += 2 + len(ss.intSkillList)
		_dynamicSkills(intSkillFrame, ss.intSkillList)

		#REF
		refSkillFrame = ttk.TTkFrame(parent=skillScroll.viewport(),
									 pos=(0, frameRowSize),
									 size=(35, 2 + len(ss.refSkillList)),
									 title="REF")
		frameRowSize += 2 + len(ss.refSkillList)
		_dynamicSkills(refSkillFrame, ss.refSkillList)

		#TECH
		techSkillFrame = ttk.TTkFrame(parent=skillScroll.viewport(),
									  pos=(0, frameRowSize),
									  size=(35, 2 + len(ss.techSkillList)),
									  title="TECH")

		_dynamicSkills(techSkillFrame, ss.techSkillList)

		def _skillButtonPull(btn):
			skillPopWin = ttk.TTkWindow(
				parent=self.root.viewport(),
				pos=(4, 4),
				size=(38, _textLabelHeight(36, btn.description)),
				title=btn.name + " " + btn.reference,
				border=True)
			desc = ""
			skillStat = self.GetStat(btn.stat)
			if btn.check.checkState(): desc += "[X] "
			else: desc += "[ ] "
			if btn.special: desc += "ROLE/" + btn.stat + " : "
			else: desc += btn.stat + " : "

			desc += "d10 + " + str(skillStat) + " + " + str(btn.level)
			ttk.TTkLabel(parent=skillPopWin, pos=(0, 0), text=desc)
			ttk.TTkButton(parent=skillPopWin, pos=(30, 0),
						  text="ROLL").clicked.connect(
							  lambda btn=btn: self._rollSkillDice(btn))

			desc = ""
			cost = 0
			if btn.level < 1:
				cost = 1
			else:
				cost = btn.level
			desc += "	Costs: " + str(
				cost * btn.cost) + " IP (" + str(cost) + " x " + str(
					btn.cost) + ")"
			ttk.TTkLabel(parent=skillPopWin, pos=(0, 1), text=desc)
			ttk.TTkButton(parent=skillPopWin, pos=(30, 1), text="BUY")
			_splitTextLabel([0, 3], 36, skillPopWin, btn.description)
			skillPopWin.raiseWidget()

	

	def GetStat(self, stat):
		if stat == "INT":
			return self.int.value()
		elif stat == "REF":
			return self.currentRef.value()
		elif stat == "TECH":
			return self.tech.value()
		elif stat == "COOL":
			return self.cool.value()
		elif stat == "ATTR":
			return self.attr.value()
		elif stat == "LUCK":
			return self.luck.value()
		elif stat == "MA":
			return self.currentMA.value()
		elif stat == "BODY":
			return self.body.value()
		elif stat == "EMP":
			return self.currentEmp.value()
		return 0

	

	def _rollSkillDice(self, btn):  #TODO, ADD ABILITY TO USE LUCK
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

	def CalcHP(self, v=None):
		count = 40
		if v:
			for hp in reversed(self.healthArray):
				if hp.checkState() == 2:
					break
				else:
					count -= 1
			self.health = count

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
			self.health = count

			for i in reversed(range(40)):
				if i >= count:
					self.healthArray[i].setCheckState(0)
				else:
					self.healthArray[i].setCheckState(2)

		self.ChangeBody()

	def GotADoc(self, v=None):
		self.healRate.setText(
			str(self.character.GetHealRate(self.gotMedTech.checkState())))

	def StatChanged(self, v=-1):
		self.pts.setText(
			str(self.attr.value() + self.body.value() + self.cool.value() +
				self.emp.value() + self.int.value() + self.ref.value() +
				self.tech.value() + self.MA.value() + self.luck.value()))

	def HumanityChanged(self, v=-1):
		try:
			v = int(v._text)
		except:
			v = 0
		self.currentEmp.setValue(
			self.character.GetCurrentEMP(int(v), self.emp.value()))

	def ChangeMA(self, v=-1):
		self.run.setText(str(self.character.GetRun(self.currentMA.value())))
		self.leap.setText(str(self.character.GetLeap(self.currentMA.value())))
		self.swim.setText(str(self.character.GetSwim(self.currentMA.value())))

	def ChangeBody(self, v=-1):
		self.carry.setText(
			str(self.character.GetCarryWeight(self.body.value())))
		self.lift.setText(
			str(self.character.GetMaxCarryWeight(self.body.value())))
		gg = str(self.character.GetBodySave(self.body.value(), self.health))

		if int(gg) < 0:
			pass
		elif int(gg) < 10:
			gg = " " + gg

		self.save.setText(gg)
		self.BTM.setText(str(self.character.GetBTM(self.body.value())))
		gg = str(self.character.GetDamageBonus(self.body.value()))
		if int(gg) > -1:
			gg = "+" + gg
		self.DMG.setText(gg)

	def MakeBodySave(self, v=None):  #TODO: make sure to add mods later
		roll = r(1, 10)
		result = ""
		sym = ""
		if roll <= self.character.GetBodySave(self.body.value()):
			result = "STILL KICKIN"
			sym = "✅"
		else:
			result = "DOWN AND OUT"
			sym = "❌"
		popUp = ttk.TTkWindow(parent=self.root.viewport(),
							  title=sym,
							  pos=(40, 4),
							  size=(11, 7),
							  border=True)
		ttk.TTkLabel(parent=popUp, text="d10 = " + str(roll), pos=(0, 0))
		ttk.TTkLabel(parent=popUp, text="--------", pos=(0, 1))
		ttk.TTkLabel(parent=popUp,
					 text="   VS " +
					 str(self.character.GetBodySave(self.body.value())),
					 pos=(0, 2))

	def ToggleRoot(self):
		if self.root.height() > 25: self.root.resize(84, 25)
		else: self.root.resize(84, 100)


class CreateCharacter:
	'''
 	Step1: Biological Information
  	Step2: Family
   	Step3: Life Path
   		Life Path -> provide dropdowns for ethnicity + language
		--rerolls too
 
   	Step4: Stats
	Step5: Role
	Step6: Skills
 	FINAL CHARACTER CHECK
  
 	--Step5: Living Expenses
  	--Step6: Equipment
  	--Step7: Cybernetics
   	FINAL ITEM CHECK
  	'''
	def __init__(self):
		self.r = ttk.TTk()
		self.punk = cp.Punk()
		self.lifepath = cl.LifePath()

		self.alias = None

		ttk.TTkLabel(parent=self.r,
					 text="╔═NCPD Punk B.U.S.T.R. powered by WorldSat═╗",
					 pos=(0, 0))
		ttk.TTkLabel(parent=self.r,
					 text="╟┈┈┈┈┈┈New Perpetrator Inprocessing┈┈┈┈┈┈┈┈╢",
					 pos=(0, 1))

		self.root = ttk.TTkWindow(parent=self.r,
								  pos=(0, 2),
								  size=(44, 15),
								  draggable=False,
								  title="Biography")
		self.root._btnClose.hide()

		self.stage = ttk.TTkFrame(parent=self.root, pos=(31, -1), size=(11, 8))

		self.step1 = ttk.TTkButton(parent=self.stage,
								   checkable=True,
								   checked=True,
								   text="BIO",
								   pos=(0, 0),
								   size=(9, 1))
		self.step1.clicked.connect(lambda: self.ButtonPush(self.step1))
		self.step2 = ttk.TTkButton(parent=self.stage,
								   checkable=True,
								   checked=False,
								   text="FAMILY",
								   pos=(0, 1),
								   size=(9, 1))
		self.step2.clicked.connect(lambda: self.ButtonPush(self.step2))
		self.step3 = ttk.TTkButton(parent=self.stage,
								   checkable=True,
								   checked=False,
								   text="LIFE",
								   pos=(0, 2),
								   size=(9, 1))
		self.step3.clicked.connect(lambda: self.ButtonPush(self.step3))
		self.step4 = ttk.TTkButton(parent=self.stage,
								   checkable=True,
								   checked=False,
								   text="STATS",
								   pos=(0, 3),
								   size=(9, 1))
		self.step4.clicked.connect(lambda: self.ButtonPush(self.step4))
		self.step5 = ttk.TTkButton(parent=self.stage,
								   checkable=True,
								   checked=False,
								   text="ROLE",
								   pos=(0, 4),
								   size=(9, 1))
		self.step5.clicked.connect(lambda: self.ButtonPush(self.step5))
		self.step6 = ttk.TTkButton(parent=self.stage,
								   checkable=True,
								   checked=False,
								   text="SKILLS",
								   pos=(0, 5),
								   size=(9, 1))
		self.step6.clicked.connect(lambda: self.ButtonPush(self.step6))

		#put check mark next to completed steps that are saved
		self.prev = ttk.TTkButton(parent=self.root,
								  text="<PREV",
								  pos=(1, 6),
								  border=True,
								  size=(11, 5))
		self.prev.clicked.connect(self.Prev)

		self.next = ttk.TTkButton(parent=self.root,
								  text="NEXT>",
								  pos=(31, 6),
								  border=True,
								  size=(11, 5))
		self.next.clicked.connect(self.Next)

		self.saveButton = ttk.TTkButton(parent=self.root,
					  text=">SAVE<",
					  pos=(16, 8),
					  border=True,
					  size=(11, 3))
		self.saveButton.clicked.connect(self.Save)

		self.saveStatus = ttk.TTkLabel(parent=self.root,
									   pos=(16, 7),
									   text=" [UNSAVED]",
									   color=ttk.TTkColor.fg("#FF0000"))

		self.widg = []
		##DEBUG##
		#self.Step1()
		self.Step4()
		
		self.r.mainloop()
		#check here

	def Unsaved(self, v=None):
		# Should make this check if something was actually changed <.<
		self.saveStatus._color = ttk.TTkColor.fg("#FF0000")
		self.saveStatus.setText(" [UNSAVED]")

	def Save(self, v=None):
		if self.screen == self.step1:
			self.punk.firstName = str(self.firstNameTE._text)
			self.punk.lastName = str(self.lastNameTE._text)
			self.lifepath.ethnicity = self.ethnicityCB.currentText()
			self.lifepath.language = self.languageCB.currentText()
			self.lifepath.hairstyle = self.hairCB.currentText()
			self.lifepath.clothes = self.clothesCB.currentText()
			self.lifepath.affectation = self.affectCB.currentText()
		elif self.screen == self.step2:
			if self.v == "THE PERP":
				###	there is no easy way to export data yet v---- THIS IS UNTIL THE NEXT RELEASE ----v
				self.lifepath.familyBackground = "".join([str(l) for l in self.te.document()._dataLines])
				self.lifepath.motivations[0] = self.personalityCB.currentText()
				self.lifepath.motivations[1] = self.importantPersonCB.currentText()
				self.lifepath.motivations[2] = self.conceptCB.currentText()
				self.lifepath.motivations[3] = self.socialCB.currentText()
				self.lifepath.motivations[4] = self.importantItemCB.currentText()
			else:
				for a in self.lifepath.knownNPCs:
					if a.name == self.v:
							a.motivations[0] = self.personalityCB.currentText()
							a.motivations[1] = self.importantPersonCB.currentText()
							a.motivations[2] = self.conceptCB.currentText()
							a.motivations[3] = self.socialCB.currentText()
							a.motivations[4] = self.importantItemCB.currentText()
							a.notes = "".join([str(l) for l in self.te.document()._dataLines])
		elif self.screen == self.step3:
			pass
		elif self.screen == self.step4:
			self.punk.INT = self.intSB.value()
			self.punk.REF = self.refSB.value()
			self.punk.TECH = self.techSB.value()
			self.punk.COOL = self.coolSB.value()
			self.punk.ATTR = self.attrSB.value()
			self.punk.LUCK = self.luckSB.value()
			self.punk.MA = self.maSB.value()
			self.punk.BODY = self.bodySB.value()
			self.punk.EMP = self.empSB.value()

		self.saveStatus._color = ttk.TTkColor.fg("#00FF00")
		self.saveStatus.setText(" >[SAVED]<")

	def Prev(self, v=None):
		buttons = [
			self.step1, self.step2, self.step3, self.step4, self.step5,
			self.step6
		]
		temp = None
		for b in buttons:
			if b.isChecked():
				self.ButtonPush(temp)
				return
			else:
				temp = b

	def Next(self, v=None):		
		buttons = [
			self.step1, self.step2, self.step3, self.step4, self.step5,
			self.step6
		]
		flag = False
		for b in buttons:
			if flag:
				self.ButtonPush(b)
				return
			elif b.isChecked():
				flag = True

	def ButtonPush(self, v=None):
		for a in self.widg:
			a.close()
		self.widg = []
			
		buttons = [
			self.step1, self.step2, self.step3, self.step4, self.step5,
			self.step6
		]
		for b in buttons:
			if b != v:
				b.setChecked(False)
			else:
				b.setChecked(True)

		self.prev.setEnabled(True)
		if v == self.step1:
			self.prev.setEnabled(False)
			self.Step1()
		elif v == self.step2:
			self.Step2()
		elif v == self.step3:
			self.Step3()
		elif v == self.step4:
			self.Step4()  #TODO PUT THE OTHERS HERE
		elif v == self.step5:
			self.Step5()
		elif v == self.step6:
			self.Step6()
		
	def MoveButtons(self,v=None):
		self.prev._y = self.root._height - self.prev._height - 4
		
		self.next._y = self.root._height - self.next._height - 4
		self.next._x = self.root._width - self.next._width - 3
		
		self.saveButton._y = self.root._height - self.saveButton._height - 4
		self.saveButton._x = int(self.root._width / 2) - self.saveButton._width + 5
		
		self.saveStatus._y = self.root._height - self.saveStatus._height - 7
		self.saveStatus._x = int(self.root._width / 2) - self.saveStatus._width + 4
		
		self.stage._x = self.root._width - self.stage._width - 2
	
	def Step1(self):
		self.screen = self.step1
		self.root.resize(44,19)
		self.root._title = "Biography"
		self.MoveButtons()
		
		if self.punk.firstName.strip() == "":
			fn = cp.GetFirstNames()
			self.firstNameTE = ttk.TTkLineEdit(parent=self.root,
											   pos=(14, 0),
											   size=(12, 1),
											   text=fn[r(0,
														 len(fn) - 1)])
		else:
			fn = self.punk.firstName
			self.firstNameTE = ttk.TTkLineEdit(parent=self.root,
											   pos=(14, 0),
											   size=(12, 1),
											   text=fn)
		self.widg.append(self.firstNameTE)
		self.widg.append(ttk.TTkLabel(parent=self.root,
					 text="[First Name:",
					 pos=(1, 0),
					 size=(12, 1)))

		self.firstNameTE.textChanged.connect(self.Unsaved)

		self.widg.append(ttk.TTkLabel(parent=self.root, text="]", pos=(26, 0), size=(1, 1)))

		if self.punk.lastName.strip() == "":
			ln = cp.GetLastNames()
			self.lastNameTE = ttk.TTkLineEdit(parent=self.root,
											  pos=(14, 1),
											  size=(12, 1),
											  text=ln[r(0,
														len(ln) - 1)])
		else:
			ln = self.punk.lastName
			self.lastNameTE = ttk.TTkLineEdit(parent=self.root,
											  pos=(14, 1),
											  size=(12, 1),
											  text=ln)
		self.widg.append(self.lastNameTE)
		self.widg.append(ttk.TTkLabel(parent=self.root,
					 text="[Last  Name:",
					 pos=(1, 1),
					 size=(12, 1)))

		self.lastNameTE.textChanged.connect(self.Unsaved)

		self.widg.append(ttk.TTkLabel(parent=self.root, text="]", pos=(26, 1), size=(1, 1)))

		self.widg.append(ttk.TTkLabel(parent=self.root,
					 text="[Ethnicity]",
					 pos=(1, 2),
					 size=(11, 1)))
		self.ethnicityCB = ttk.TTkComboBox(
			parent=self.root,
			pos=(1, 3),
			size=(26, 1),
			list=self.lifepath.GetEthnicityList())
		self.ethnicityCB.setCurrentIndex(
			self.lifepath.GetEthnicityList().index(self.lifepath.ethnicity))
		self.ethnicityCB.currentIndexChanged.connect(self.Unsaved)
		
		self.widg.append(self.ethnicityCB)
		
		self.widg.append(ttk.TTkLabel(parent=self.root,
					 text="[Native Language]",
					 pos=(1, 4),
					 size=(18, 1)))
		self.languageCB = ttk.TTkComboBox(parent=self.root,
										  pos=(1, 5),
										  size=(26, 1),
										  list=self.lifepath.SelectLanguage(
											  self.ethnicityCB.currentText()))
		self.widg.append(self.languageCB)
		if type(self.lifepath.language) == type(list()):
			self.languageCB.setCurrentIndex(
				self.lifepath.SelectLanguage().index(
					self.lifepath.language[0]))
		else:
			self.languageCB.setCurrentIndex(
				self.lifepath.SelectLanguage().index(self.lifepath.language))

		self.languageCB.currentIndexChanged.connect(self.Unsaved)

		self.widg.append(ttk.TTkButton(
			parent=self.root, pos=(27, 0),
			text='🎲'))
		self.widg[-1].clicked.connect(lambda: self.firstNameTE.setText(
				cp.GetFirstNames()[r(0,
									 len(cp.GetFirstNames()) - 1)]))

		self.widg.append(ttk.TTkButton(
			parent=self.root, pos=(27, 1),
			text='🎲'))
		self.widg[-1].clicked.connect(lambda: self.lastNameTE.setText(
				cp.GetLastNames()[r(0,
									len(cp.GetLastNames()) - 1)]))

		def ChangedLanguage(v=None):
			self.languageCB._list = self.lifepath.SelectLanguage(
				self.ethnicityCB.currentText())
			self.languageCB.setCurrentIndex(
				r(0,
				  len(self.languageCB._list) - 1))

		self.ethnicityCB.currentIndexChanged.connect(ChangedLanguage)

		def ChangedEthnicity(v=None):
			self.ethnicityCB.setCurrentIndex(
				self.lifepath.GetEthnicityList().index(
					self.lifepath.Ethnicity()))
			ChangedLanguage()

		def ChangedLanguage(v=None):
			self.languageCB._list = self.lifepath.SelectLanguage(
				self.ethnicityCB.currentText())
			self.languageCB.setCurrentIndex(
				r(0,
				  len(self.languageCB._list) - 1))

		self.widg.append(ttk.TTkButton(parent=self.root, pos=(27, 3),
					  text='🎲'))
		self.widg[-1].clicked.connect(ChangedEthnicity)

		self.widg.append(ttk.TTkButton(
			parent=self.root, pos=(27, 5),
			text='🎲'))
		self.widg[-1].clicked.connect(lambda: self.languageCB.setCurrentIndex(
				r(0,
				  len(self.languageCB._list) - 1)))

		self.widg.append(ttk.TTkLabel(parent=self.root,text="  [Hairstyle:",pos=(1,7)))
		self.hairCB = ttk.TTkComboBox(
			parent=self.root,
			pos=(14, 7),
			size=(23, 1),
			list=self.lifepath.GetHairList())
		self.hairCB.setCurrentIndex(self.lifepath.GetHairList().index(self.lifepath.hairstyle))
		self.hairCB.currentIndexChanged.connect(self.Unsaved)
		
		self.widg.append(ttk.TTkLabel(parent=self.root,text="    [Clothing:",pos=(1,8)))
		self.clothesCB = ttk.TTkComboBox(
			parent=self.root,
			pos=(14, 8),
			size=(23, 1),
			list=self.lifepath.GetClothesList())
		self.clothesCB.setCurrentIndex(self.lifepath.GetClothesList().index(self.lifepath.clothes))
		self.clothesCB.currentIndexChanged.connect(self.Unsaved)
		
		self.widg.append(ttk.TTkLabel(parent=self.root,text="[Affectation:",pos=(1,9)))
		self.affectCB = ttk.TTkComboBox(
			parent=self.root,
			pos=(14, 9),
			size=(23, 1),
			list=self.lifepath.GetAffectationList())
		self.affectCB.setCurrentIndex(self.lifepath.GetAffectationList().index(self.lifepath.affectation))
		self.affectCB.currentIndexChanged.connect(self.Unsaved)

		self.widg.append(self.affectCB)
		self.widg.append(self.clothesCB)
		self.widg.append(self.hairCB)

		self.widg.append(ttk.TTkButton(
			parent=self.root, pos=(37, 7),
			text='🎲'))
		self.widg[-1].clicked.connect(lambda: self.hairCB.setCurrentIndex(
				r(0,
				  len(self.hairCB._list) - 1)))

		self.widg.append(ttk.TTkButton(
			parent=self.root, pos=(37, 8),
			text='🎲'))
		self.widg[-1].clicked.connect(lambda: self.clothesCB.setCurrentIndex(
				r(0,
				  len(self.clothesCB._list) - 1)))

		self.widg.append(ttk.TTkButton(
			parent=self.root, pos=(37, 9),
			text='🎲'))
		self.widg[-1].clicked.connect(lambda: self.affectCB.setCurrentIndex(
				r(0,
				  len(self.affectCB._list) - 1)))

	def Step2(self):
		#self.root.resize(44,_textLabelHeight(15,self.lifepath.familyBackground,10))
		##very nice but not needed here yet
		
		# NEED TO FIX SAVE SYSTEM HERE (WILL ALWAYS SAY UNSAVED)
		######
		self.root.resize(54,21)
		self.root._title = "Psychology/Family"
		self.MoveButtons()
		self.screen = self.step2
		self.prev.setEnabled(True)
		self.te = ttk.TTkTextEdit(parent= (tef:=ttk.TTkFrame(parent=self.root,
						pos=(13,-1),size=(29,8),border=True)),
						document=None,pos=(0,0),size=(27,6))
		self.widg.append(self.te)
		self.widg.append(tef)
		self.te.setReadOnly(False)
		self.te.setLineWrapMode(ttk.TTkK.WidgetWidth)
		self.te.setWordWrapMode(ttk.TTkK.WordWrap)
		self.te.setText(self.lifepath.familyBackground)
		
		self.te.document().contentsChanged.connect(self.Unsaved)
		self.v = "THE PERP"
		def _listCallback(v=None):
			self.v = v
			if v == "THE PERP":
				self.te.setText(self.lifepath.familyBackground)
				self.personalityCB.setCurrentIndex(self.lifepath.GetPersonalityList().index(self.lifepath.motivations[0]))
				self.importantPersonCB.setCurrentIndex(self.lifepath.GetImportantPersonList().index(self.lifepath.motivations[1]))
				self.conceptCB.setCurrentIndex(self.lifepath.GetConceptList().index(self.lifepath.motivations[2]))
				self.socialCB.setCurrentIndex(self.lifepath.GetSocialList().index(self.lifepath.motivations[3]))
				self.importantItemCB.setCurrentIndex(self.lifepath.GetImportantItemList().index(self.lifepath.motivations[4]))
			else:
				self.lw.items()[0].selected = False
				self.lw.items()[0].highlighted = False
			
				for a in self.lifepath.knownNPCs:
					if a.name == v:
							self.personalityCB.setCurrentIndex(self.lifepath.GetPersonalityList().index(a.motivations[0]))
							self.importantPersonCB.setCurrentIndex(self.lifepath.GetImportantPersonList().index(a.motivations[1]))
							self.conceptCB.setCurrentIndex(self.lifepath.GetConceptList().index(a.motivations[2]))
							self.socialCB.setCurrentIndex(self.lifepath.GetSocialList().index(a.motivations[3]))
							self.importantItemCB.setCurrentIndex(self.lifepath.GetImportantItemList().index(a.motivations[4]))
							self.te.setText(a.notes)
							

		self.personalityCB = ttk.TTkComboBox(
			parent=self.root, textAlign=ttk.TTkK.LEFT_ALIGN,
			pos=(13, 7),
			size=(35, 1),
			list=self.lifepath.GetPersonalityList())
		self.personalityCB.setCurrentIndex(self.lifepath.GetPersonalityList().index(self.lifepath.motivations[0]))
		self.personalityCB.currentIndexChanged.connect(self.Unsaved)

		self.importantPersonCB = ttk.TTkComboBox(
			parent=self.root, textAlign=ttk.TTkK.LEFT_ALIGN,
			pos=(15, 8),
			size=(33, 1),
			list=self.lifepath.GetImportantPersonList())
		self.importantPersonCB.setCurrentIndex(self.lifepath.GetImportantPersonList().index(self.lifepath.motivations[1]))
		self.importantPersonCB.currentIndexChanged.connect(self.Unsaved)

		self.conceptCB = ttk.TTkComboBox(
			parent=self.root, textAlign=ttk.TTkK.LEFT_ALIGN,
			pos=(12, 9),
			size=(36, 1),
			list=self.lifepath.GetConceptList())
		self.conceptCB.setCurrentIndex(self.lifepath.GetConceptList().index(self.lifepath.motivations[2]))
		self.conceptCB.currentIndexChanged.connect(self.Unsaved)

		self.socialCB = ttk.TTkComboBox(
			parent=self.root, textAlign=ttk.TTkK.LEFT_ALIGN,
			pos=(16, 10),
			size=(32, 1),
			list=self.lifepath.GetSocialList())
		self.socialCB.setCurrentIndex(self.lifepath.GetSocialList().index(self.lifepath.motivations[3]))
		self.socialCB.currentIndexChanged.connect(self.Unsaved)

		self.importantItemCB = ttk.TTkComboBox(
			parent=self.root, textAlign=ttk.TTkK.LEFT_ALIGN,
			pos=(16, 11),
			size=(32, 1),
			list=self.lifepath.GetImportantItemList())
		self.importantItemCB.setCurrentIndex(self.lifepath.GetImportantItemList().index(self.lifepath.motivations[4]))
		self.importantItemCB.currentIndexChanged.connect(self.Unsaved)

		self.widg.append(self.personalityCB)
		self.widg.append(self.importantPersonCB)
		self.widg.append(self.conceptCB)
		self.widg.append(self.socialCB)
		self.widg.append(self.importantItemCB)
		
		lwf = ttk.TTkFrame(parent=self.root, border=True, pos=(-1,-1), size=(15,8))
		self.lw = ttk.TTkList(parent=lwf,pos=(0,0),size=(13,7),maxWidth=19,minWidth=8)
		self.widg.append(lwf)
		self.widg.append(self.lw)

		self.lw.addItem("THE PERP")

		self.widg.append(ttk.TTkLabel(parent=self.root,text="[Personality:",pos=(0,7)))
		self.widg.append(ttk.TTkLabel(parent=self.root,text="[Valued Person:",pos=(0,8)))
		self.widg.append(ttk.TTkLabel(parent=self.root,text="[Motivation:",pos=(0,9)))
		self.widg.append(ttk.TTkLabel(parent=self.root,text="[Social Outlook:",pos=(0,10)))
		self.widg.append(ttk.TTkLabel(parent=self.root,text="[Important Item:",pos=(0,11)))
		
		self.widg.append(ttk.TTkButton(
			parent=self.root, pos=(48, 7),
			text='🎲'))
		self.widg[-1].clicked.connect(lambda: self.personalityCB.setCurrentIndex(
				r(0,
				  len(self.personalityCB._list) - 1)))

		self.widg.append(ttk.TTkButton(
			parent=self.root, pos=(48, 8),
			text='🎲'))
		self.widg[-1].clicked.connect(lambda: self.importantPersonCB.setCurrentIndex(
				r(0,
				  len(self.importantPersonCB._list) - 1)))

		self.widg.append(ttk.TTkButton(
			parent=self.root, pos=(48, 9),
			text='🎲'))
		self.widg[-1].clicked.connect(lambda: self.conceptCB.setCurrentIndex(
				r(0,
				  len(self.conceptCB._list) - 1)))

		self.widg.append(ttk.TTkButton(
			parent=self.root, pos=(48, 10),
			text='🎲'))
		self.widg[-1].clicked.connect(lambda: self.socialCB.setCurrentIndex(
				r(0,
				  len(self.socialCB._list) - 1)))

		self.widg.append(ttk.TTkButton(
			parent=self.root, pos=(48, 11),
			text='🎲'))
		self.widg[-1].clicked.connect(lambda: self.importantItemCB.setCurrentIndex(
				r(0,
				  len(self.importantItemCB._list) - 1)))
		
		for a in self.lifepath.knownNPCs:
			if a.relation == "family":
				self.lw.addItem(a.name)
		self.lw.textClicked.connect(_listCallback)

		self.lw.items()[0].selected = True
		self.lw.items()[0].highlighted = True
		
	def Step3(self):
		self.screen = self.step3
		self.root.resize(44,19)
		self.root._title = "Life Events"
		self.MoveButtons()
		self.prev.setEnabled(True)

		self.widg.append(ttk.TTkLabel(parent=self.root, text="Not implemented yet!", pos=(4,3)))

		#lwf = ttk.TTkFrame(parent=self.root, border=True, pos=(-1,-1), size=(15,14))
		#self.lw = ttk.TTkList(parent=lwf,pos=(0,0),size=(13,12),maxWidth=19,minWidth=8)
		#self.widg.append(lwf)
		#self.widg.append(self.lw)
		
		#self.lw.addItem("THE PERP")

		#for a in self.lifepath.knownNPCs:
		#	if a.relation == "family":
		#		self.lw.addItem(a.name)
		#self.lw.textClicked.connect(_listCallback)

	def Step4(self):
		self.screen = self.step4
		self.root.resize(44,19)
		self.root._title = "Physical Profile"
		self.MoveButtons()

		pointsL = ttk.TTkFrame(parent=self.root,title="Pts",pos=(0,0),border=True,size=(7,3))
		self.widg.append(pointsL)
		points = ttk.TTkLabel(parent=pointsL, text="0xFF",pos=(1,0))
		self.widg.append(points)

		intSB =  self.punk.INT
		refSB = self.punk.REF
		techSB = self.punk.TECH
		coolSB = self.punk.COOL
		attrSB = self.punk.ATTR
		luckSB = self.punk.LUCK
		maSB = self.punk.MA
		bodySB = self.punk.BODY
		empSB = self.punk.EMP

		
		statDesc = ["Problem solving ability","Dexterity and coodination",
					"Willpower, determination, and suave","Understanding technology",
					"That 'something' which keeps you alive","how purty your mouth is",
					"Movement Allowance, how fast or far you move","Charisma and sympathy, humanity",
				    "Stamina, brawn, constitution"]
		
		_desc = ttk.TTkTextEdit(parent=self.root,document=None,pos=(8,0),size=(23,3))
		_desc.setReadOnly(True)
		_desc.setLineWrapMode(ttk.TTkK.WidgetWidth)
		_desc.setWordWrapMode(ttk.TTkK.WordWrap)
		_desc.setText(" <ERROR:FILE_NOT_FOUND> __INSERT RECORD DATA// ::(0xA21FD8:CORRUPTED)")
		
		self.widg.append(_desc)
		
		_min = 3
		_max = 10
		
		### We'll introduce thresholds later ###
		#self.widg.append(ttk.TTkLabel(parent=self.root, text="Min:",pos=(32,8)))
		#self.widg.append(ttk.TTkLabel(parent=self.root, text="Max:",pos=(32,9)))
		
		#ttk.TTkSpinBox(parent=self.root, value=_min,pos=(37,8),size=(4,1))
		#ttk.TTkSpinBox(parent=self.root, value=_max,pos=(37,9),size=(4,1))

		#threshold = 7
		#self.widg.append(ttk.TTkLabel(parent=self.root,text="Limiting Threshold:"))
				
		
		def _buttonCallback(v=None):
			if v == None:
				return
			_desc.setText(statDesc[v])

		def _countPoints(v=None):
			points.setText(str(self.intSB.value() + self.refSB.value() + self.techSB.value() +
							   self.coolSB.value() + self.attrSB.value() + self.luckSB.value() +
							   self.maSB.value() + self.bodySB.value() + self.empSB.value()))
		
		intF = ttk.TTkFrame(parent=self.root, border=True, title="INT",pos=(0,3),  size=(7,4))
		self.intSB = ttk.TTkSpinBox(parent=intF, minimum=_min, maximum=_max,value=intSB,pos=(1,0),size=(4,1))
		intB = ttk.TTkButton(parent=intF, text="?",pos=(1,1),border=False,size=(3,1))
		self.intSB.valueChanged.connect(_countPoints)
		intB.clicked.connect(lambda : _buttonCallback(0))

		self.widg.append(intF)
		self.widg.append(self.intSB)
		self.widg.append(intB)

		
		refF = ttk.TTkFrame(parent=self.root, border=True, title="REF",pos=(8,3),size=(7,4))
		self.refSB = ttk.TTkSpinBox(parent=refF, minimum=_min, maximum=_max,value=refSB,pos=(1,0),size=(4,1))
		refB = ttk.TTkButton(parent=refF, text="?",pos=(1,1),border=False,size=(3,1))
		self.refSB.valueChanged.connect(_countPoints)
		refB.clicked.connect(lambda : _buttonCallback(1))

		self.widg.append(refF)
		self.widg.append(self.refSB)
		self.widg.append(refB)

		techF = ttk.TTkFrame(parent=self.root, border=True, title="TECH",pos=(16,3),  size=(8,4))
		self.techSB = ttk.TTkSpinBox(parent=techF, minimum=_min, maximum=_max,value=techSB,pos=(1,0),size=(4,1))
		techB = ttk.TTkButton(parent=techF, text="?",pos=(1,1),border=False,size=(3,1))
		self.techSB.valueChanged.connect(_countPoints)
		techB.clicked.connect(lambda : _buttonCallback(3))

		self.widg.append(techF)
		self.widg.append(self.techSB)
		self.widg.append(techB)

		coolF = ttk.TTkFrame(parent=self.root, border=True, title="COOL",pos=(24,3),  size=(8,4))
		self.coolSB = ttk.TTkSpinBox(parent=coolF, minimum=_min, maximum=_max,value=coolSB,pos=(1,0),size=(4,1))
		coolB = ttk.TTkButton(parent=coolF, text="?",pos=(1,1),border=False,size=(3,1))
		self.coolSB.valueChanged.connect(_countPoints)
		coolB.clicked.connect(lambda : _buttonCallback(2))

		self.widg.append(coolF)
		self.widg.append(self.coolSB)
		self.widg.append(coolB)
		
		attrF = ttk.TTkFrame(parent=self.root, border=True, title="ATTR",pos=(0,7), size=(8,4))
		self.attrSB = ttk.TTkSpinBox(parent=attrF, minimum=_min, maximum=_max,value=attrSB,pos=(1,0),size=(4,1))
		attrB = ttk.TTkButton(parent=attrF, text="?",pos=(1,1),border=False,size=(3,1))
		self.attrSB.valueChanged.connect(_countPoints)
		attrB.clicked.connect(lambda : _buttonCallback(5))

		self.widg.append(attrF)
		self.widg.append(self.attrSB)
		self.widg.append(attrB)

		luckF = ttk.TTkFrame(parent=self.root, border=True, title="LUCK",pos=(8,7),  size=(8,4))
		self.luckSB = ttk.TTkSpinBox(parent=luckF, minimum=_min, maximum=_max,value=luckSB,pos=(1,0),size=(4,1))
		luckB = ttk.TTkButton(parent=luckF, text="?",pos=(1,1),border=False,size=(3,1))
		self.luckSB.valueChanged.connect(_countPoints)
		luckB.clicked.connect(lambda : _buttonCallback(4))

		self.widg.append(luckF)
		self.widg.append(self.luckSB)
		self.widg.append(luckB)

		maF = ttk.TTkFrame(parent=self.root, border=True, title="M.A.",pos=(16,7),  size=(8,4))
		self.maSB = ttk.TTkSpinBox(parent=maF, minimum=_min, maximum=_max,value=maSB,pos=(1,0),size=(4,1))
		maB = ttk.TTkButton(parent=maF, text="?",pos=(1,1),border=False,size=(3,1))
		self.maSB.valueChanged.connect(_countPoints)
		maB.clicked.connect(lambda : _buttonCallback(6))

		self.widg.append(maF)
		self.widg.append(self.maSB)
		self.widg.append(maB)

		bodyF = ttk.TTkFrame(parent=self.root, border=True, title="BODY",pos=(24,7),  size=(8,4))
		self.bodySB = ttk.TTkSpinBox(parent=bodyF, minimum=_min, maximum=_max,value=bodySB,pos=(1,0),size=(4,1))
		bodyB = ttk.TTkButton(parent=bodyF, text="?",pos=(1,1),border=False,size=(3,1))
		self.bodySB.valueChanged.connect(_countPoints)
		bodyB.clicked.connect(lambda : _buttonCallback(8))

		self.widg.append(bodyF)
		self.widg.append(self.bodySB)
		self.widg.append(bodyB)

		empF = ttk.TTkFrame(parent=self.root, border=True, title="EMP",pos=(32,7),  size=(7,4))
		self.empSB = ttk.TTkSpinBox(parent=empF, minimum=_min, maximum=_max,value=empSB,pos=(1,0),size=(4,1))
		empB = ttk.TTkButton(parent=empF, text="?",pos=(1,1),border=False,size=(3,1))
		self.empSB.valueChanged.connect(_countPoints)
		empB.clicked.connect(lambda : _buttonCallback(7))

		self.widg.append(empF)
		self.widg.append(self.empSB)
		self.widg.append(empB)

		_countPoints()
		

	def Step5(self):
		pass
	
	def Step6(self):
		# THIS SHIT ALSO NEEDS TO BE FIXED IN THE NEXT PYTERMTK UPDATE
		self.next._text = ttk.TTkString("SHIT")

	def ChangeStep(self, step):
		pass


if __name__ == "__main__":
	pass
