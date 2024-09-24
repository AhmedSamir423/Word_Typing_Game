import random
import tkinter as tk

class Word:
    def __init__(self, text, window, entry, end_game_callback) -> None:
        self.text = text
        self.x_position = -100
        self.y_position = random.randint(10, 150)
        self.window = window
        self.entry = entry
        self.end_game_callback = end_game_callback # Callback to end the game
        self.word_label = tk.Label(self.window, text=self.text, font=("Helvetica", 24))
        self.word_label.place(x=self.x_position, y=self.y_position)

    def move_word(self):
        if self.x_position < self.window.winfo_width():
            self.x_position += 5
            self.word_label.place(x=self.x_position, y=self.y_position)
            self.window.after(50, self.move_word)
        else:
            self.end_game_callback()  # Trigger game over callback

    def compare_word(self):
        print("Correct!")
        self.word_label.destroy()
