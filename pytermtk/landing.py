import TermTk as ttk
import saveLoadExport as sle
import uni

def main():
	if uni.online: #login db doesn't work
		import pytermtk.login
		pytermtk.login.LoginBox()
	
	else:
		import pytermtk.viewCharacters
		pytermtk.viewCharacters.ShowCharacters()

if __name__ == "__main__":
	main()