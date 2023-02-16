import saveLoadExport as sle
import TermTk as ttk
import uni
import pytermtk.viewCharacters
'''
Required Widgets
-Single Line Text Edit with secure entry (the ****** thing)
-Button
-Window
'''

def LoginBox():
	root = ttk.TTk()
	
	lbaf = ttk.TTkFrame(parent=root,border=True,pos=(0,0),size=(47,14))
	ttk.TTkLabel(parent=lbaf, text="[Welcome to NCPD Punk B.U.S.T.R.]["
				 + uni.version + "]",pos=(1,0))
	ttk.TTkLabel(parent=lbaf, text="─────────────────────────────────────────────",
				 pos=(0,1))

	lbf = ttk.TTkFrame(parent=lbaf,pos=(6,4),size=(33,7), border=False)
	ttk.TTkLabel(parent=lbf, text="[USERNAME:",pos=(1,0))
	user = ttk.TTkLineEdit(parent=lbf, pos=(11,0), size=(18,1))
	ttk.TTkLabel(parent=lbf, text="]",pos=(29,0))

	ttk.TTkLabel(parent=lbf, text="[PASSWORD:",pos=(1,1))
	password = ttk.TTkLineEdit(parent=lbf, pos=(11,1),
							   size=(18,1),inputType=ttk.TTkK.Input_Password)
	ttk.TTkLabel(parent=lbf, text="]",pos=(29,1))

	def Login():
		weGood = sle.CheckUserNamePassword(str(user._text),str(password._text))
		if True:
			root.quit()
			pytermtk.viewCharacters.ShowCharacters()
		else:
			print("SHIT")
			pop = ttk.TTkWindow(parent=root,title="❌ERROR❌",pos=(5,5),size=(22,6))
			ttk.TTkLabel(parent=pop,text="  Unknown User or",pos=(0,0))
			ttk.TTkLabel(parent=pop,text="Password combination",pos=(0,1))

	def NewUser():
		pop = ttk.TTkWindow(parent=root,title="NEW USER",pos=(6,2),size=(33,9))
		ttk.TTkLabel(parent=pop, text="[USERNAME:",pos=(1,0))
		username = ttk.TTkLineEdit(parent=pop, pos=(11,0), size=(18,1))
		ttk.TTkLabel(parent=pop, text="]",pos=(29,0))

		ttk.TTkLabel(parent=pop, text="[PASSWORD:",pos=(1,1))
		pass1 = ttk.TTkLineEdit(parent=pop, pos=(11,1), size=(18,1),
							   inputType=ttk.TTkK.Input_Password)
		ttk.TTkLabel(parent=pop, text="]",pos=(29,1))

		ttk.TTkLabel(parent=pop, text="[SAMEPASS:",pos=(1,2))
		pass2 = ttk.TTkLineEdit(parent=pop, pos=(11,2), size=(18,1),
							   inputType=ttk.TTkK.Input_Password)
		ttk.TTkLabel(parent=pop, text="]",pos=(29,2))

		def NW():
			weGood = sle.NewUser(str(username._text),str(pass1._text),str(pass2._text))
			
			if weGood:
				pop.close()
			else:
				poop = ttk.TTkWindow(parent=root, title="❌ERROR❌", pos=(10,5),size=(24,6))
				ttk.TTkLabel(parent=poop,text="   Bad Username or",pos=(0,0))
				ttk.TTkLabel(parent=poop,text="Passwords didn't match",pos=(0,1))
				poop.raiseWidget()
				
		
		ttk.TTkButton(parent=pop, text="MAKE NEW USER",
				  pos=(1,4),size=(29,1)).clicked.connect(NW)
			
		pop.raiseWidget()
		
		
		
	ttk.TTkButton(parent=lbf, text="LOGIN",
				  pos=(1,3),size=(7,1)).clicked.connect(Login)
	ttk.TTkButton(parent=lbf, text="NEW USER",
				  pos=(20,3),size=(10,1)).clicked.connect(NewUser)
	#ttk.TTkButton(parent=lbf, text="FORGOT PASSWORD",
	#			  pos=(13,5),size=(17,1)).clicked.connect()
	
	ttk.TTkLabel(parent=lbaf, text="ᵂᵒʳˡᵈˢᵃᵗ ˢʸˢᵗᵉᵐ ˢᵉᶜᵘʳⁱᵗʸ ⁿᵒᵗ ᵍᵘᵃʳᵃⁿᵗᵉᵉᵈ",pos=(3,2))
	ttk.TTkLabel(parent=lbaf, text="ᵂᵒʳˡᵈˢᵃᵗ ˢʸˢᵗᵉᵐ ˢᵉᶜᵘʳⁱᵗʸ ⁿᵒᵗ ᵍᵘᵃʳᵃⁿᵗᵉᵉᵈ",pos=(3,11))
	
	root.mainloop()