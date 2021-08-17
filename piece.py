
class Piece:
    "Abstract piece class"

    def __init__(self, side, board, space, pType):
        self._current_space = space
        self._board = board
        # read only properties
        self._side = side
        self._type = pType

    @property
    def side(self):
        return self._side

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, pType):
        self._type = pType

    def __str__(self):
        return self._symbol

    def move(self, space):
        self._current_space = space

    def promote(self):
        "Promote returns the current piece by default (doing nothing), but may be overridden for specific piece rules"
        return self

    def enumerate_moves(self):
        """Abstract method
        Concrete implementations should return a list of valid Move objects
        """
        raise NotImplementedError()

    def is_valid_move(self, new_space):
        return new_space in self.enumerate_moves()

    # def noObstacle(self, dir):
    #     if dir()
