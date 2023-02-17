from random import randint as r
import skill as ss

class Punk:
	def __init__(self,
	             firstName="",
				 lastName="",
	             handle="",
	             role="",
	             age=0,
	             ATTR=3,
	             BODY=3,
	             COOL=3,
	             EMP=3,
	             INT=3,
	             REF=3,
	             TECH=3,
	             MA=3,
	             LUCK=3,
	             health=0,
	             rep=0,
	             humanity=None,
	             skills=[],
	             inventory=[],
	             cyberware=[],
	             expenses=[],
	             eurobucks=0,
	             income=0,
	             employed=False,
	             lifepath=None,
				 notes=""):
		#Life
		self.firstName = firstName
		self.lastName = lastName
		self.handle = handle
		self.role = role
		self.age = age
		self.lifepath = lifepath

		#Stats
		self.ATTR = ATTR
		self.BODY = BODY
		self.COOL = COOL
		self.EMP = EMP
		self.INT = INT
		self.REF = REF
		self.TECH = TECH
		self.MA = MA
		self.LUCK = LUCK
		self.health = health

		if humanity == None: self.humanity = self.EMP * 10
		else: self.humanity = humanity

		self.reputation = rep
		#if skills == []:
			#ss._skillInit()
			#self.skills = ss.skillList
		#else:
		self.skills = skills

		#Economy
		self.eurobucks = eurobucks
		self.income = income
		self.employed = employed
		self.expenses = expenses

		#Posessions
		self.inventory = inventory
		self.cyberware = cyberware
		self.notes = notes

	def GetTotalStatPoints(self, stats=[]):
		if stats == []:
			return self.ATTR + self.BODY + self.COOL + self.EMP + self.INT + self.REF + self.TECH + self.MA + self.LUCK
		else:
			y = 0
			for x in stats:
				y += int(x)
			return y

	def GetTotalSkillPoints(self):
		pass  #make return all skill points

	def GetTotalCharacterPoints(self):
		pass  #return all points

	def GetCurrentEMP(self, HL=None, emp=None):
		'''
		HL is humanity
		emp is max empathy, not current
		'''
		if HL == None:
			HL = self.humanity
		if emp == None:
			emp = self.EMP

		if int(HL / 10) + 1 > emp:
			return int(HL / 10)
		else:
			return int(HL / 10) + 1

	def GetCurrentMA(self):
		return self.MA  #no idea ho items work yet

	def GetCurrentREF(self):
		return self.REF  #no idea ho items work yet

	def AdjustHumanity(self, amt):
		self.humanity += amt
		if self.humanity < 0:
			print("Lost in the RED")
		elif self.humanity < 20:
			print("One bad day away from tipping")
		elif self.humanity < 30:
			print("You should de-chrome, choombatta")
		elif self.humanity < 40:
			print("Close to Cyberpsycho")

	def GetBodyType(self, body=None):
		if body == None:
			body = self.BODY
		if body < 3:
			return "Very Weak"
		elif body < 5:
			return "Weak"
		elif body < 8:
			return "Average"
		elif body < 10:
			return "Strong"
		elif body < 11:
			return "Very Strong"
		elif body >= 11:
			return "Superhuman"
		else:
			return body

	def GetBTM(self, body=None):
		if body == None:
			body = self.BODY
		bt = self.GetBodyType(body)
		if bt == "Very Weak":
			return 0
		elif bt == "Weak":
			return -1
		elif bt == "Average":
			return -2
		elif bt == "Strong":
			return -3
		elif bt == "Very Strong":
			return -4
		elif bt == "Superhuman":
			return -5
		else:
			return bt

	def GetDamageBonus(self, body=None):
		if body == None:
			body = self.BODY
		bt = self.GetBodyType(body)
		if bt == "Very Weak":
			return -2
		elif bt == "Weak":
			return -1
		elif bt == "Average":
			return 0
		elif bt == "Strong":
			return 1
		elif bt == "Very Strong":
			return 2
		elif bt == "Superhuman":
			if body < 13:
				return 4
			elif body < 15:
				return 6
			else:
				return 8
		else:
			return bt

	def GetHealRate(self, v=None):
		default = 0.5
		if v == None:
			v = 0
		if v == 2:
			default += 0.5
		return default  #cyberpunk + party bullshit

	def GetBodySave(self, body=None, health=None):
		if body == None:
			body = self.BODY
		return body - self.GetBodySaveMod(health)
		#remember scifi bullshit later

	def GetBodySaveMod(self, health=None):
		if health == None:
			health = self.health
		if health < 5:
			return 0
		elif health < 9:
			return 1
		elif health < 13:
			return 2
		elif health < 17:
			return 3
		elif health < 21:
			return 4
		elif health < 25:
			return 5
		elif health < 29:
			return 6
		elif health < 33:
			return 7
		elif health < 37:
			return 8
		elif health < 41:
			return 9
		else:
			return 99

	def GetCarryWeight(self, body=None):
		if body == None:
			body = self.BODY
		return body * 10

	def GetMaxCarryWeight(self, body=None):
		if body == None:
			body = self.BODY
		return body * 40

	def GetRun(self, ma=None):
		if ma == None:
			ma = self.MA
		return ma * 3

	def GetLeap(self, ma=None):
		return int(self.GetRun(ma) / 4)

	def GetSwim(self, ma=None):
		if ma == None:
			ma = self.MA
		return ma  #gotta add cybernetic shit

	def ParseLifeEvents(self):
		for x in self.lifepath.events:
			pass

	def MakeBodySave(self):
		roll = r(1,10)
		if roll <= self.GetBodySave():
			return [True,roll]
		else:
			return [False,roll]

	def SetStat(self,stat=None,improve=None):
		if improve == None:
			pass
		elif type(improve) == type([]):
			self.ATTR = improve[0]
			self.BODY = improve[1]
			self.COOL = improve[2]
			self.EMP = improve[3]
			self.INT = improve[4]
			self.REF = improve[5]
			self.TECH = improve[6]
			self.MA = improve[7]
			self.LUCK= improve[8]
		elif type(stat) == type(""):
			if stat.lower() == "attr":
				self.ATTR = improve
			elif stat.lower() == "body":
				self.BODY = improve
			elif stat.lower() == "cool":
				self.COOL = improve
			elif stat.lower() == "emp":
				self.EMP = improve
			elif stat.lower() == "int":
				self.INT = improve
			elif stat.lower() == "ref":
				self.REF = improve
			elif stat.lower() == "tech":
				self.TECH = improve
			elif stat.lower() == "ma":
				self.MA = improve
			elif stat.lower() == "luck":
				self.LUCK = improve
			else: return False
		else: return False
		
	def __repr__(self):
		return self.handle