from tkinter import *

# from MainMenuGUI import MainMenuGui
from MainMenuGUI import MainMenuGui
from DataToStorageManagement import LoadShopFromStorage

# import json


shopData = LoadShopFromStorage()
root = Tk()
root.title("Data Structure Assignment")
# root.configure(background="Cyan")
root.configure(background="DeepSkyBlue")
# root.configure(background="yellow")
# root.iconbitmap()
root.geometry("1100x640+200+100")

MainMenuGui(root, shopData)

root.mainloop()
