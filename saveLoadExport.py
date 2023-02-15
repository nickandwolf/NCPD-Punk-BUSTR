import os
import punk
import pyAesCrypt
import io

online = False
user = None


if "REPL_OWNER" in os.environ:
	from replit import db
	online = True
else:
	online = False

def SaveCharacterDB(data=None,name=None):
	if data == None or user == None: return
	
	if online:
		db[user + "`char`" + name] = data
	else:
		pass
## ENCRYPTION IS BLACK MAGIC, I DON'T KNOW WHAT I'M DOING; GOD HELP US ALL ##
def CheckUserNamePassword(user="",password=""):
	return True

def NewUser(user="",password1="",password2=""):
	if user != "" and password1 != "" and password2 != "":
		if user not in db and password1 == password2:
			password1 += os.environ['salt']
			fIn = io.BytesIO(password1.encode('utf-8'))
			fCiph = io.BytesIO()
			pyAesCrypt.encryptStream(fIn, fCiph, password1, 64*1024)
			fCiph.seek(0)
			db[user] = str(fCiph.getvalue())
			return True
		
	return False