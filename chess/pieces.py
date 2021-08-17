from piece import Piece
from piece_factory import PieceFactory
from constants import BLACK, WHITE
from chess.moves import ChessMove, ChessMoveSet
from chess.characters import WHITE_PIECES, BLACK_PIECES

class ChessFactory(PieceFactory):
    "Concrete piece factory for setting up a checkers game"

    def create_piece(self, board, space):
        x = space.row
        y = space.col
        if x < 2:
            if x == 1:
                return Pawn(BLACK, board, space, "pawn")
            elif y == 3:
                return Queen(BLACK, board, space, "queen")
            elif y == 4:
                return King(BLACK, board, space, "king")
            elif y == 2 or y == 5:
                return Bishop(BLACK, board, space, "bishop")
            elif y == 1 or y == 6:
                return Knight(BLACK, board, space, "knight")
            elif y == 0 or y == 7:
                return Rook(BLACK, board, space, "rook")
        elif x > 5:
            if x == 6:
                return Pawn(WHITE, board, space, "pawn")
            elif y == 3:
                return Queen(WHITE, board, space, "queen")
            elif y == 4:
                return King(WHITE, board, space, "king")
            elif y == 2 or y == 5:
                return Bishop(WHITE, board, space, "bishop")
            elif y == 1 or y == 6:
                return Knight(WHITE, board, space, "knight")
            elif y == 0 or y == 7:
                return Rook(WHITE, board, space, "rook")
        
        return None

class ChessPiece(Piece):
    "Abstract piece class for a chess piece"
    # def __init__(self, side, board, space, pType):
    #     super().__init__(side, board, space, pType)

    def _findMoves(self, directions, piece):
        # moves = ChessMoveSet()
        moves = []

        if len(moves) == 0:
            # print(f"side: {self.side}")
            for direction in directions:
                curr_row = self._current_space.row
                one_step = self._board.get_dir(self._current_space, direction)
                knight = False
                steps = []
                i = 0
                if isinstance(one_step, list):
                    knight = True
                    steps = one_step
                    one_step = steps[0]
                    i += 1
                elif isinstance(self, Pawn) and len(direction) > 1:
                    if one_step and not one_step.has_opponent(self.side):
                        continue
                first = True
                while one_step and (knight or one_step.is_free() or one_step.has_opponent(self.side)):
                    # GONNA CAUSE PROBLEMS???????????
                    # ADD PROMOTION OPTION LATER
                    # print("yo")

                    if one_step.has_opponent(self.side) and (first or knight):
                        if isinstance(self, Pawn) and len(direction) < 2:
                            break
                        # print("hello")
                        m = ChessMove(self._current_space, one_step, captures=[one_step])
                        moves.append(m)
                        first = False
                        # if not knight:
                        #     if isinstance(piece, Pawn) and ((one_step.row == 0 and self.side == WHITE) or (one_step.row == 7 and self.side == BLACK)):
                        #         moves[0].add_promotion()

                        #     break
                    # elif not one_step.is_free():
                    #     if one_step.piece.side != self.side:
                    #         return moves
                    elif one_step.is_free():
                        # print("hello2")
                        m = ChessMove(self._current_space, one_step)
                        moves.append(m)
                    # if (self._side == WHITE and one_step.row == 0) or \
                    #         (self._side == BLACK and one_step.row == self._board.size - 1):
                    #     m.add_promotion()
                    if isinstance(piece, Pawn) or isinstance(piece, King):
                        # print("hello3")
                        # print(one_step.row)
                        if isinstance(piece, Pawn):
                            # print("kool")
                            if (one_step.row == 0 and self.side == WHITE) or (one_step.row == 7 and self.side == BLACK):
                                # print("555")
                                moves[0].add_promotion()
                                return moves
                            elif (self.side == WHITE and curr_row == 6 and direction == 'n') or (self.side == BLACK and curr_row == 1 and direction == 's'):
                                # print("666")
                                one_step = self._board.get_dir(one_step, direction)
                                curr_row = -1
                            else:
                                # print("777")
                                break
                                # return moves
                        else:
                            # print("nope")
                            return moves
                    elif knight:
                        if i <= len(steps) - 1:
                            one_step = steps[i]
                            i += 1
                        else:
                            return moves
                    else:
                        # print("hello4")
                        one_step = self._board.get_dir(one_step, direction)

        return moves

class King(ChessPiece):
    "Concrete piece class for a king piece"

    def __init__(self, side, board, space, pType):
        super().__init__(side, board, space, pType)
        if self._side == WHITE:
            self._symbol = WHITE_PIECES['KING'] 
        if self._side == BLACK:
            self._symbol = BLACK_PIECES['KING'] 
        self._directions = ['n', 's', 'w', 'e', 'ne', 'nw', 'sw', 'se']

    def enumerate_moves(self):
        return self._findMoves(self._directions, self)

    def promote(self):
        "Overrides promote to return a KingChecker in the same space for the same side"
        # return KingChecker(self._side, self._board, self._current_space)
        pass

class Queen(ChessPiece):
    "Concrete piece class for a queen piece"

    def __init__(self, side, board, space, pType):
        super().__init__(side, board, space, pType)
        if self._side == WHITE:
            self._symbol = WHITE_PIECES['QUEEN'] 
        if self._side == BLACK:
            self._symbol = BLACK_PIECES['QUEEN'] 
        self._directions = ['n', 's', 'w', 'e', 'ne', 'nw', 'sw', 'se']
            # self._directions = ["se", "sw"]

    def enumerate_moves(self):
        return self._findMoves(self._directions, self)

    def promote(self):
        "Overrides promote to return a KingChecker in the same space for the same side"
        # return KingChecker(self._side, self._board, self._current_space)
        pass

class Rook(ChessPiece):
    "Concrete piece class for a rook piece"

    def __init__(self, side, board, space, pType):
        super().__init__(side, board, space, pType)
        if self._side == WHITE:
            self._symbol = WHITE_PIECES['ROOK'] 
        if self._side == BLACK:
            self._symbol = BLACK_PIECES['ROOK'] 
        self._directions = ['n', 's', 'w', 'e']
            # self._directions = ["se", "sw"]

    def enumerate_moves(self):
        return self._findMoves(self._directions, self)

    def promote(self):
        "Overrides promote to return a KingChecker in the same space for the same side"
        # return KingChecker(self._side, self._board, self._current_space)
        pass


class Bishop(ChessPiece):
    "Concrete piece class for a bishop piece"

    def __init__(self, side, board, space, pType):
        super().__init__(side, board, space, pType)
        if self._side == WHITE:
            self._symbol = WHITE_PIECES['BISHOP'] 
        if self._side == BLACK:
            self._symbol = BLACK_PIECES['BISHOP'] 
        self._directions = ["ne", "nw", "se", "sw"]
            # self._directions = ["se", "sw"]

    def enumerate_moves(self):
        return self._findMoves(self._directions, self)

    def promote(self):
        "Overrides promote to return a KingChecker in the same space for the same side"
        # return KingChecker(self._side, self._board, self._current_space)
        pass


class Knight(ChessPiece):
    "Concrete piece class for a knight piece"

    def __init__(self, side, board, space, pType):
        super().__init__(side, board, space, pType)
        if self._side == WHITE:
            self._symbol = WHITE_PIECES['KNIGHT'] 
        if self._side == BLACK:
            self._symbol = BLACK_PIECES['KNIGHT'] 
        self._directions = ["knight"]
            # self._directions = ["se", "sw"]

    def enumerate_moves(self):
        return self._findMoves(self._directions, self)

    def promote(self):
        "Overrides promote to return a KingChecker in the same space for the same side"
        # return KingChecker(self._side, self._board, self._current_space)
        pass


class Pawn(ChessPiece):
    "Concrete piece class for a pawn piece"

    def __init__(self, side, board, space, pType):
        super().__init__(side, board, space, pType)
        if self._side == WHITE:
            self._symbol = WHITE_PIECES['PAWN'] 
            self._directions = ['n', 'ne', 'nw']
        if self._side == BLACK:
            self._symbol = BLACK_PIECES['PAWN'] 
            self._directions = ['s', 'se', 'sw']
            # self._directions = ["se", "sw"]

    def enumerate_moves(self):
        options = self._findMoves(self._directions, self)
        # for move in options:

        # print(options)
        return options

    def promote(self):
        "Overrides promote to return a KingChecker in the same space for the same side"
        # return KingChecker(self._side, self._board, self._current_space)
        old = self._current_space
        old.piece = None
        return Queen(self._side, self._board, self._current_space, "queen")
        # self._current_space = Queen(self._side, self._board, self._current_space, self._type)

# def moveFunc(board, directions, side, size, piece, space):
#     moves = ChessMoveSet()

#     if len(moves) == 0:
#         for direction in directions:
#             one_step = board.get_dir(space, direction)
#             while one_step and one_step.is_free():
#                 # print("here")
#                 m = ChessMove(space, one_step)
#                 moves.append(m)
#                 if (side == WHITE and one_step.row == 0) or \
#                         (side == BLACK and one_step.row == size - 1):
#                     m.add_promotion()
#                 if isinstance(piece, Pawn):
#                     one_step = None
#                 else:
#                     one_step = board.get_dir(one_step, direction)

#     return moves
