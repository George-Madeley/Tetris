import random
from Pieces import Pieces
from Board import BOARD_HEIGHT, PIECE_BLOCKS, Board, BOARD_WIDTH
import os


class Game:
    def __init__(self, pBoard, pPieces):
        self.__mBoard = pBoard
        self.__mPieces = pPieces

        self.mPiece = random.randint(0, 6)
        self.mRotation = random.randint(0, 3)
        self.mPosX = int((BOARD_WIDTH / 2) + self.__mPieces.GetXInitialPosition(self.mPiece, self.mRotation))
        self.mPosY = self.__mPieces.GetYInitialPosition(self.mPiece, self.mRotation)

        self.__mNextPiece = random.randint(0, 6)
        self.__mNextRotation = random.randint(0, 3)

    def CreateNewPiece(self):
        """
        Create a random piece
        """
        # The new piece
        self.mPiece = self.__mNextPiece
        self.mRotation = self.__mNextRotation
        self.mPosX = int((BOARD_WIDTH / 2) + self.__mPieces.GetXInitialPosition(self.mPiece, self.mRotation))
        self.mPosY = self.__mPieces.GetYInitialPosition(self.mPiece, self.mRotation)
        # random next piece
        self.__mNextPiece = random.randint(0, 6)
        self.__mNextRotation = random.randint(0, 3)

    def __DrawPiece(self, pX, pY, pPiece, pRotation) -> None:
        """
        Draw piece

        Parameters:
        - int pX: Horizontal position in blocks
        - int pY: Vertical position in blocks
        - int pPiece: Piece to draw
        - int pRotation: 1 of the 4 possible rotations
        """
        for i in range(PIECE_BLOCKS):
            for j in range(PIECE_BLOCKS):
                blockType = self.__mPieces.GetBlockType(pPiece, pRotation, j, i)
                if blockType != 0:
                    self.__mBoard[j][i] = blockType

    def DrawScene(self):
        """
        Draw scene

        Draw all the objects of the scene
        """
        # Clear the terminal
        os.system('cls' if os.name == 'nt' else 'clear')

        board = self.__mBoard.GetBoard()
        for j1 in range(len(board)):
            for i1 in range(BOARD_WIDTH):
                if j1 >= self.mPosY and j1 < self.mPosY + PIECE_BLOCKS and i1 >= self.mPosX and i1 < self.mPosX + PIECE_BLOCKS:
                    blockXCoord = i1 - self.mPosX
                    blockYCoord = j1 - self.mPosY
                    blockPiece = self.__mPieces.GetBlockType(self.mPiece, self.mRotation, blockYCoord, blockXCoord)
                    if blockPiece != 0:
                        print(str(blockPiece), end="")
                        pass
                    else:
                        if board[j1][i1] == 0:
                            print("-", end="")
                        else:
                            print("X", end="")
                else:
                    if board[j1][i1] == 0:
                        print("-", end="")
                    else:
                        print("X", end="")
            print("\n", end="")
    