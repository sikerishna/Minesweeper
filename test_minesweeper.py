import pytest
from functions_minesweeper import *

def test_insert_mines_valid_positions():
    # Test if mines are placed at specified positions correctly
    board = initialise_board()
    insert_mines(board, [(0, 0), (2, 2), (4, 4)])
    expected_board = ['X', 'O', 'O', 'O', 'O',
                      'O', 'O', 'O', 'O', 'O',
                      'O', 'O', 'X', 'O', 'O',
                      'O', 'O', 'O', 'O', 'O',
                      'O', 'O', 'O', 'O', 'X']
    assert board == expected_board


def test_count_adjacent_mines_adjacent_mines():
    # Test counting adjacent mines when multiple mines are around
    board = initialise_board()
    insert_mines(board, [(0, 1), (1, 0), (1, 1)])  # Insert mines around (0, 0)
    result = count_adjacent_mines(board, 0, 0)
    assert result == 3  # There should be 3 adjacent mines


def test_count_adjacent_mines_no_adjacent_mines():
    # Test counting adjacent mines when there are no adjacent mines
    board = initialise_board()
    insert_mines(board, [(4, 4), (3, 3)])  # Insert mines far from (0, 0)
    result = count_adjacent_mines(board, 0, 0)
    assert result == 0  # There should be 0 adjacent mines


def test_play_turn_hit_mine():
    # Test if playing a turn and hitting a mine updates correctly
    board = initialise_board()
    insert_mines(board, [(2, 2)])  # Insert a mine at (2, 2)
    updated_board, mine_hit = play_turn(board, 2, 2)
    assert mine_hit is True  # Ensure that hitting the mine is detected
    assert updated_board[12] == '#'  # Check that the mine was replaced with '#'


def test_play_turn_reveal_safe_square():
    # Test revealing a safe square during a turn
    board = initialise_board()
    insert_mines(board, [(0, 0)])  # Insert a mine at (0, 0)
    updated_board, mine_hit = play_turn(board, 1, 1)  # Safe square
    assert mine_hit is False  # Should not hit a mine
    assert updated_board[6] == '1'  # Revealed square should show '1', as (0, 0) is nearby


def test_check_win_win_condition():
    #Test if the check_win function detects a win condition
    board = ['1', '1', '1', '1', 'X',
             '1', 'X', '1', '1', ' ',
             '1', '1', '1', ' ', ' ',
             '1', '1', ' ', '8', ' ',
             'X', '1', ' ', ' ', ' ']
    result = check_win(board)
    assert result is True  # Player has revealed every non-mine square


def test_check_win_not_yet_won():
    # Test if check_win detects that the game is not yet won
    board = initialise_board()  # All squares still unrevealed
    result = check_win(board)
    assert result is False
