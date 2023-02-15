import saveLoadExport as sle
import TermTk as ttk

root = ttk.TTk()

def ShowCharacters():
	characters = sle.GetCharacters()
	scf = ttk.TTkFrame(parent=root,border=True,pos=(0,0),size=(47,14))
	scl = ttk.TTkList(parent=scf,pos=(0,0),size=(18,5))
	for x in characters:
		self.scl.addItem(x.handle)