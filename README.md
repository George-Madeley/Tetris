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

## Version History

### v1.0.1

- Created tetris.cpp, Pieces.h, and Pieces.cpp files.
- Created the two arrays storing each pieces rotation and their displacement on spawn
- Created a pieces class used to store the data of the pieces.
- Created three methods used to get the block type, horizontal displacement, and vertical displacement.

### v1.0.0

- Repo Initialised.
