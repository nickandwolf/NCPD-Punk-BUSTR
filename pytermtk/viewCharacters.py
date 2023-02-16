import saveLoadExport as sle
import TermTk as ttk
import pytermtk.fullCharacterSheet


def ShowCharacters():
	root = ttk.TTk()

	def Load():
		v = str([str(s) for s in scl.selectedLabels()])
		v = v[2:-2]
		dude = sle.LoadCharacterDB(v)
		pytermtk.fullCharacterSheet.FullSheet(dude)

	def Delete():
		pass
	
	characters = sle.GetCharacters()
	scf = ttk.TTkFrame(parent=root,border=True,pos=(0,0),size=(20,7))
	scl = ttk.TTkList(parent=scf,pos=(0,0),size=(18,5))
	for x in characters:
		scl.addItem(x)

	#newB = ttk.TTkButton(parent=root, text="NEW",pos=(0,8),size=(5,1))
	loadB = ttk.TTkButton(parent=root, text="LOAD",pos=(7,8),size=(6,1))
	loadB.clicked.connect(Load)
	
	deleteB = ttk.TTkButton(parent=root, text="DELETE",pos=(16,8),size=(8,1))
	#deleteB.clicked.connect()

	root.mainloop()