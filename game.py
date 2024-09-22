import tkinter as tk


def move_word():
    global x_position
    if x_position < window.winfo_width():
        
        x_position += 5
        word_label.place(x=x_position, y=50)
        
        window.after(50, move_word)
    else:
        
        create_game_over_button()


def close_window():
    window.destroy()


def create_game_over_button():
    button = tk.Button(window, text="Game Over", command=close_window)
    button.pack(pady=20)


window = tk.Tk()
window.title("Moving Word")
window.geometry("500x200")


x_position = -100


word_label = tk.Label(window, text="Word", font=("Helvetica", 24))
word_label.place(x=x_position, y=50)


move_word()


window.mainloop()
