from Game import Game
from Pieces import Pieces
from Board import Board
from datetime import datetime
from keyboard import keyboard

WAIT_TIME

def main():
    mScreenHeight = 100
    mPieces = Pieces()
    mBoard = Board(mPieces, mScreenHeight)
    mGame = Game(mBoard, mPieces, mScreenHeight)

    mTime1 = datetime.now().time()

    while (keyboard.read_key() != "ESC"):
        mGame.DrawScene()
        
        key = keyboard.read_key()
        match key:
            case "d":
                if mBoard.IsPossibleMovement(mGame.mPosX - 1, mGame.mPosY, mGame.mPiece, mGame.mRotation):
                    mGame.mPosX += 1
            case "a":
                if mBoard.IsPossibleMovement(mGame.mPosX - 1, mGame.mPosY, mGame.mPiece, mGame.mRotation):
                    mGame.mPosX -= 1
            case "s":
                if mBoard.IsPossibleMovement(mGame.mPosX, mGame.mPosY + 1, mGame.mPiece, mGame.mRotation):
                    mGame.mPosY += 1
            case "space":
                # Check collision from up to down
                while mBoard.IsPossibleMovement(mGame.mPosX, mGame.mPosY, mGame.mPiece, mGame.mRotation):
                    mGame.mPosY += 1
                mBoard.StorePiece(mGame.mPosX, mGame.mPosY - 1, mGame.mPiece, mGame.mRotation)
                mBoard.DeletePossibleLines()
                if (mBoard.IsGameOver):
                    quit()
                mGame.CreateNewPiece()
            case "w":
                if (mBoard.IsPossibleMovement(mGame.mPosX, mGame.mPosY, mGame.mPiece, (mGame.mRotation + 1) % 4)):
                    mGame.mRotation = (mGame.mRotation + 1) % 4

    # —– Vertical movement —–
    mTime2 = datetime.now().time()
    if mTime1 - mTime2 > WAIT_TIME:
        if mBoard.IsPossibleMovement(mGame.mPosX, mGame.mPosY + 1, mGame.mPiece, mGame.mRotation):
            mGame.mPosY += 1
        else:
            mBoard.StorePiece(mGame.mPosX, mGame.mPosY, mGame.mPiece, mGame.mRotation)
            mBoard.DeletePossibleLines()
            if mBoard.IsGameOver():
                exit(0)
            mGame.CreateNewPiece()
        mTime1 = datetime.now().time()
