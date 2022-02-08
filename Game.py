from random import Random
from numpy import random
import Pieces
import Board


class Game:
    def __init__(self, pBoard, pPieces, pScreenHeight):
        self.mScreenHeight = pScreenHeight
        self.mBoard = pBoard
        self.mPieces = pPieces

        self.mPiece = random.randint(6)
        self.mRotation = random.randint(3)
        self.mPosX = (BOARD_WIDTH / 2) + self.mPieces.GetXInitialPosition(self.mPiece, self.mRotation)
        self.mPosY = self.mPieces.GetYInitialPosition(self.mPiece, self.mRotation)

        self.mNextPiece = random.randint(6)
        self.mNextRotation = random.randit(3)
        self.mNextPosX = BOARD_WIDTH + 5
        self.mNextPosY = 5

    def CreateNewPiece(self):
        """
        Create a random piece
        """
        # The new piece
        self.mPiece = self.mNextPiece
        self.mRotation = self.mNextRotation
        self.mPosX = (BOARD_WIDTH / 2) + self.mPieces.GetXInitialPosition(self.mPiece, self.mRotation)
        self.mPosY = self.mPieces.GetYInitialPosition(self.mPiece, self.mRotation)
        # random next piece
        self.mNextPiece = random.randint(6)
        self.mNextRotation = random.randint(3)

    def DrawPiece(self, pX, pY, pPiece, pRotation) -> None:
        """
        Draw piece

        Parameters:
        - int pX: Horizontal position in blocks
        - int pY: Vertical position in blocks
        - int pPiece: Piece to draw
        - int pRotation: 1 of the 4 possible rotations
        """
        pass

    def DrawBoard(self) -> None:
        """
        Draw board

        Draw the two lines that delimit the board
        """
        pass

    def DrawScene(self):
        """
        Draw scene

        Draw all the objects of the scene
        """
        # Draw the delimitation lines and blocks stored in the board
        self.DrawBoard()
        # Draw the playing piece
        self.DrawPiece(self.mPosX, self.mPosY, self.mPiece, self.mRotation)
        # Draw the next piece
        self.DrawPiece(self.mNextPosX, self.mNextPosY, self.mNextPiece, self.mNextRotation)
    