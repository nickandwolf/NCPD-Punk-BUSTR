import tkinter as tk


class Player:
    def __init__(self, name):
        self.name = name
        self.characters = []

    def AddCharacter(self, character):
        if character not in self.characters:
            self.characters.append(character)

    def RemoveCharacter(self, character):
        if character in self.characters:
            self.characters.pop(character)


class PlayerFrame(tk.Frame):
    def __init__(self, master, player=None):
        self.master = master
        self.currentPlayer = player
        if self.currentPlayer == None:
            self.currentPlayer = Player("")
        self._GenerateFrame()

    def _GenerateFrame(self):
        nameTV = tk.StringVar()
        nameTV.set(self.currentPlayer.name)
        nameE = tk.Entry(self.master, text=nameTV)
        nameE.grid()
