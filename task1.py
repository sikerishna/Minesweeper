from functions_minesweeper import *

board = [
    'X', 'O', 'O', 'O', 'X',  # Row 0
    'O', 'X', 'O', 'X', 'O',  # Row 1
    'O', 'O', 'X', 'O', 'O',  # Row 2
    'O', 'X', 'O', 'O', 'O',  # Row 3
    'X', 'O', 'O', 'O', 'X']  # Row 4

# Test cases
display_board(board)
print(board)

print(count_adjacent_mines(board, 0, 0))
display_board(board)
print(play_turn(board, 0, 1))

play_game([[2, 3], [1, 4], [0, 0]])

