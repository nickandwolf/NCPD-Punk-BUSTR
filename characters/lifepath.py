from random import randint as r
import characters.punk as cp

def getKey(obj):
	return obj.name

class LifePath:
	def __init__(self,
	             ethnicity=None,
	             language=None,
	             clothes=None,
	             hairstyle=None,
	             affectations=None,
	             familyBackground=None,
	             knownNPCs=None,
	             motivations=None):
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