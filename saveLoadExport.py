import os
import punk
import base64
import uni
import skill
import json

skill._skillInit()
### Changing Handle Duplicates Characters ###

if "REPL_OWNER" in os.environ:
	from replit import db
	'''
 	Replit DB is a bane on my existence. The amount of persnickety BS it demands
  	and number of catches required pains me greatly. But I wanted a thing to work
    online so I guess I need to put up with it.
 	'''
	uni.online = True
else:
	uni.online = False

def DeleteCharacterDB(handle=""):
	if handle.strip() == "": return

	if uni.online:
		del db[uni.user + '`char`' + handle.lower()]

def SaveCharacterDB(data=None,handle=""):
	if data == None or handle.strip() == "": return
	handle = handle.lower()
	if uni.online:
		db[uni.user + "`char`" + handle] = data.__dict__
	else:
		pass

def LoadCharacterDB(handle=""):
	if handle.strip() == "": return

	if uni.online:
		p = punk.Punk()
		p.__dict__ = db[uni.user + "`char`" + handle.lower()].value
		return p

def GetCharacters():
	characters = []
	if uni.online:
		for x in db.keys():
			x = x.split('`char`')
			if len(x) > 1 and x[0] == uni.user:
				characters.append(x[1]) #make this load a punk object
	else:
		pass

	return characters
	
## ENCRYPTION IS BLACK MAGIC, I DON'T KNOW WHAT I'M DOING; GOD HELP US ALL ##
def CheckUserNamePassword(user="",password=""):
	if user != "" and password != "":
		user.lower()
		password += os.environ['salt']
		while len(password) % 4 != 0:
				password += "*"
		test = str(base64.b64encode(password.encode("utf8")))
		try:
			if db[user] == test:
				uni.user = user
				return True
		except:
			pass
	return False

def NewUser(user="",password1="",password2=""):
	if user != "" and password1 != "" and password2 != "":
		user = user.lower()
		if user not in db and password1 == password2:
			password1 += os.environ['salt']
			while len(password1) % 4 != 0:
				password1 += "*"
			db[user] = str(base64.b64encode(password1.encode("utf8")))
			
			return True
		
	return False