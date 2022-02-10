class Pieces:
    def __init__(self):
        self.__mPieces = [
            # Square
            [
                [
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 2, 1, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 0, 0]
                ],
                [
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 2, 1, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 0, 0]
                ],
                [
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 2, 1, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 0, 0]
                ],
                [
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 2, 1, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 0, 0]
                ]
            ],
            # I
            [
                [
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 1, 2, 1, 1],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]
                ],
                [
                    [0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 2, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0]
                ],
                [
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [1, 1, 2, 1, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]
                ],
                [
                    [0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 2, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0]
                ]
            ],
            # L
            [
                [
                    [0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 2, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 0, 0]
                ],
                [
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 1, 2, 1, 0],
                    [0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0]
                ],
                [
                    [0, 0, 0, 0, 0],
                    [0, 1, 1, 0, 0],
                    [0, 0, 2, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0]
                ],
                [
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 2, 1, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]
                ]
            ],
            # L mirrored
            [
                [
                    [0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 2, 0, 0],
                    [0, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0]
                ],
                [
                    [0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 0],
                    [0, 1, 2, 1, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]
                ],
                [
                    [0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 2, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0]
                ],
                [
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 1, 2, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 0]
                ]
            ],
            # N
            [
                [
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0],
                    [0, 0, 2, 1, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0]
                ],
                [
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 1, 2, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 0, 0]
                ],
                [
                    [0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 1, 2, 0, 0],
                    [0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0]
                ],

                [
                    [0, 0, 0, 0, 0],
                    [0, 1, 1, 0, 0],
                    [0, 0, 2, 1, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]
                ]
            ],
            # N mirrored
            [
                [
                    [0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 2, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 0]
                ],
                [
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 2, 1, 0],
                    [0, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0]
                ],
                [
                    [0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0]
                ],
                [
                    [0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 1, 2, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]
                ]
            ],
            # T
            [
                [
                    [0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 2, 1, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0]
                ],
                [
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 1, 2, 1, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0]
                ],
                [
                    [0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 1, 2, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0]
                ],
                [
                    [0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 1, 2, 1, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]
                ]
            ]
        ]
        self.__mPiecesInitialPosition = [
            # Square
            [
                [-2, -3],
                [-2, -3],
                [-2, -3],
                [-2, -3]
            ],
            # I
            [
                [-2, -2],
                [-2, -3],
                [-2, -2],
                [-2, -3]
            ],
            # L
            [
                [-2, -3],
                [-2, -3],
                [-2, -3],
                [-2, -2]
            ],
            # L Mirrored
            [
                [-2, -3],
                [-2, -2],
                [-2, -3],
                [-2, -3]
            ],
            # N
            [
                [-2, -3],
                [-2, -3],
                [-2, -3],
                [-2, -2]
            ],
            # N mirrored
            [
                [-2, -3],
                [-2, -3],
                [-2, -3],
                [-2, -2]
            ],
            # T
            [
                [-2, -3],
                [-2, -3],
                [-2, -3],
                [-2, -2]
            ]
        ]

    
    def GetBlockType(self, pPiece, pRotation, pX, pY):
        """
        Return the type of a block (0 = no-block, 1 = normal block, 2 = pivot block)

        Parameters:
        - int pPiece:       Piece to draw
        - int pRotation:    1 of the 4 possible rotations
        - int pX:           Horizontal position in blocks
        - int pY:           Vertical position in blocks
        """
        return self.__mPieces[pPiece][pRotation][pX][pY]

    
    def GetXInitialPosition(self, pPiece, pRotation):
        """
        Returns the horizontal displacement of the piece that has to be applied in order to create it in the
        correct position.

        Parameters:
        - int pPiece:       Piece to draw
        - int pRotation:    1 of the 4 possible rotations
        """
        return self.__mPiecesInitialPosition[pPiece][pRotation][0]

    
    def GetYInitialPosition(self, pPiece, pRotation):
        """
        Returns the vertical displacement of the piece that has to be applied in order to create it in the
        correct position.

        Parameters:
        - int pPiece:       Piece to draw
        - int pRotation:    1 of the 4 possible rotations
        """
        return self.__mPiecesInitialPosition[pPiece][pRotation][1]