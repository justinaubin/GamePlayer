from game_state import GameState
from chess.moves import ChessMoveSet
from constants import BLACK, WHITE

class ChessGameState(GameState):

    def all_possible_moves(self, side=None):
        if not side:
            side = self._current_side
        pieces = self._board.pieces_iterator(side)
        # uses CheckersMoveSet to enforce restriction on basic moves when at least once piece has a jump
        options = ChessMoveSet()
        for piece in pieces:
            # if piece.side 
            options.extend(piece.enumerate_moves())

        return options



    def check_loss(self, side=None):
        if not side:
            side = self._current_side
        # no more pieces
        for piece in list(self._board.pieces_iterator(side)):
            if piece.type == "king":
                return False
        
        return True
