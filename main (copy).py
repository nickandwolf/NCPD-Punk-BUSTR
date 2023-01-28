import tkinter as tk
from tkinter import ttk
import player.player as pp


class Frame(tk.Tk):
    def __init__(self, master):
        self.master = master
        super().__init__(self.master)
        self.didSave = False

    def RemoveFrame(self):
        self.forget()
        #something about double checking if they want to save first


class Main:
    def __init__(self, master):
        self.master = master
        master.title("WorldSat C.P.2.0.2.0.")
        self._MenuBar()
        #self.currentFrame = tk.Frame(self.master)
        self.currentFrame = pp.PlayerFrame(self.master)
        self.currentFrame.grid(row=1, columnspan=5)

    def _MenuBar(self):
        self.menuBar = []
        campaignMB = tk.Menubutton(self.master, text="Campaign")
        campaignMB.grid(row=0, column=0)
        campaignMB.menu = tk.Menu(campaignMB, tearoff=0)
        campaignMB["menu"] = campaignMB.menu

        campaignMB.menu.add_command(label="New")
        campaignMB.menu.add_command(
            label="Load")  #make it auto-load other campaigns
        campaignMB.menu.add_command(label="Delete")

        playerMB = tk.Menubutton(self.master, text="Player")
        playerMB.grid(row=0, column=1)
        playerMB.menu = tk.Menu(playerMB, tearoff=0)
        playerMB["menu"] = playerMB.menu

        playerMB.menu.add_command(label="New")
        playerMB.menu.add_command(
            label="Load")  #make it auto-load other campaigns
        playerMB.menu.add_command(label="Delete")

        characterMB = tk.Menubutton(self.master, text="Character")
        characterMB.grid(row=0, column=2)
        characterMB.menu = tk.Menu(characterMB, tearoff=0)
        characterMB["menu"] = characterMB.menu

        characterMB.menu.add_command(label="New")
        characterMB.menu.add_command(
            label="Load")  #make it auto-load other campaigns
        characterMB.menu.add_command(label="Delete")


if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.mainloop()
