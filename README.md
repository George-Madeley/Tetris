# Tetris

## About

I developed this game following a tutorial by diciembre (Javier Lopez). To follow this tutorial, see <https://javilop.com/gamedev/tetris-tutorial-in-c-platform-independent-focused-in-game-logic-for-beginners/>.

## Keys

ESC - Quit the game
z - Rotate Piece
x - Drop Piece

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

- `GetXPosInPixels()` - which returns the horizontal position of a given block. This is used to draw the blocks on to the screen.  
- `GetYPosInPixels()` - which returns the vertical position of a given block. This is used to draw the blocks on to the screen.  
- `IsFreeBlock()` -  returns true if a given block in the board is free. Returns false if occupied.  
- `IsPossibleMovement()` - returns true if the piece can still move and is not colliding with other pieces on the board.  
- `StorePiece()` - Stores a piece on to the board by looping through the board and the given pieces 5x5 array.  
- `DeletePossibleLines()` - Deletes any lines that should be removed. (aka after a line has been completed)  
- `DeleteLine()` - Deletes a line and moves all the pieces above that line down by 1.  
- `IsGameOver()` - returns true if the game is over.

This class contains an enum with two values, `POS_FREE` and `POS_FILLED`. These values are used to check if a given block on the board is free or filled.

## Version History

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
