import os
import punk
import base64
import uni


if "REPL_OWNER" in os.environ:
	from replit import db
	uni.online = True
else:
	uni.online = False

def SaveCharacterDB(data=None,handle=""):
	if data == None or name == "": return
	
	if uni.online:
		db[uni.user + "`char`" + handle] = data.__dict__
	else:
		pass

def LoadCharacterDB(handle=""):
	if handle == "": return

	if uni.online:
		p = punk.Punk()
		p.__dict__ = db[uni.user + "`char`" + handle].value
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
		password += os.environ['salt']
		while len(password) % 4 != 0:
				password += "*"
		test = str(base64.b64encode(password.encode("utf8")))
		if db[user] == test:
			uni.user = user
			return True
	return False

def NewUser(user="",password1="",password2=""):
	if user != "" and password1 != "" and password2 != "":
		if user not in db and password1 == password2:
			password1 += os.environ['salt']
			while len(password1) % 4 != 0:
				password1 += "*"
			db[user] = str(base64.b64encode(password1.encode("utf8")))
			
			return True
		
	return False