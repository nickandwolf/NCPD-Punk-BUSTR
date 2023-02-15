'''
Night City Police Department 'Punk' B.U.S.T.R.
Official Name: Biotelemetric Unlocated Scene Threat Reposity
AKA Beat Up Street Trash Repository

https://towardsdatascience.com/finding-performance-bottlenecks-in-python-4372598b7b2c (when finalized)
'''

import sys
import importlib
import saveLoadExport as sle

def main(GUI=None):
	''' Different versions go here '''
	commands = ["pytermtk","tkinter"]
	gui = None
	args = []
	if len(sys.argv) < 2:
		args = 'pytermtk'
	else:
		args = sys.argv[1]
		
	try:
		gui = importlib.import_module(args + '.landing')
	except:
		gui = importlib.import_module('tkinter')

	gui.main()
		
if __name__ == "__main__":
	main()
