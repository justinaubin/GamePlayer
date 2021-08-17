# GamePlayer

This project provides implementations for both human and computer players of checkers and chess. All files not in the "chess" or "checkers" folders are general to all similar board games. Computer players come in "random" and "greedy" varieties, which determines the types of moves each makes.

To specify which game you wish to play along with the players run the following command:
`python main.py [chess/checkers] [human/random/greedy] [human/random/greedy] [on/off]`

The state of the game (meaning the board, turn number, and current configuration of pieces) is printed to stdout after each turn is played. If two computer players are chosen the entire game is automatically. That is, unless the fourth argument is set to "on". This argument toggles the game history setting, which allows users to undo/redo all move made in the game. Users must type in "next/undo/redo" after each turn to decide how to proceed. 

A game always ends in one player winning, unless 50 turns are made with no piece being taken or there are no legal moves available, at which case there is a draw. In chess, players must capture the kind to win, rather than simply reaching checkmate.
