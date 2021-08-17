from move import Move

class ChessMove(Move):
    def __init__(self, start, end, captures=None):
        super().__init__(start, end, captures)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"move: {self._start}->{self._end}"

    def pieceTaken(self):
        return len(self._captures) > 0





class ChessMoveSet(list):
    """
    An extension to a list meant to hold chess moves. When using append this ensures that the list does not mix jumps and non-jumps.
    """

    def __init__(self):
        self.captured = False

    # def append(self, move):
    #     # if move.pieceTaken():
    #     #     if not self.has_jump:
    #     #         #this is the first jump so clear out any basic moves that might be here already
    #     #         self.has_jump = True
    #     #         self.clear()
    #     #     super().append(move)
           
    #     # elif not self.has_jump:
    #     #     # only add basic moves if there are no jumps so far

    #     # HAVE TO MAKE "JUMP" MOVES?????????????????????????????????????
    #     # ???????????????????
    #     # !!!!!!!!!!!!!!!!!
    #     # ????????????????
    #     # 
    #     super().append(move)

    # def extend(self, other):
    #     """
    #     Overrides extend to use this version of append
    #     """
    #     if other:
    #         for m in other:
    #             self.append(m)

