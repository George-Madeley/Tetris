# Tetris

## About

I developed this game following a tutorial by Diciembre (Javier Lopez). To follow this tutorial, see <https://javilop.com/gamedev/tetris-tutorial-in-c-platform-independent-focused-in-game-logic-for-beginners/>. I created this game in order to then create an AI that could attempt the beat this game.

This was original planed to be coded in C++ and use SDL to draw to the terminal. However, due to an error within the original code, I was unable to compile the files. This error was related to the SDL package I got from Diciembre's (Javier Lopez) sourcecode. I was unable to solve the error due to the time difference between diciembre's (Javier Lopez) tutorial (2008) and now (Feb 2022). Therefore, I decided to recode this in python. The structure of the code still follows Diciembre (Javier Lopez) original code structure however, some functions have been redacted or redesigned.

## Keys

ESC - Quit the game  
w - Rotate Piece  
a - Move Left  
s - Move Down
d - Move Right  
space - Drop  

## Design

### Pieces

There are seven total pieces in Tetris; square, L, L-mirrored, N, N-mirrored, T, and I. Each piece can be rotated by 90 degrees. Therefore, each piece has four different layouts. An example of this can be seen below:

    {0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0},
    {0, 1, 2, 1, 1},
    {0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0}

Each piece is stored within a 5x5 matrix where the 0s represent nothing, 1s represent the piece, 2s represent the pivot point. The seven pieces along with their four different rotoation positions are stored in a single matrix named `mPieces`.

When a piece spawns in Tetris, it spawns are the very top of the screen. Therefore, you do not see the 0s above the piece as they exist outside o fthe board. However, every piece has a different number of 0s above them. I created an array whcih stored the translation of each piece so that they spawn in the correct position.

A pieces class is used to store these arrays and this class also has three methods used to get the block type, horizontal displacement, and vertical displacement.

### Board

The baord class stores a 2D-array of variable size which stores the pieces on the board. This class also comes with a series of methods:

- `IsFreeBlock()` -  returns true if a given block in the board is free. Returns false if occupied.  
- `IsPossibleMovement()` - returns true if the piece can still move and is not colliding with other pieces on the board.  
- `StorePiece()` - Stores a piece on to the board by looping through the board and the given pieces 5x5 array.  
- `DeletePossibleLines()` - Deletes any lines that should be removed. (aka after a line has been completed)  
- `DeleteLine()` - Deletes a line and moves all the pieces above that line down by 1.  
- `IsGameOver()` - returns true if the game is over.

This class contains an enum with two values, `POS_FREE` and `POS_FILLED`. These values are used to check if a given block on the board is free or filled.

### Game

The game class creates and instance of the board class, initialises it, and draws the board and each pieces to the terminal. The Game class makes use of five methods:

- `DrawScene()` - prints the board and the piece to the terminal.
- `CreateNewPiece()` - sets the current piece to the next piece and resets its position, then selects a new next piece.
- `InitGame()` - Initialises the parameters of the game such as setting the current piece and setting the next piece.

### main

Within the main class, we set up a loop which draws everything at the end of each frame. During these frames, the player has the ability to move the piece. Prior to moving the piece, the program checks if moving the piece is possible. The piece is lowered one block, after a set amount of time. Each time the block is lowered, the program deletes all the lines that have been completed then checks if thhe game is over.

## Version History

### v1.1.6

- Changed the Main function into a class
- imported Pynput.
- Updated playing movement using Pynput

### v1.1.5

- Fixed Spawning issue where game would end after the piece spawns
- Redesigned the board printing system so the piece is only stored on the board after it has been placed.

### v1.1.4

- installed Keyboard
- imported keyboard from keyboard
- Created main.py file
- Added a while loop which allows the game to run and operate.
- Deleted main.cpp
- Deleted IO.h and IO.cpp

ERRORS:
The python version of the game does not run as of yet. This is because the code has been translated from C++ to Python without fixing any python realted errors.

### v1.1.3

- installed NumPy
- imported random from NumPy
- Created Game.py file.
- Added the Game class used to initialise the board and draw the board to the screen
- Added the accompanying methods used to generate the next piece, initalise the board, and to draw the board and pieces to the screen.

### v1.1.2

- Deleted SDL directory
- Deleted Board.cpp and Board.h
- Deleted Pieces.cpp and Pieces.h
- Deleted Tetris.cpp

### v1.1.1

- Created Board.py file.
- Added the Board class used to represent the board.
- Added the accompanying methods used to get or check certain data on the board.

### v1.1.0

- Started changing the code from C++ to Python.
- Created Pieces.py file.
- Added the two arrays storing each pieces rotation and their displacement on spawn
- Added a pieces class used to store the data of the pieces.
- Added three methods used to get the block type, horizontal displacement, and vertical displacement.

### v1.0.6

- Fixed any missing code.
- Fixed any syntax and formatting errors.

ERRORS:
Does not compilig correctly; presumably due to the missing SDL/SDL.h file.

### v1.0.5

- Created the main.cpp file.
- Created a while loop which allows the game to run and operate.

### v1.0.4

- Added the IO.h and IO.cpp files to the directory. These come from diciembre (Javier Lopez) source code as they were required for the completion of the code.

### v1.0.3

- Created the Game.h and Game.cpp files
- Created the Game class used to initialise the board and draw the board to the screen
- Creates the accompanying methods used to generate the next piece, initalise the board, and to draw the board and pieces to the screen.

### v1.0.2

- Created the Board.h and Board.cpp files
- Created the Board class used to represent the board.
- Created the accompanying methods used to get or check certain data on the board.

### v1.0.1

- Created tetris.cpp, Pieces.h, and Pieces.cpp files.
- Created the two arrays storing each pieces rotation and their displacement on spawn
- Created a pieces class used to store the data of the pieces.
- Created three methods used to get the block type, horizontal displacement, and vertical displacement.

### v1.0.0

- Repo Initialised.
