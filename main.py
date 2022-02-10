from multiprocessing.connection import wait
from Game import Game
from Pieces import Pieces
from Board import Board
import datetime
import keyboard

# Time between each movement in milliseconds
WAIT_TIME = 700

def main():
    mPieces = Pieces()
    mBoard = Board(mPieces)
    mGame = Game(mBoard, mPieces)

    mTime1 = datetime.datetime.now().time()

    while (not keyboard.is_pressed("ESC")):
        mGame.DrawScene()

        if keyboard.is_pressed("d"):
            if mBoard.IsPossibleMovement(mGame.mPosX - 1, mGame.mPosY, mGame.mPiece, mGame.mRotation):
                mGame.mPosX += 1
        elif keyboard.is_pressed("a"):
            if mBoard.IsPossibleMovement(mGame.mPosX - 1, mGame.mPosY, mGame.mPiece, mGame.mRotation):
                mGame.mPosX -= 1
        elif keyboard.is_pressed("s"):
            if mBoard.IsPossibleMovement(mGame.mPosX, mGame.mPosY + 1, mGame.mPiece, mGame.mRotation):
                mGame.mPosY += 1
        elif keyboard.is_pressed("space"):
            # Check collision from up to down
            while mBoard.IsPossibleMovement(mGame.mPosX, mGame.mPosY, mGame.mPiece, mGame.mRotation):
                mGame.mPosY += 1
            mBoard.StorePiece(mGame.mPosX, mGame.mPosY - 1, mGame.mPiece, mGame.mRotation)
            mBoard.DeletePossibleLines()
            if (mBoard.IsGameOver):
                quit()
            mGame.CreateNewPiece()
        elif keyboard.is_pressed("w"):
            if (mBoard.IsPossibleMovement(mGame.mPosX, mGame.mPosY, mGame.mPiece, (mGame.mRotation + 1) % 4)):
                mGame.mRotation = (mGame.mRotation + 1) % 4

        # —– Vertical movement —–
        mTime2 = datetime.datetime.now().time()
        commonDate = datetime.date(1, 1, 1)
        dateTime1 = datetime.datetime.combine(commonDate, mTime1)
        dateTime2 = datetime.datetime.combine(commonDate, mTime2)
        dateTimeDifference = dateTime2 - dateTime1
        print(dateTimeDifference)
        if dateTimeDifference > datetime.timedelta(0,0,0, WAIT_TIME):
            if mBoard.IsPossibleMovement(mGame.mPosX, mGame.mPosY + 1, mGame.mPiece, mGame.mRotation):
                print("True")
                mGame.mPosY += 1
            else:
                print("False")
                mBoard.StorePiece(mGame.mPosX, mGame.mPosY, mGame.mPiece, mGame.mRotation)
                mBoard.DeletePossibleLines()
                if mBoard.IsGameOver():
                    exit(0)
                mGame.CreateNewPiece()
            mTime1 = datetime.datetime.now().time()

main()
