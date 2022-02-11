# -- Defines --
# Board width in blocks
BOARD_WIDTH = 10
# Board height in blocks
BOARD_HEIGHT = 20
# Number of horizontal and vertical blocks of a matrix piece
PIECE_BLOCKS = 5

class Board:
    def __init__(self, pPieces):
        self.__mBoard = [[0 for i in range(BOARD_WIDTH)] for j in range(BOARD_HEIGHT)]
        self.__mPieces = pPieces

    def GetBoard(self):
        """
        Returns the board
        """
        return self.__mBoard

    def StorePiece(self, pX, pY, pPiece, pRotation):
        """
        Store a piece in the board by filling the blocks

        Parameters:
        - int pX:           Horizontal position in blocks
        - int pY:           Vertical position in blocks
        - int pPiece:       Piece to draw
        - int pRotation:    1 of the 4 possible rotations
        """
        # Store each block of the piece into the board
        i2 = 0
        for i1 in range(pX, pX + PIECE_BLOCKS):
            j2 = 0
            for j1 in range(pY, pY + PIECE_BLOCKS):
                # Store only the blocks of the piece that are not holes
                if i1 < 0 or i1 > BOARD_WIDTH - 1 or j1 < 0 or j1 > BOARD_HEIGHT - 1:
                    j2 += 1
                    continue 
                if self.__mPieces.GetBlockType(pPiece, pRotation, j2, i2) != 0:
                    self.__mBoard[j1][i1] = 1
                j2 += 1
            i2 += 1

    def IsGameOver(self):
        """
        Check if the game is over becase a piece have achived the upper position

        Returns true or false
        """
        # If the first line has blocks, then, game over 
        for i in range(BOARD_WIDTH):
            if self.__mBoard[0][i] == 1:
                return True
        return False

    def __DeleteLine(self, pY):
        """
        Delete a line of the board by moving all above lines down

        Parameters:
        - int pY: Vertical position in blocks of the line to delete
        """
        # Moves all the upper lines one row down
        for j in range(pY, 0, -1):
            for i in range(BOARD_WIDTH):
                self.__mBoard[j][i] = self.__mBoard[j-1][i]

    def DeletePossibleLines(self):
        """
        Delete all the lines that should be removed
        """
        for j in range(BOARD_HEIGHT):
            i = 0
            while i < BOARD_WIDTH:
                if self.__mBoard[j][i] != 1:
                    break
                i += 1
            if i == BOARD_WIDTH:
                self.__DeleteLine(j)

    def IsFreeBlock(self, pX, pY):
        """
        Returns 1 (true) if the this block of the board is empty, 0 if it is filled

        Parameters:
        - int pX: Horizontal position in blocks
        - int pY: Vertical position in blocks
        """
        if self.__mBoard[pY][pX] == 0:
            return True
        else:
            return False

    def IsPossibleMovement(self, pX, pY, pPiece, pRotation):
        """
        Check if the piece can be stored at this position without any collision
        Returns true if the movement is possible, false if it not possible

        Parameters:
        - int pX: Horizontal position in blocks
        - int pY: Vertical position in blocks
        - int pPiece: Piece to draw
        - int pRotation: 1 of the 4 possible rotations
        """
        
        # Checks collision with pieces already stored in the board or the board limits
        # This is just to check the 5×5 blocks of a piece with the appropriate area in the board
        i2 = 0
        for i1 in range(pX, pX + PIECE_BLOCKS):
            j2 = 0
            for j1 in range(pY, pY + PIECE_BLOCKS):
                # Check if the piece is outside the limits of the board
                if i1 < 0 or i1 > BOARD_WIDTH - 1 or j1 > BOARD_HEIGHT - 1:
                    if self.__mPieces.GetBlockType(pPiece, pRotation, j2, i2) != 0:
                        return False
                # Check if the piece have collisioned with a block already stored in the map
                if j1 >= 0:
                    if self.__mPieces.GetBlockType(pPiece, pRotation, j2, i2) != 0 and not self.IsFreeBlock(i1, j1):
                        return False
                j2 += 1
            i2 += 1
        # No collision
        return True