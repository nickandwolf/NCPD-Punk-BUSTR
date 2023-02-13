import base64
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import os

#os.environ["REPLIT_DB_URL"] = os.environ['database']
from replit import db


def encrypt(key, source, encode=True):
	key = SHA256.new(
	    key).digest()  # use SHA-256 over our key to get a proper-sized AES key
	IV = os.urandom(AES.block_size)  # generate IV
	encryptor = AES.new(key, AES.MODE_CBC, IV)
	padding = AES.block_size - len(
	    source) % AES.block_size  # calculate needed padding
	source += chr(
	    padding) * padding  # Python 2.x: source += chr(padding) * padding
	data = IV + encryptor.encrypt(
	    source)  # store the IV at the beginning and encrypt
	return base64.b64encode(data).decode("latin-1") if encode else data


def decrypt(key, source, decode=True):
	if decode:
		source = base64.b64decode(source.encode("latin-1"))
	key = SHA256.new(
	    key).digest()  # use SHA-256 over our key to get a proper-sized AES key
	IV = source[:AES.block_size]  # extract the IV from the beginning
	decryptor = AES.new(key, AES.MODE_CBC, IV)
	data = decryptor.decrypt(source[AES.block_size:])  # decrypt
	padding = data[
	    -1]  # pick the padding value from the end; Python 2.x: ord(data[-1])
	if data[-padding:] != bytes(
	    [padding]) * padding:  # Python 2.x: chr(padding) * padding
		raise ValueError("Invalid padding...")
	return data[:-padding]  # remove the padding


def main(debug=False):
	if debug:
		return "gas" + os.environ['salt']
	else:
		print("[version:0.0.0.1]\n")
		print("[Welcome to NCPD Punk B.U.S.T.R. powered by WorldSat]\n")
		print("[WorldSat does not guarentee the security of this system]\n")
		print("[NEW USERS LEAVE USERNAME BLANK]\n")
		username = input("USERNAME: ")
		user = username
		if username == "":
			username = newUser()
		else:
			username += os.environ['salt']

		password = getpass("PASSWORD: ").encode('utf-8')
		password2 = decrypt(username.encode('utf-8'), db[username])

		if password == password2:
			os.system('clear')
			print("Welcome <" + user + ">\n[NOW LOADING]")
			return username
		else:
			os.system('clear')
			main()


def newUser(user=""):
	os.system('clear')
	if user == "":
		print("[Welcome <UNIDENTIFIED>]\n[Please identify yourself]\n")
		go1 = True
		while go1:
			username = input("NEW USERNAME: ")
			if username != "":
				username += os.environ['salt']
			if username not in db and username != "":
				go1 = False
				go2 = True
				while go2:
					password = getpass("PASSWORD: ")
					password2 = getpass("REPEAT PASSWORD: ")
					if password == password2:
						db[username] = encrypt(username.encode('utf-8'),
						                       password)
						go2 = False
					else:
						print("\n[ERROR: PASSWORDS DO NOT MATCH]\n")
			else:
				print("\n[ERROR: USER ALREADY EXISTS]\n")
	else:
		print("[Welcome " + user.split(os.environ['salt'][0]) +
		      "]\nSomething about changing your password.")
	return username
	#else:
	#  print("[Welcome " + username.split(os.environ['salt'])[0] + "]\n[Prepare to change password]\n")
	#  #blahblah change password shit


#ttk.TTkLineEntry(inputType=ttk.TTkK.Input_Password)
