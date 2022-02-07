from enum import Enum

class POS(enum):
    FREE = 0
    FILLED = 1

# -- Defines --

# Width of each of the two lines that delimit the board
BOARD_LINE_WIDTH = 6
# Width ond Height of each block of a piece
BLOCK_SIZE = 16
# Center position of the board from the left of the screen
BOARD_POSITION = 320
# Board width in blocks
BOARD_WIDTH = 10
# Board height in blocks
BOARD_HEIGHT = 20
# Minimum vertical mergin for the board limit
MIN_VERTICAL_MARGIN = 20
# Minimum horizontal margin for the board limit
MIN_HORIZONTAL_MARGIN = 20
# Number of horizontal and vertical blocks of a matrix piece
PIECE_BLOCKS = 5

class Board:
    def __init__(self, pPieces, pScreenHeight):
        self.mBoard = [[POS.FREE for i in range(BOARD_WIDTH)] for j in range(BOARD_HEIGHT)]
        self.mScreenHeight = pScreenHeight
        self.mPieces = pPieces
        for i in range(BOARD_WIDTH):
            for j in range(BOARD_HEIGHT):
                self.mBoard[i][j] = POS.FREE

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
                if self.mPieces.GetBlockType(pPiece, pRotation, j2, i2) != 0:
                    self.mBoard[i1][j1] = POS.FILLED
                j2 += 1
            i2 += 1

    def IsGameOver(self):
        """
        Check if the game is over becase a piece have achived the upper position

        Returns true or false
        """
        # If the first line has blocks, then, game over
        for i in range(BOARD_WIDTH):
            if self.mBoard[i][0] == POS.FILLED:
                return True
        return False

    def DeleteLine(self, pY):
        """
        Delete a line of the board by moving all above lines down

        Parameters:
        - int pY: Vertical position in blocks of the line to delete
        """
        # Moves all the upper lines one row down
        for j in range(pY, 0, -1):
            for i in range(BOARD_WIDTH):
                self.mBoard[i][j] = self.mBoard[i][j-1]

    def DeletePossibleLines(self):
        """
        Delete all the lines that should be removed
        """
        for j in range(BOARD_HEIGHT):
            i = 0
            while i < BOARD_WIDTH:
                if self.mBoard[i][j] != POS.FILLED:
                    break
                i += 1
            if i == BOARD_WIDTH:
                self.DeleteLine(j)

    def IsFreeBlock(self, pX, pY):
        """
        Returns 1 (true) if the this block of the board is empty, 0 if it is filled

        Parameters:
        - int pX: Horizontal position in blocks
        - int pY: Vertical position in blocks
        """
        if self.mBoard[pX][pY] == POS.FREE:
            return True
        else:
            return False

    def GetXPosInPixels(self, pPos):
        """
        Returns the horizontal position (in pixels) of the block given like parameter

        Parameters:
        - int pPos: Horizontal position of the block in the board
        """
        return ((BOARD_POSITION - (BLOCK_SIZE * (BOARD_WIDTH / 2))) + (pPos * BLOCK_SIZE))

    def GetYPosInPixels(self, pPos):
        """
        Returns the vertical position (in pixels) of the block given like parameter

        Parameters:
        - int pPos: Horizontal position of the block in the board
        """
        return ((self.mScreenHeight - (BLOCK_SIZE * BOARD_HEIGHT)) + (pPos * BLOCK_SIZE))

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
                    if self.mPieces.GetBlockType(pPiece, pRotation, j2, i2) != 0:
                        return False
                # Check if the piece have collisioned with a block already stored in the map
                if j1 >= 0:
                    if self.mPieces.GetBlockType(pPiece, pRotation, j2, i2) != 0 and not self.IsFreeBlock(i1, j1):
                        return False
                j2 += 1
            i2 += 1
        # No collision
        return True