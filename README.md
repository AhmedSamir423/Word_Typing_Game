# Word Typing Game

## Overview
The Word Typing Game is an interactive typing game built using Python and Tkinter. Players need to type the moving words correctly before they disappear off the screen. The game tracks the player's score based on the length of the words typed correctly, providing an engaging way to improve typing speed and accuracy.

## Features
- **Dynamic Word Generation**: Words appear randomly and move across the screen.
- **Real-Time Typing Check**: Players can type in a text box, and the game checks their input in real time.
- **Score Tracking**: The score increases based on the length of the correctly typed words.
- **Game Over Screen**: Displays the final score when the game ends.

## Installation

To run this project, you need to have Python installed on your machine. Follow the steps below to set it up:

1. Clone this repository:
   ```bash
   git clone https://github.com/AhmedSamir423/Word_Typing_Game.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Word_Typing_Game
   ```

3. Install the required dependencies (if any). This project primarily uses Tkinter, which comes pre-installed with Python:
   ```bash
   # No additional installation needed for Tkinter
   ```

4. Prepare your dictionary file:
   - Create a file named `dictionary.txt` in the project root directory.
   - Add a list of words, each on a new line.

## Usage

To start the game, run the following command in your terminal:
```bash
python game.py
```

- The game window will open, and words will start moving across the screen.
- Type the words as they appear and press `Enter` to submit.
- Your score will be updated based on the words you type correctly.
- If a word passes the screen without being typed, the game ends, and your final score will be displayed.

## Gameplay Screenshot
![image](https://github.com/user-attachments/assets/0bf92220-0f80-4c9c-ae57-e16ecefee23a)


## Code Structure

```
word_typing_game/
│
├── game.py               # Main game logic
├── Word.py               # Word class handling word display and movement
├── utils.py              # Utility functions (e.g., loading words, game state management)
└── dictionary.txt        # Text file containing the list of words
```

## Contributing
If you'd like to contribute to this project, please fork the repository and submit a pull request. Contributions, suggestions, and feedback are welcome!

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
- Special thanks to [Tkinter](https://docs.python.org/3/library/tkinter.html) for providing the GUI framework.
- Thanks to [OpenAI](https://openai.com) for their assistance during development.

## Contact
For any inquiries, feel free to reach out to me at [your_email@example.com].
```

