import csv
import os
#TODO: Put in my custom skills


class Skill: #how to do martial arts, pilot, expert?
    def __init__(self,
                 stat="",
                 special=False,
                 name="",
                 description="",
                 level=0,
                 cost=1,
                 IP=0,
                 reference=""):
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
        self.learned = False

        self.check = None
        self.button = None
        self.spin = None

    def __repr__(self):
        return self.name


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
        with open(path + "/skills/skills_cc.csv", 'r') as csvFile:
            reader = csv.reader(csvFile, delimiter="`")
            for row in reader:
                #print(row)#DEBUG
                thing = Skill(row[0], row[1], row[2], row[3], row[4], row[5],
                              row[6], row[7])
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
    