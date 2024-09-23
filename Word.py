
import random
import tkinter as tk

class Word:
    def __init__(self,text,window) -> None:
        self.text = text
        self.length = len(text)
        self.x_position = -100
        self.y_position = random.randint(0, 200)
        self.window = window
        self.word_label = tk.Label(self.window, text=self.text, font=("Helvetica", 24))   
        self.word_label.place(x=self.x_position, y=self.y_position)
        

    def create_game_over_button(self):
        button = tk.Button(self.window, text="Game Over", command=self.close_window)
        button.pack(pady=20)
    
    def close_window(self):
        self.window.destroy()

    def move_word(self):
        if self.x_position < self.window.winfo_width():
            
            self.x_position += 5
            self.word_label.place(x=self.x_position, y=self.y_position)
            self.window.after(50, self.move_word)
        else:
            self.create_game_over_button()
    