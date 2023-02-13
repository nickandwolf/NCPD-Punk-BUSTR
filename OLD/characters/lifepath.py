from random import randint as r
import characters.punk as cp

### May want to make all these lists be external files?

def getKey(obj):
	return obj.name

class LifePath: #we can expand a lot of this lifepath stuff
	def __init__(self,
				 ethnicity=None,
				 language=None,
				 clothes=None,
				 hairstyle=None,
				 affectations=None,
				 familyBackground=None,
				 knownNPCs=None,
				 motivations=None,
				 events=None):
		if ethnicity == None:	
			self.ethnicity = self.Ethnicity()
		else:
			self.ethnicity = ethnicity

		if language == None:
			self.language = self.SelectLanguage()
		else:
			self.language = language

		self.knownNPCs = []
		if knownNPCs == None:
			self.Siblings()
		else:
			self.knownNPCs = knownNPCs
			
		dressStyle = self.DressAndStyle()
		if affectations == None:
			self.clothes = dressStyle[0]
		else:
			self.clothes = affectations[0]
		if affectations == None:
			self.hairstyle = dressStyle[1]
		else:
			self.hairstyle = affectations[1]
		if affectations == None:
			self.affectation = dressStyle[2]
		else:
			self.affectation = affectations[2]

		if familyBackground == None:
			self.familyBackground = self.FamilyBackground()
		else:
			self.familyBackground = familyBackground

		if motivations == None:
			self.motivations = self.Motivations()
		else:
			self.motivations = motivations

		self.events = []
		if events == None:
			self.LifeEvents()
		else:
			self.events = events
			
		self.knownNPCs.sort(key=getKey)

	def Ethnicity(self):
		ethnicity = ["Anglo-American","African","Japanese/Korean","Central European/Soviet","Pacific Islander","Chinese/Southeast Asian","Black American","Hispanic American","Central/South American","European"]
		return ethnicity[r(0,len(ethnicity)-1)]

	def GetEthnicityList(self):
		return ["Anglo-American","African","Japanese/Korean","Central European/Soviet","Pacific Islander","Chinese/Southeast Asian","Black American","Hispanic American","Central/South American","European"]
	
	def SelectLanguage(self,ethnicity=None):
		if ethnicity == None:
			ethnicity = self.ethnicity
		if ethnicity == "Anglo-American":
			return ["English","French"]
		elif ethnicity == "African":
			return ["Bantu", "Fante", "Kongo", "Ashanti", "Zulu", "Swahili"]
		elif ethnicity == "Japanese/Korean":
			return ["Japanese", "Korean"]
		elif ethnicity == "Central European/Soviet":
			return [
				"Bulgarian", "Russian", "Czech", "Polish", "Ukranian", "Slovak"
			]
		elif ethnicity == "Pacific Islander":
			return [
				"Microneasian", "Tagalog", "Polynesian", "Malayan", "Sudanese",
				"Indonesian", "Hawaiian"
			]
		elif ethnicity == "Chinese/Southeast Asian":
			return [
				"Burmese", "Cantonese", "Mandarin", "Thai", "Tibetan",
				"Vietnamese"
			]
		elif ethnicity == "Black American":
			return ["English", "Blackfolk"]
		elif ethnicity == "Hispanic American":
			return ["Spanish", "English"]
		elif ethnicity == "Central/South American":
			return ["Spanish", "Portuguese"]
		elif ethnicity == "European":
			return [
				"French", "German", "English", "Spanish", "Italian", "Greek",
				"Danish", "Dutch", "Norwegian", "Swedish", "Finnish"
			]
		else:
			return None

	def SetLanguage(self, lang):
		self.language = lang

	def GetClothesList(self):
		return ["Biker Leathers", "Blue Jeans", "Corporate Suits", "Jumpsuits",
			"Miniskirts/Flash", "High Fashion", "Military", "Normal Clothes",
			"Near Nude", "Bag Lady Chic"]

	def GetHairList(self):
		return ["Mohawk", "Long & Ratty", "Short & Spiked", "Wild & All Over",
			"Bald", "Striped", "Frosted", "Neat & Short", "Short & Curly",
			"Long & Straight"]

	def GetAffectationList(self):
		return ["Tattoos", "Mirrorshades", "Ritual Scars", "Spiked Gloves",
			"Nose Rings", "Earrings", "Long Fingernails", "Spiked Boots",
			"Weird Contact Lenses", "Fingerless Gloves"]

	def GetPersonalityList(self):
		return [
			"shy & secretive", "rebellious, antisocial, & violent",
			"arrogant, proud, & aloof", "moody, rash, & headstrong",
			"picky, fussy, & nervous", "cold & serious",
			"silly & fluffheaded", "sneaky & deceptive",
			"intellectual & detached", "friendly & outgoing"
		]

	def GetImportantPersonList(self):
		return [
			"a parent", "a sibling or cousin", "a lover", "a friend",
			"themself", "a pet", "a teacher or mentor", "a public figure",
			"a personal hero", "no one, not even themself"
		]

	def GetConceptList(self):
		return [
			"money", "honor", "their word", "honesty", "knowledge", "vengeance",
			"love", "power", "having a good time", "friendship"
		]

	def GetImportantItemList(self):
		return [
			"favorite weapon", "favorite tool", "favorite article of clothing",
			"photograph", "journal", "mix tape", "musical instrument",
			"favorite piece of jewelry", "childhood memento", "letter"
		]
	
	def GetSocialList(self):
		return [
			"likes almost everyone", "hates almost everyone",
			"people like tools, meant to be used and then discarded",
			"believes every person has value",
			"believes people are obstacles to be crushed if they get in your the way",
			"believes people are untrustworthy and will only let you down",
			"believes mankind deserves to wiped out",
			"believes people are wonderful"
		]
	def DressAndStyle(self):
		total = []
		total.append(self.GetClothesList()[r(0, len(self.GetClothesList())-1)])
		total.append(self.GetHairList()[r(0, len(self.GetHairList())-1)])
		total.append(self.GetAffectationList()[r(0, len(self.GetAffectationList())-1)])
		return total

	def FamilyBackground(self, PC=True, overdosed=False):#add PC stuff so it makes sense
		#You parents were ...
		familyRanking = [
			"Corporate Executives", "Corporate Managers",
			"Corporate Technicians", "in a Nomad Pack",
			"part of a Pirate Fleet", "a Gang Family", "Crime Lords",
			"Combat Zone Poor", "Urban Homeless", "an Arcology Family"
		]
		parents = ["parents are alive",
				   "something happened"]  #Spin this better
		#however ...
		somethingHappened = [
			"one or both parents died in warfare",
			"one or both parents died in an accident",
			"one or both parents were murdered",
			"one or both parents overdosed", "never knew parents",
			"one or both parents are in hiding for protection",
			"were raised by relatives for safekeeping",
			"was raised by the streets", "one or both parents gave their children up",
			"one or both parents sold children for cash"
		]
		familyStatus = ["Family is in danger", "Family isn't in danger"]
		#so you ...
		childhoodEnviron = [
			"spent most of childhood on the streets with no adult supervision",
			"spent childhood in a safe Corporate Suburbia",
			"spent childhood in a Nomad Pack, moving from town to town",
			"grew up in a decaying, once upscale neighborhood",
			"grew up in a defended Corporate Zone in the central City",
			"grew up in the heart of the Combat Zone",
			"grew up in a small village or town far from the City",
			"grew up in a large arcology", "grew up in an aquatic Pirate Pack",
			"grew up in a Corporate controlled Arcology or Research Center"
		]
		#Your family ...
		familyTragedy = [
			"lost everything through betrayal",
			"lost everything through bad management", "were cast into exile",
			"were imprisoned", "vanished one day", "were murdered",
			"were the target of a long-term conspiracy",
			"were scattered to the winds due to misfortune",
			"were cursed with a hereditary feud that has lasted generations",
			"left children to inherit a family debt which must be honored"
		]

		story = "Parents were "
		story += familyRanking[r(0, len(familyRanking)-1)]

		if r(1, 10) > 6:
			story += ". " + somethingHappened[r(0, len(somethingHappened)-1)].capitalize()
		roll = r(0,3)

		if roll == 0:#work this out more
			self.AddKnownNPC("Father","family",self.Motivations(),"Alive")
			self.AddKnownNPC("Mother","family",self.Motivations(),"Alive")
		elif roll == 1:
			self.AddKnownNPC("Father","family",self.Motivations(),"Dead")
			self.AddKnownNPC("Mother","family",self.Motivations(),"Alive")
		elif roll == 2:
			self.AddKnownNPC("Father","family",self.Motivations(),"Alive")
			self.AddKnownNPC("Mother","family",self.Motivations(),"Dead")
		elif roll == 3:
			self.AddKnownNPC("Father","family",self.Motivations(),"Dead")
			self.AddKnownNPC("Mother","family",self.Motivations(),"Dead")
			
		
		#and overdosed
		if overdosed:
			story += " and overdosed"
		if r(1, 10) > 6:
			story += ", parents " + familyTragedy[r(0, len(familyTragedy)-1)]
			
		story += ". Children " + childhoodEnviron[r(0, len(childhoodEnviron)-1)]

		if overdosed:
			story += " and overdosed"

		story += "."

		return story

	def Siblings(self):
		sibNum = r(1, 10)
		if sibNum > 7:
			return

		for i in range(sibNum):
			relationship = ""
			motivations = self.Motivations()
			notes = ""
			
			roll = r(1, 10)
			if roll < 6: relationship += "Oldr"
			elif roll < 10: relationship += "Yngr"
			elif roll == 10: relationship += "Twin"

			if r(0, 1) == 0: relationship += " Bro"
			else: relationship += " Sis"

			like = [
				"Dislikes you", "Likes you", "Is neutral to you",
				"Hero worships you", "Hates you"
			]
			
			notes += like[r(0, len(like)-1)] + ". "
			relationship += " #1"
			self.AddKnownNPC(relationship,"family",motivations,notes)
			
			
	def AddKnownNPC(self,name1="",relationship1="",motivations1="",notes1=""):
		x = 2
		if notes1 != "" and notes1[-1].strip() != ".":
			notes1 = notes1.strip() + ". "
		for a in self.knownNPCs:
			while a.name == name1:
				name1 = name1.split(" #")[0] + " #" + str(x)
				x+=1
		dude = cp.NPC(relation=relationship1,name=name1,motivations=motivations1,notes=notes1)
		self.knownNPCs.append(dude)
		#family#friend#associate#enemy#rando
		
	def Motivations(self):
		story = []
		story.append(self.GetPersonalityList()[r(0,len(self.GetPersonalityList())-1)])
		story.append(self.GetImportantPersonList()[r(0,len(self.GetImportantPersonList())-1)])
		story.append(self.GetConceptList()[r(0,len(self.GetConceptList())-1)])
		story.append(self.GetSocialList()[r(0,len(self.GetSocialList())-1)])
		story.append(self.GetImportantItemList()[r(0,len(self.GetImportantItemList())-1)])
		return story

	def LifeEvents(self):
		class Problem:
			def __init__(self,age=0,problem="",details="",resolve="",function=None):
				self.age = age
				self.problem = problem
				self.details = details
				self.resolve = resolve
				self.function = function
			
		age = 16
		count = 0
		for x in range(r(2,12)):
			roll = r(1,10)
			if roll < 4:
				if r(0,1) == 0:
					pass
					#yep = self.BigWins()
					#self.events.append(Problem(age+count,) +"] " + self.BigWins()
				else:
					yep = self.BigProblems()
					self.events.append(Problem(age+count, yep[0],yep[1],yep[3],yep[2]))
			elif roll < 7:
				pass
				#self.events.append("[Age " + str(age+count) +"] " + self.FriendsAndEnemies()
			elif roll < 9:
				pass
				#self.events.append(["Age " + str(age+count) +"] " + self.RomanticRelations()
			else:
				pass
				#self.events.append("[Age " + str(age+count) +"] Nothing worth remembering.")
			count += 1

	def BigProblems(self):
								   
		disasters = ["Financial Loss / Debt", "Imprisonment", "Illness or Addiction",
								   "Betrayal", "Accident", "Lover, Friend, or Relative Killed",
								   "False Accusation", "Hunted by the Law", "Hunted by a Corporation",
								   "Mental or Physical Incapacitation"]

		#this mirrors disasters

		urDisaster = r(0,len(disasters)-1) #I have no clue if this lambda stuff is going to work
		urDetails = ""					   #SHIT I may have to learn how to do args* kwargs**
		if urDisaster == 1: #Lost money		#ALSO THIS CAN EFFECT REP!
			dosh = str(r(1,10)*100)
			urDetails = "You owe €$" + dosh + " to someone you don't want to piss off."
			self.AddKnownNPC(cp.GetFirstLastName(),"associate",
							 "", "You owe them €$" + dosh + ".")
			urFunc = lambda cash,cost : cash - cost
		elif urDisaster == 2: #Imprisonment
			if r(0,1) == 0:
				urDetails = "You were held hostage for " + str(r(1,10)) + "months."
			else: urDetails = "You were in prison for " + str(r(1,10)) + "months."
			urFunc = None
		elif urDisaster == 3: #illness/addition
			if r(0,1) == 0:
				urDetails = "You contracted a designer disease."
			else: urDetails = "You struggled with drug addiction."
			urFunc = lambda ref : ref - 1
		elif urDisaster == 4: #betrayal
			roll = r(1,10)
			if roll < 4:
				urDetails = "You are being blackmailed by someone you trusted."
				self.AddKnownNPC(cp.GetFirstLastNames(),
								 "enemy","", "They are blackmailing you.")
			elif roll < 8:
				urDetails = "Someone you trusted exposed a secret to hurt you."
				self.AddKnownNPC(cp.GetFirstLastName(),
								 "enemy","", "They exposed one of your secrets to hurt you.")
			else:
				urDetails = "A close friend stabbed you in the back."
				self.AddKnownNPC(cp.GetFirstLastName(),
								 "enemy","", "They stabbed you in the back.")
		elif urDisaster == 5: #Accident
			roll = r(1,10)
			if roll < 5:
				urDetails = "You were disfigured in a terrible accident."
				urFunc = lambda attr : 1 if attr-5 < 1 else attr-5
			elif roll < 7:
				urDetails = "You were hospitalized for " + str(r(1,10)) + " months that year."
				urFunc = None
			elif roll < 9:
				urDetails = "You lost " + str(r(1,10)) + " months of your memory that year."
				urFunc = None
			else:
				urDetails = "You suffer from severe PTSD from a terrible accident."
				urFunc = None
		elif urDisaster == 6: #Friend/Lover/Family killed
			victim = ""
			roll = r(0,2);
			if roll == 0:
				victim = "close friend "
				self.AddKnownNPC(cp.GetFirstLastName(),"friend","","")
			elif roll == 1:
				victim = "lover "
				self.AddKnownNPC(cp.GetFirstLastName(),"friend","","")
			else:
				victim = "family member "
				self.AddKnownNPC(cp.GetFirstLastName(),"family","","")
			roll = r(1,10)
			urDetails = "A " + victim
			if roll < 6:
				urDetails += "died in an accident."
				self.knownNPCs[-1].notes = "Died in an accident."
			elif roll < 9:
				urDetails += "was murdered."
				self.knownNPCs[-1].notes = "Murdered."
			else:
				urDetails += "was murdered and you know who did it. You just need the proof."
				self.knownNPCs[-1].notes = "Murdered."
				self.AddKnownNPC(cp.GetFirstLastName(),"enemy","",
								 "They murdered " + self.knownNPCs[-1].name + ".")
			urFunc = None
		elif urDisaster == 7: #False accusation
			roll = r(1,10)
			urDetails = "You were set up and "
			if roll < 4:
				urDetails += "accused of theft."
			elif roll < 6:
				urDetails += "made to look like a coward."
			elif roll < 9:
				urDetails += "accused of murder."
			elif roll < 10:
				urDetails += "accused of rape."
			else:
				urDetails += "made to look like a snitch."
			urFunc = None
		elif urDisaster == 8: #Hunted by the law
			roll = r(1,10)
			if roll < 4:
				urDetails = "A couple of local cops have it out for you."
				self.AddKnownNPC("Local Cops", "enemy", "", "")
			elif roll < 7:
				urDetails = "The local police precinct is hunting you down."
				self.AddKnownNPC("Local Police Department", "enemy", "", "")
			elif roll < 9:
				urDetails = "NCPD has an APB out for you."
				self.AddKnownNPC("NCPD", "enemy", "", "")
			elif roll < 10:
				urDetails = "The State Police have an APB out on you."
				self.AddKnownNPC("State Police", "enemy", "", "")
			else: 
				urDetails = "You're on America's Most Wanted."
				self.AddKnownNPC("US Marshals", "enemy", "", "")
			urFunc = None 
		elif urDisaster == 9: #Hunted by corporation
			roll = r(1,10)
			if roll < 4:
				urDetails = "A small corporation is pissed at you."
				self.AddKnownNPC("Local Corporate", "enemy", "", "")
			elif roll < 7:
				urDetails = "A corporation with multiple local offices has it out for you."
				self.AddKnownNPC("Small Corporation", "enemy", "", "")
			elif roll < 9:
				urDetails = "A statewide corporation wants you 'unalived'."
				self.AddKnownNPC("Statewide Corporation", "enemy", "", "")
			elif roll < 10:
				urDetails = "A national corporation with some serious pull has a vested interest in your demise."
				self.AddKnownNPC("National Corporation", "enemy", "", "")
			else: 
				urDetails = "A global corporation with armies, spies, and ninjas with a market cap that eclipses 75% of the world's economy has a stock called DEAD with your name on it."
				self.AddKnownNPC("Global Corporation", "enemy", "", "")
			urFunc = None 
		elif urDisaster == 10: #mental/physical incapicitation
			roll = r(1,10)
			if roll < 4:
				urDetails = "You developed a neuro-disorder, possibly from a bio-plague."
				urFunc = lambda ref : ref-1
			elif roll < 8:
				urDetails = "You suffer from severe anxiety."
				urFunc = lambda cool : cool-1
			else:
				urDetails = "You have major psychosis; hear voices, prone to violence, irrational impulses, and depression."
				urFunc = lambda ref,cool : [ref - 1, cool -1]
				
		whatDo = ["Clear your name", "Live it down and try to forget", "Hunt down those responsible and make them pay", "Get what's rightfully yours", "Save, if possible, anyone else involved in the situation"]

		return [disasters[urDisaster], urDetails, urFunc, whatDo[r(0,len(whatDo)-1)]]
		

	def BigWins(self):
		pass

	def FriendsAndEnemies(self):
		pass

	def RomanticRelations(self):
		pass

	def GetLPAge(self):
		pass #life events + 16
	