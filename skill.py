import csv
import os
#TODO: Put in my custom skills

class Skill: #how to do martial arts, pilot, expert?
	def __init__(self,
				 name="",
				 description="",
				 special=False,
				 stat="",
				 level=0,
				 cost=1,
				 IP=0,
				 reference="",
				 learned=False):
		self.special = special
		self.name = name
		self.description = description
		self.stat = stat

		if level == '': level = 0
		self.level = int(level)

		self.cost = int(cost) * 10

		if IP == '': IP = 0
		self.IP = int(IP)
		self.reference = reference
		self.learned = learned

	def __repr__(self):
		return self.name

	def __iter__(self):
		yield 'name', self.name
		yield 'description', self.description
		yield 'special', self.special
		yield 'stat', self.stat
		yield 'level', self.level
		yield 'cost', self.cost
		yield 'IP', self.IP
		yield 'reference', self.reference
		yield 'learned', self.learned

def getKey(obj):
	return obj.name


skillList = []
specSkillList = []
attrSkillList = []
bodySkillList = []
coolSkillList = []
empSkillList = []
intSkillList = []
refSkillList = []
techSkillList = []


def _skillInit():  #pass the csv
	if skillList == []:
		path = os.getcwd()
		'''
		csv order = stat[0],special[1],name[2],description[3],cost[4],reference[5]
  		'''
		with open(path + "/files/skills.csv", 'r') as csvFile:
			reader = csv.reader(csvFile, delimiter="`")
			for row in reader:
				thing = Skill(row[2],row[3],row[1],row[0],0,row[4],0,row[5],False)
				if thing not in skillList:
					skillList.append(thing)

				if thing.special and thing not in specSkillList:
					specSkillList.append(thing)
				else:
					if thing.stat == 'ATTR' and thing not in attrSkillList:
						attrSkillList.append(thing)
					elif thing.stat == 'BODY' and thing not in bodySkillList:
						bodySkillList.append(thing)
					elif thing.stat == 'COOL' and thing not in coolSkillList:
						coolSkillList.append(thing)
					elif thing.stat == 'EMP' and thing not in empSkillList:
						empSkillList.append(thing)
					elif thing.stat == 'INT' and thing not in intSkillList:
						intSkillList.append(thing)
					elif thing.stat == 'REF' and thing not in refSkillList:
						refSkillList.append(thing)
					elif thing.stat == 'TECH' and thing not in techSkillList:
						techSkillList.append(thing)
					else:
						print("SKILL ERROR:" + str(thing.name))
		specSkillList.sort(key=getKey)
		attrSkillList.sort(key=getKey)
		bodySkillList.sort(key=getKey)
		coolSkillList.sort(key=getKey)
		empSkillList.sort(key=getKey)
		intSkillList.sort(key=getKey)
		refSkillList.sort(key=getKey)
		techSkillList.sort(key=getKey)
	else:
		pass