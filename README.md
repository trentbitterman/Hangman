# Hangman  

The game of hangman written in Python!  

## Structure  

The repository is split into two sections, 
the resources directory and the python files. 

### Resources  

The resources directory holds all of the word lists
sorted by difficulty level and compressed in the xz 
format to save space, and a small python script to 
take a large word list and split it up into smaller files 
by length.  

### Python Files  

The python files are made up of four files, each with distinct 
purposes.  

#### initialize_game.py  

The initialize_game.py file houses functions responsible 
for asking the player required questions to set up the game state, 
such as word length and what difficulty they want to play at.  

#### print_hangman.py  

The print_hangman.py file houses functions responsible 
for printing the current state of the hangman after the 
player has responded to the computer querying for if its 
guess was correct.  

#### finding_word.py  
The finding_word.py file houses functions responsible 
for determining what word the player is thinking of. 
It does this by removing words from the word list based 
on the player's responses to the computer's questions.  

#### hangman.py  
This is the file that stores the main function that starts 
and controls the game state. This is where the main game logic 
is held.  

Note: This program requires Python 3.
