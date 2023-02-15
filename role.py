import os
import csv
import skill

roleList = []

class Role:  #TODO: Choosing THIS or THAT in creation...
	def __init__(self, name="", description="", sList=[], reference=""):
		self.name = name
		self.description = ""
		for x in description.split('|'):
			self.description += x + "\n"
		self.description = self.description[:-2]
		self.reference = reference
		self.skillList = sList

	def __repr__(self):
		return self.name

def getKey(obj):
	return obj.name

def _roleInit():
	path = os.getcwd()
	skill._skillInit()
	if roleList == []:
		with open(path + "/files/roles.csv", 'r') as csvFile:
			reader = csv.reader(csvFile, delimiter="`")
			for row in reader:
				roleSkillz = []
				for x in skill.skillList: #TODO: Probably better way to handle this
					for y in row[3].split(';'):
						if y.lower() == x.name.lower():
							roleSkillz.append(x)
				thing = Role(row[0], row[1], roleSkillz, row[2])
				if thing not in roleList:
					roleList.append(thing)
		roleList.sort(key=getKey)
	else:
		pass