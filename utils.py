import random
import tkinter as tk
from Word import Word


score = 0
# Load words from the dictionary file
def load_words():
    with open("dictionary.txt", "r") as file:
        words = file.read().splitlines()
    return words

# Function to check user input
def check_input(event, word_instances, entry,score_label):
    global score
    user_input = entry.get()  # Get the input text from the entry
    for word in word_instances:
        if user_input == word.text:
            score += len(user_input)
            score_label.config(text=f"Score: {score}")
            word.compare_word()  # Call compare_word for the matched word
            word_instances.remove(word)  # Remove the word once matched
            break
    else:
        print("Try again!")  # Feedback for incorrect input
    entry.delete(0, tk.END)  # Clear the entry after checking

# Function to end the game
def end_game(window):
    if window.winfo_exists():  # Check if the window still exists
        window.destroy()  # Close the main game window
    game_over = tk.Tk()
    game_over.title("Game Over")
    game_over.geometry("300x100")
    game_over.configure(bg="black")
    text = tk.Label(game_over, text="Game Over", font=("Helvetica", 24), fg="white", bg="black")
    text.pack(pady=20)
    score = tk.Label(game_over, text=f"Your score is {score}", font=("Helvetica", 16), fg="white", bg="black")
    score.pack(pady=10)
    game_over.after(3000, game_over.destroy)

def create_new_word(words_list, window, entry, word_instances):
    new_word = Word(random.choice(words_list), window, entry,lambda: end_game(window))
    new_word.move_word()
    word_instances.append(new_word)  # Add the new word to the list
    window.after(2000, create_new_word, words_list, window, entry, word_instances)

# Function to start the game
def start_game():
    # Load words from the file
    words_list = load_words()

    # Create the main window
    window = tk.Tk()
    window.title("Moving Word")
    window.geometry("500x200")

    # Create an entry widget for user input
    score_label = tk.Label(window, text="Your score is :", font=("Helvetica", 16), fg="white", bg="black")
    score_label.pack(pady=20)
    entry = tk.Entry(window)
    entry.pack(pady=20)

    word_instances = []

    # Bind the Enter key to the check_input function
    entry.bind("<Return>", lambda event: check_input(event, word_instances, entry,score_label=score_label))

    # Start creating words every 1 second
    create_new_word(words_list, window, entry, word_instances)

    # Start the Tkinter loop
    window.mainloop()
