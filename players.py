import random
import math
import copy
piece_points = {"peasant": 1, "checker_king": 2, "pawn": 1, "knight": 3, "bishop": 3, "rook": 5, "queen": 9, "king": 100}

class Player:
    "Abstract player class"

    def __init__(self, side=None) -> None:
        self.side = side

    def take_turn(self):
        raise NotImplementedError()

    @staticmethod
    def create_player(player_type):
        "Factory method for creating players"
        if player_type == "human":
            return HumanPlayer()
        elif player_type == "random":
            return RandomCompPlayer()
        elif player_type == "greedy":
            return GreedyCompPlayer()
        elif "minimax" in player_type:
            max_depth = int(player_type[len(player_type)-1])
            return MinimaxPlayer(max_depth)
        else:
            return None


class HumanPlayer(Player):
    "Concrete player class that prompts for moves via the command line"

    def take_turn(self, game_state):
        b = game_state.board
        while True:
            chosen_piece = input("Select a piece to move\n")
            chosen_piece = b.get_space(chosen_piece).piece
            if chosen_piece is None:
                print("no piece at that location")
                continue
            if chosen_piece.side != self.side:
                print("that is not your piece")
                continue
            options = chosen_piece.enumerate_moves()
            if len(options) == 0 or options[0] not in game_state.all_possible_moves():

                print("that piece cannot move")
                continue

            self._prompt_for_move(options).execute(game_state)
            return

    def _prompt_for_move(self, options):
        while True:
            for idx, op in enumerate(options):
                print(f"{idx}: {op}")
            chosen_move = input(
                "Select a move by entering the corresponding index\n")
            try:
                chosen_move = options[int(chosen_move)]
                return chosen_move
            except ValueError:
                print("not a valid option")


class RandomCompPlayer(Player):
    "Concrete player class that picks random moves"

    def take_turn(self, game_state):
        options = game_state.all_possible_moves()
        m = random.choice(options)
        print(m)
        m.execute(game_state)


class GreedyCompPlayer(Player):
    "Concrete player class that chooses moves that capture the most pieces while breaking ties randomly"

    def take_turn(self, game_state):
        options = game_state.all_possible_moves()
        max_captures = 0
        potential_moves = []
        for m in options:
            if m.num_captures() > max_captures:
                potential_moves = [m]
                max_captures = m.num_captures()
            elif m.num_captures() == max_captures:
                potential_moves.append(m)

        selected_move = random.choice(potential_moves)
        print(selected_move)
        selected_move.execute(game_state)


class MinimaxPlayer(Player):
    
    def __init__(self, max_depth):
        self._max_depth = max_depth

    def take_turn(self, game_state):
        options = game_state.all_possible_moves()
        state_copy = copy.deepcopy(game_state)
        points, index = self._minimax(0, state_copy, True, None)
        # print(points, m)
        m = options[index]
        m.execute(game_state)

    def _minimax(self, current_depth, state, is_max_turn, best_move):

        best_value = float('-inf') if is_max_turn else float('inf')
        # action_target = ""
        best_move_index = 0

        if current_depth >= self._max_depth:
            player_pieces = state.board.pieces_iterator(state.current_side)
            opponent_pieces = state.board.pieces_iterator(not state.current_side)
            player_count = 0
            opponent_count = 0
            for piece in player_pieces:
                player_count += piece_points[piece.type]

            for piece in opponent_pieces:
                opponent_count += piece_points[piece.type]
            return player_count - opponent_count, best_move_index
            # return AIElements.evaluation_function(state, self.player_color), ""

        possible_moves = state.all_possible_moves()
        # key_of_actions = list(possible_action.keys())

        # print(possible_moves)
        for i, move in enumerate(possible_moves):
            # print(move)
            move = copy.deepcopy(move)
            state_copy = copy.deepcopy(state)
            move.execute(state_copy)
            state_copy.next_turn()
            # new_state = AIElements.result_function(state,possible_action[action_key])

            turn_points, best_m = self._minimax(current_depth+1, state_copy, not is_max_turn, best_move)

            # print(move)
            if is_max_turn and best_value < turn_points:
                # print("bruh")
                best_value = turn_points
                best_move_index = i
                # action_target = action_key

            elif (not is_max_turn) and best_value > turn_points:
                best_value = turn_points
                best_move_index = i 
                # action_target = action_key

        # print(f"made it: {best_move}")
        return best_value, best_move_index




















# import random
# import math
# import copy
# piece_points = {"peasant": 1, "checker_king": 2, "pawn": 1, "knight": 3, "bishop": 3, "rook": 5, "queen": 9, "king": 100}


# class Player:
#     "Abstract player class"

#     def __init__(self, side=None):
#         self.side = side

#     def take_turn(self):
#         raise NotImplementedError()

#     @staticmethod
#     def create_player(player_type):
#         "Factory method for creating players"
#         if player_type == "human":
#             return HumanPlayer()
#         elif player_type == "random":
#             return RandomCompPlayer()
#         elif player_type == "greedy":
#             return GreedyCompPlayer()
#         elif player_type == "minimax":
#             return MinimaxPlayer()
#         else:
#             return None


# class HumanPlayer(Player):
#     "Concrete player class that prompts for moves via the command line"

#     def take_turn(self, game_state):
#         b = game_state.board
#         while True:
#             chosen_piece = input("Select a piece to move\n")
#             chosen_piece = b.get_space(chosen_piece).piece
#             if chosen_piece is None:
#                 print("no piece at that location")
#                 continue
#             if chosen_piece.side != self.side:
#                 print("that is not your piece")
#                 continue
#             options = chosen_piece.enumerate_moves()
#             if len(options) == 0 or options[0] not in game_state.all_possible_moves():

#                 print("that piece cannot move")
#                 continue

#             self._prompt_for_move(options).execute(game_state)
#             return

#     def _prompt_for_move(self, options):
#         while True:
#             for idx, op in enumerate(options):
#                 print(f"{idx}: {op}")
#             chosen_move = input("Select a move by entering the corresponding index\n")
#             try:
#                 chosen_move = options[int(chosen_move)]
#                 return chosen_move
#             except ValueError:
#                 print("not a valid option")


# class RandomCompPlayer(Player):
#     "Concrete player class that picks random moves"

#     def take_turn(self, game_state):
#         options = game_state.all_possible_moves()
#         m = random.choice(options)
#         print(m)
#         m.execute(game_state)


# class GreedyCompPlayer(Player):
#     "Concrete player class that chooses moves that capture the most pieces while breaking ties randomly"

#     def take_turn(self, game_state):
#         # piece_points = {"pawn": 1, "knight": 3, "bishop": 3, "rook": 5, "queen": 9, "king": 100}
#         options = game_state.all_possible_moves()
#         max_piece = 0
#         potential_moves = []
#         for m in options:
#             if m.captured:
#                 value = piece_points[m.captured.type]
#                 if value > max_piece:
#                     max_piece = value
#                     potential_moves = [m]
#                 elif value == max_piece:
#                     potential_moves.append(m)
#             elif max_piece == 0:
#                 potential_moves.append(m)

#         selected_move = random.choice(potential_moves)
#         print(selected_move)
#         selected_move.execute(game_state)

# class MinimaxPlayer(Player):

#     def __init__(self):
#         self.best_move = None

#     def take_turn(self, game_state):
#         options = game_state.all_possible_moves()
#         state_copy = copy.deepcopy(game_state)
#         points, index = self._minimax(0, 2, state_copy, True, None)
#         # print(points, m)
#         m = options[index]
#         m.execute(game_state)

#     # def minimax(self, curDepth, nodeIndex, maxTurn, options, targetDepth):

#     #     # base case : targetDepth reached
#     #     if (curDepth == targetDepth):
#     #         return options[nodeIndex]
#     #         # return piece_points[nodeIndex]
        
#     #     if (maxTurn):
#     #         return max(minimax(curDepth + 1, nodeIndex * 2,
#     #                     False, targetDepth),
#     #                 minimax(curDepth + 1, nodeIndex * 2 + 1,
#     #                     False, targetDepth))
        
#     #     else:
#     #         return min(minimax(curDepth + 1, nodeIndex * 2,
#     #                     True, targetDepth),
#     #                 minimax(curDepth + 1, nodeIndex * 2 + 1,
#     #                     True, targetDepth))


#     # def choose_action(self, game_state):
#     #     options = game_state.all_possible_moves()
#     #     m = self.minimax(0, 0, True, options, 2)
#     #     m.execute(game_state)

#         # list_action = AIElements.get_possible_action(state)
#         # eval_score, selected_key_action = self._minimax(0,state,True)
#         # return (selected_key_action,list_action[selected_key_action])

#     def _minimax(self, current_depth, max_depth, state, is_max_turn, best_move):

#         if current_depth >= max_depth:
#             player_pieces = state.board.pieces_iterator(state.current_side)
#             opponent_pieces = state.board.pieces_iterator(not state.current_side)
#             player_count = 0
#             opponent_count = 0
#             for piece in player_pieces:
#                 player_count += piece_points[piece.type]

#             for piece in opponent_pieces:
#                 opponent_count += piece_points[piece.type]
#             return player_count - opponent_count, self.best_move
#             # return AIElements.evaluation_function(state, self.player_color), ""

#         possible_moves = state.all_possible_moves()
#         # key_of_actions = list(possible_action.keys())

#         best_value = float('-inf') if is_max_turn else float('inf')
#         # action_target = ""
#         best_move_index = 0
#         # print(possible_moves)
#         for i, move in enumerate(possible_moves):
#             # print(move)
#             move = copy.deepcopy(move)
#             state_copy = copy.deepcopy(state)
#             move.execute(state_copy)
#             state_copy.next_turn()
#             # new_state = AIElements.result_function(state,possible_action[action_key])

#             turn_points, best_m = self._minimax(current_depth+1, max_depth, state_copy, not is_max_turn, best_move)

#             # print(move)
#             if is_max_turn and best_value < turn_points:
#                 # print("bruh")
#                 best_value = turn_points
#                 best_move_index = i
#                 # action_target = action_key

#             elif (not is_max_turn) and best_value > turn_points:
#                 best_value = turn_points
#                 best_move_index = i 
#                 # action_target = action_key

#         # print(f"made it: {best_move}")
#         return best_value, best_move_index
        
#     # Driver code

#     # treeDepth = math.log(len(piece_points), 2)

#     # print("The optimal value is : ", end = "")
#     # print(minimax(0, 0, True, treeDepth))

#     # This code is contributed
#     # by rootshadow

