import saveLoadExport as sle
import TermTk as ttk
import pytermtk.fullCharacterSheet


def ShowCharacters():#TODO: Add flavor
	root = ttk.TTk()

	def Load():
		v = str([str(s) for s in scl.selectedLabels()])
		v = v[2:-2]
		dude = sle.LoadCharacterDB(v)
		root.quit()
		pytermtk.fullCharacterSheet.FullSheet(dude)

	def Blip(x):
		sle.DeleteCharacterDB(x)
		root.quit()
		ShowCharacters()
	
	def Delete():
		v = str([str(s) for s in scl.selectedLabels()])
		v = v[2:-2]
		pop = ttk.TTkWindow(parent=root,title="Delete?",size=(21,8),pos=(3,3))
		ttk.TTkLabel(parent=pop, text="   Expunge perp's", pos=(0,0))
		ttk.TTkLabel(parent=pop, text="      record?",pos=(0,1))
		ttk.TTkButton(parent=pop,text="Okay",pos=(1,3),size=(6,1)).clicked.connect(
			lambda x = v: Blip(x))
		ttk.TTkButton(parent=pop,text="Cancel",pos=(10,3),size=(8,1)).clicked.connect(
			pop.close)
		pop.raiseWidget()
	
	characters = sle.GetCharacters()
	scf = ttk.TTkFrame(parent=root,border=True,pos=(0,0),size=(20,7))
	scl = ttk.TTkList(parent=scf,pos=(0,0),size=(18,5))
	for x in characters:
		scl.addItem(x)

	def New(v=None):
		root.quit()
		pytermtk.fullCharacterSheet.FullSheet()
	
	newB = ttk.TTkButton(parent=root, text="NEW",pos=(0,8),size=(5,1))
	newB.clicked.connect(New)
	
	loadB = ttk.TTkButton(parent=root, text="LOAD",pos=(7,8),size=(6,1))
	loadB.clicked.connect(Load)
	
	deleteB = ttk.TTkButton(parent=root, text="DELETE",pos=(16,8),size=(8,1))
	deleteB.clicked.connect(Delete)

	root.mainloop()