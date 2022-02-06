#ifndef _GAME_
#define _GAME_

// —— Includes —–

#include "Board.h"
#include "Pieces.h"
#include "io.h"
#include <time.h>

// —— Defines —–

// Number of milliseconds that the piece remains before going one block down
#define WAIT_TIME 700

// ——————————————————————————–
// Game
// ——————————————————————————–

class Game {
    public:
        Game(Board *pBoard, Pieces *pPieces, io *pIO, int pScreenHeight);

        void DrawScene();
        void CreateNewPiece();

        // Position of the Piece falling down
        int mPosX, mPosY;
        // King and rotation the piece that is falling down
        int mPiece, mRotation;

    private:
        // Screen height in pixels
        int mScreenHeight;
        // Position of the next piece
        int mNextPosX, mNextPosY;
        // Kind and rotation of the next piece
        int mNextPiece, mNextRotation;

        Board *mBoard;
        Pieces *mPieces;
        IO *mIO;

        int GetRand(int pA, int pB);
        void InitGame();
        void DrawPiece(int pX, int pY, int pPiece, int pRotation);
        void DrawBoard();
};

#endif // _Game_