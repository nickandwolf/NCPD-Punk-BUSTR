from random import randint as r


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

		self.knownNPCs = []
		if knownNPCs == None:
			self.Siblings()
		else:
			self.knownNPCs = knownNPCs

		if motivations == None:
			self.motivations = self.Motivations()
		else:
			self.motivations = motivations

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
		    "Bald", "Striped", "Tinted", "Neat & Short", "Short & Curly",
		    "Long & Straight"]

	def GetAffectationList(self):
		return ["Tattoos", "Mirrorshades", "Ritual Scars", "Spiked Gloves",
		    "Nose Rings", "Earrings", "Long Fingernails", "Spiked Boots",
		    "Weird Contact Lenses", "Fingerless Gloves"]
	
	def DressAndStyle(self):
		cList = ["Biker Leathers", "Blue Jeans", "Corporate Suits", "Jumpsuits",
		    "Miniskirts/Flash", "High Fashion", "Military", "Normal Clothes",
		    "Near Nude", "Bag Lady Chic"]

		hList = ["Mohawk", "Long & Ratty", "Short & Spiked", "Wild & All Over",
		    "Bald", "Striped", "Tinted", "Neat & Short", "Short & Curly",
		    "Long & Straight"]

		aList = ["Tattoos", "Mirrorshades", "Ritual Scars", "Spiked Gloves",
		    "Nose Rings", "Earrings", "Long Fingernails", "Spiked Boots",
		    "Weird Contact Lenses", "Fingerless Gloves"]
		
		total = []
		total.append(cList[r(0, len(cList)-1)])
		total.append(hList[r(0, len(hList)-1)])
		total.append(aList[r(0, len(aList)-1)])
		return total

	def FamilyBackground(self, overdosed=False):
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
		    "one or both parents overdosed", "you never knew your parents",
		    "one or both parents are in hiding to protect you",
			"you were raised by relatives for safekeeping"
		    "the streets raised you", "one or both parents gave you up",
		    "one or both parents sold you for cash"
		]
		familyStatus = ["Family is in danger", "Family isn't in danger"]
		#so you ...
		childhoodEnviron = [
		    "spent most of your childhood on the streets with no adult supervision",
		    "spent your childhood in a safe Corporate Suburbia",
		    "spent your childhood in a Nomad Pack, moving from town to town",
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
		    "left you to inherit a family debt which must be honored"
		]

		story = "Your parents were "
		story += familyRanking[r(0, len(familyRanking)-1)]

		if r(1, 10) > 6:
			story += " however " + somethingHappened[r(0, len(somethingHappened)-1)]

		#and overdosed
		if overdosed:
			story += " and overdosed"
		if r(1, 10) > 6:
			story += " and " + familyTragedy[r(0, len(familyTragedy)-1)]

		story += ". So you " + childhoodEnviron[r(0, len(childhoodEnviron)-1)]

		if overdosed:
			story += " and overdosed"

		story += "."

		return story

	def Siblings(self):
		sibNum = r(1, 10)
		if sibNum > 7:
			return

		for i in range(sibNum):
			story = ""
			roll = r(1, 10)
			if roll < 6: story += "An older"
			elif roll < 10: story += "A younger"
			elif roll == 10: story += "A twin"

			if r(0, 1) == 0: story += " brother who "
			else: story += " sister who "

			like = [
			    "dislikes you", "likes you", "is neutral to you",
			    "hero worships you", "hates you"
			]
			story += like[r(0, len(like)-1)] + "."

			self.knownNPCs.append(story)

	def Motivations(self):
		story = ""

		#You are ...
		personality = [
		    "shy and secretive", "rebellious, antisocial, and violent",
		    "arrogant, proud, and aloof", "moody, rash, and headstrong",
		    "picky, fussy, and nervous", "cold and serious",
		    "silly and fluffheaded", "sneaky and deceptive",
		    "intellectual and detached", "friendly and outgoing"
		]
		#The person you care about most is ...
		person = [
		    "a parent", "a sibling or cousin", "a lover", "a friend",
		    "yourself", "a pet", "a teacher or mentor", "a public figure",
		    "a personal hero", "no one, not even yourself"
		]
		#More often than not, you put ... over everything else.
		concept = [
		    "money", "honor", "your word", "honesty", "knowledge", "vengeance",
		    "love", "power", "having a good time", "friendship"
		]
		#You ...
		social = [
		    "like almost everyone", "hate almost everyone",
		    "treat people like tools, meant to be used and then discarded",
		    "believe every person has value",
		    "believe people are obstacles to be crushed if they get in your the way",
		    "believe people are untrustworthy and will only let you down",
		    "believe mankind deserves to wiped out",
		    "believe people are wonderful"
		]
		#You wouldn't be caught dead without your ...
		item = [
		    "favorite weapon", "favorite tool", "favorite article of clothing",
		    "photograph", "journal", "mix tape", "musical instrument",
		    "favorite piece of jewelry", "childhood toy", "letter"
		]
