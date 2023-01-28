'''
Night City Police Department 'Punk' B.U.S.T.R.
Official Name: Biotelemetric Unlocated Scene Threat Reposity
AKA Beat Up Street Trash Repository

https://towardsdatascience.com/finding-performance-bottlenecks-in-python-4372598b7b2c (when finalized)
'''
import TermTk as ttk
import characters.character as cc
import skills.skills as ss
import characters.punk as cp
import characters.lifepath as cl
import database.database
from replit import db


def main1():
	cp._punkInit()
	root = ttk.TTk()
	ttk.TTkComboBox(parent=root,
					list=["Rockerboy", "Solo"],
					pos=(0, 0),
					size=(18, 1))
	root.mainloop()


def main():
	ss._skillInit()
	#cc.FullSheet()
	#poop = cl.LifePath()
	#for i in poop.knownNPCs:
	#	print(i)
	#print(poop.FamilyBackground())
	cc.CreateCharacter()
	# ^^^ DEBUG ^^^
	'''
	rootLayout = ttk.TTkGridLayout()
	root = ttk.TTk(layout=rootLayout)
	mainWin = ttk.TTkFrame(parent=root, pos=(0, 0), title="", border=True)

	ttk.TTkLabel(parent=mainWin,
				 pos=(1, 1),
				 text="NCPD Punk B.U.S.T.R. - powered by WorldSat",
				 alignment=ttk.TTkK.CENTER_ALIGN)

	def _close(btn):
		btn.close()
		root.update()

	def _test(btn):
		secondWin = ttk.TTkWindow(parent=mainWin,
								  pos=(4, 4),
								  size=(30, 10),
								  title="Shit",
								  border=True)
		secondWin.menubarTop().addMenu(
			"&X",
			alignment=ttk.TTkK.RIGHT_ALIGN).menuButtonClicked.connect(_close)
		secondWin.menubarTop().addMenu("TESTSETSET",
									   alignment=ttk.TTkK.LEFT_ALIGN)
		secondFrame = ttk.TTkFrame(parent=secondWin,
								   title="TESTING",
								   border=True,
								   size=(20, 8),
								   pos=(1, 1))

		secondFrame.addWidget(
			ttk.TTkLabel(parent=secondFrame, pos=(2, 2), text="poop"))
		secondWin.addWidget(
			ttk.TTkLabel(parent=secondFrame, pos=(10, 10), text="oh wow"))

	"""Character"""

	def _character(character=None):
		cc.fullSheet(character)

	mainWin.menubarTop().addMenu("Campaign").menuButtonClicked.connect(_test)
	mainWin.menubarTop().addMenu("Players")
	mainWin.menubarTop().addMenu("Characters").menuButtonClicked.connect(
		_character)

	root.mainloop()


def mainWinSAVED():
	rootLayout = ttk.TTkGridLayout()
	root = ttk.TTk(layout=rootLayout)
	mainWin = ttk.TTkWindow(parent=root,
							pos=(0, 0),
							title="NCPD Punk B.U.S.T.R. - powered by WorldSat",
							border=True)

	ttk.TTkLabel(parent=mainWin, pos=(5, 5), text="Hello World")

	def _test(btn):
		secondWin = ttk.TTkWindow(parent=mainWin,
								  pos=(4, 4),
								  size=(10, 10),
								  title="Shit",
								  border=True)
		secondWin.menubarTop().addMenu("&X", alignment=ttk.TTkK.RIGHT_ALIGN)
		secondWin.menubarTop().addMenu("TESTSETSET",
									   alignment=ttk.TTkK.LEFT_ALIGN)
		ttk.TTkLabel(parent=secondWin, pos=(2, 2), text="poop")

	mainWin.menubarTop().addMenu("Campaign").menuButtonClicked.connect(_test)
	mainWin.menubarTop().addMenu("Players")
	mainWin.menubarTop().addMenu("Characters")

	root.mainloop()
	'''


if __name__ == "__main__":
	username = ""
	#username = database.database.main(True)
	if username == "":#!= "":
		#try:
		#	charList = db[username + "characters"]
		#except:
		#	pass
		main()
