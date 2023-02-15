import TermTk as ttk
import punk as pp

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
		#self.BuildSkills()
		#self.BuildNotesBeta()
		
		root.mainloop()

	def BuildBio(self):
		bioFrame = ttk.TTkFrame(parent=self.root.viewport(), title="BIO",
								border=True, pos=(0, 0), size=(49, 4))

		ttk.TTkLabel(parent=bioFrame, text="[Handle:", pos=(0, 0), size=(8, 1))
		self.handle = ttk.TTkLineEdit(parent=bioFrame, text=self.punk.handle,
									  pos=(8, 0), size=(12, 1))
		
		ttk.TTkLabel(parent=bioFrame, text="][Role:", pos=(20, 0), size=(7, 1))
		
		self.role = ttk.TTkLineEdit(parent=bioFrame, pos=(27, 0), size=(12, 1), 
									text=self.punk.role)
		
		ttk.TTkLabel(parent=bioFrame, text="][Rep:", pos=(38, 0), size=(6, 1))
		self.rep = ttk.TTkLineEdit(parent=bioFrame, text=self.punk.reputation,
								   pos=(44, 0), size=(2, 1))
		ttk.TTkLabel(parent=bioFrame, text="]", pos=(46, 0), size=(1, 1))

		ttk.TTkLabel(parent=bioFrame, text="[Name:", pos=(0, 1), size=(6, 1))
		self.name = ttk.TTkLineEdit(parent=bioFrame, text=self.punk.firstName + 
									" " + self.punk.lastName, pos=(6, 1), size=(14, 1))

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
		#NOTE:Do we need this variable? We'll find out!
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