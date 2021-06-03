"""
Definitions of each of the different chess pieces.
"""

from abc import ABC, abstractmethod

from chessington.engine.data import Player, Square

class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player):
        self.player = player

    @abstractmethod
    def get_available_moves(self, board):
        """
        Get all squares that the piece is allowed to move to.
        """
        pass

    def move_to(self, board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """

    def isFirstMove(self, current_square): 
        if self.player== Player.White:
            if current_square.row == 1:
                return True
        elif self.Player == Player.Black:
            if current_square.row == 6:
                return True
        else: return False



    def get_available_moves(self, board):
        # get pawn location
        current_square = board.find_piece(self)
        # check if something is in the way (1 tile away), is_piece_blocked(self, blocking_coordinate)
        # if nothing in the way, add pawn +1 to available moves

        #check if it's first move, if it is then consider moving 2 spaces, and if anything is blocking the 2 space move
        if (Pawn.isFirstMove(self, current_square)):


    

        new_squares = []

        if  self.player == Player.WHITE:
            if board.get_piece(Square.at(current_square.row+1, current_square.col)):
                return []
            if  current_square.row == 1:
                new_squares.append(Square.at(current_square.row + 1, current_square.col))
                if board.get_piece(Square.at(current_square.row+2, current_square.col)):
                    return new_squares
                new_squares.append(Square.at(current_square.row + 2, current_square.col))
            else:
                new_squares.append(Square.at(current_square.row + 1, current_square.col))
        else:
            if board.get_piece(Square.at(current_square.row-1, current_square.col)):
                return []
            if  current_square.row == 6:
                new_squares.append(Square.at(current_square.row - 1, current_square.col))
                if board.get_piece(Square.at(current_square.row-2, current_square.col)):
                    return new_squares
                new_squares.append(Square.at(current_square.row - 2, current_square.col))
            else:
                new_squares.append(Square.at(current_square.row - 1, current_square.col))
        return new_squares

   





# @dataclass(frozen=True)
# class Square:
#     row: int
#     col: int

#     @classmethod
#     def at(cls, row: int, col: int):
#         """
#         Provides backward compatibility with previous namedtuple implementation.

#         Square.at(...) is equivalent to Square(...).
#         """

#         return cls(row=row, col=col)








class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        return []


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        return []


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        return []


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        return []


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        return []