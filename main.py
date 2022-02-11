from Game import Game
from Pieces import Pieces
from Board import Board
from pynput import keyboard
import datetime


class Main:
    def __init__(self):
        self.InitVariables()
        self.PlayTetris()

    def InitVariables(self):
        # Time between each movement in milliseconds
        self.WAIT_TIME = 500
        self.mPieces = Pieces()
        self.mBoard = Board(self.mPieces)
        self.mGame = Game(self.mBoard, self.mPieces)
        self.isPlaying = True

    def on_release(self, key):
        mBoard = self.mBoard
        mGame = self.mGame
        try:
            if key.char == "d" :
                if mBoard.IsPossibleMovement(mGame.mPosX - 1, mGame.mPosY, mGame.mPiece, mGame.mRotation):
                    mGame.mPosX += 1
            elif key.char == "a":
                if mBoard.IsPossibleMovement(mGame.mPosX - 1, mGame.mPosY, mGame.mPiece, mGame.mRotation):
                    mGame.mPosX -= 1
            elif key.char == "s":
                if mBoard.IsPossibleMovement(mGame.mPosX, mGame.mPosY + 1, mGame.mPiece, mGame.mRotation):
                    mGame.mPosY += 1
            elif key.char == "w":
                if (mBoard.IsPossibleMovement(mGame.mPosX, mGame.mPosY, mGame.mPiece, (mGame.mRotation + 1) % 4)):
                    mGame.mRotation = (mGame.mRotation + 1) % 4
        except AttributeError:
            if key == keyboard.Key.space:
                # Check collision from up to down
                while mBoard.IsPossibleMovement(mGame.mPosX, mGame.mPosY, mGame.mPiece, mGame.mRotation):
                    mGame.mPosY += 1
                mBoard.StorePiece(mGame.mPosX, mGame.mPosY - 1, mGame.mPiece, mGame.mRotation)
                mBoard.DeletePossibleLines()
                if (mBoard.IsGameOver()):
                    quit()
                mGame.CreateNewPiece()
            elif key == keyboard.Key.esc:
                self.isPlaying = False

    def PlayTetris(self):
        mBoard = self.mBoard
        mGame = self.mGame

        keyListener = keyboard.Listener(on_release=self.on_release)
        keyListener.start()
        
        mTime1 = datetime.datetime.now().time()

        while (self.isPlaying):
            mGame.DrawScene()

            # —– Vertical movement —–
            mTime2 = datetime.datetime.now().time()
            commonDate = datetime.date(1, 1, 1)
            dateTime1 = datetime.datetime.combine(commonDate, mTime1)
            dateTime2 = datetime.datetime.combine(commonDate, mTime2)
            dateTimeDifference = dateTime2 - dateTime1
            if dateTimeDifference > datetime.timedelta(0,0,0, self.WAIT_TIME):
                if mBoard.IsPossibleMovement(mGame.mPosX, mGame.mPosY + 1, mGame.mPiece, mGame.mRotation):
                    mGame.mPosY += 1
                else:
                    mBoard.StorePiece(mGame.mPosX, mGame.mPosY, mGame.mPiece, mGame.mRotation)
                    mBoard.DeletePossibleLines()
                    if mBoard.IsGameOver():
                        exit(0)
                    mGame.CreateNewPiece()
                mTime1 = datetime.datetime.now().time()

Main()
