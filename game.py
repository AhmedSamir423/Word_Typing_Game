import tkinter as tk
from Word import *

window = tk.Tk()
window.title("Moving Word")
window.geometry("500x200")

word1 = Word("Hello",window)
word1.move_word()

word2 = Word("World",window)
word2.move_word()

window.mainloop()
