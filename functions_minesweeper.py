#Assignment 3 - Saikrishna Bangalore, sban176, 239189441

def initialise_board():
    """
    Initialises the minesweeper board as a 1D list

    This function creates a Minesweeper board represented as a list of 25 elements. Each element
    is the string 'O', indicating an unrevealed square.

    Arguments:
        No inputs

    Returns:
        list: a list representing the minesweeper board
    """
    return ['O' for i in range(25)] # returns a list of 25 'O's


def display_board(board):
    """
    Displays a 5x5 minesweeper board

    This function prints the current state of the board to the screen.  It is what the player sees.

    Arguments:
        board (list): A list of 25 strings representing the Minesweeper board.

    Returns:
        No Outputs

        Notes:
        - The board is displayed as a 5-row grid, each with 5 space-separated values.
        - Mines ('X') are displayed as 'O' to keep them hidden.
        - The function does not modify the original board list.
        - It is assumed the input list has exactly 25 elements, corresponding to a 5 × 5 grid
    """
    count = 0 # position in list
    for i in range(5):  # Loop for each row
        row = "" # initializes string for 5x5 grid
        for j in range(5): # loop for each column
            if board[count] == 'X':
                row = row + 'O' # replace X with O on the board the player sees
            else:
                row = row + board[count] # continues to display Os
            if j < 4:  # Add a space between elements but not after the last element
                row = row + " "
            count = count + 1
        print(row) # prints each row of the grid before moving onto the next


def insert_mines(board, positions):
    """
    Inserts mines ('X') into specified positions on a 5 × 5 Minesweeper board.

    Arguments:
        board (list): A list of 25 strings representing the Minesweeper board.
        positions (list of lists): A list of [row, column] pairs where each mine should be
        inserted. Rows and columns are indexed from 0 to 4.

    Returns:
        No Outputs

    Notes:
        - The board list is modified in place; the function does not return a new list.
        - It is assumed that all provided positions are valid (within the bounds of the 5 × 5 grid).
        - The function replaces the existing value at each specified index with 'X'.
        """
    for pos in positions:  # loops through each mine position
        row = pos[0]  # gets the row index
        column = pos[1]  # gets the column index
        index = row * 5 + column  # converts 2D position to 1D index
        board[index] = 'X' # replaces the O with an X (the actual board, not what the player sees)


def count_adjacent_mines(board, row, column):
    """
    Counts the number of mines ('X') adjacent to a given square on a 5 × 5 Minesweeper board.

    Arguments:
        board (list): A list of 25 strings representing the Minesweeper board.
        row (int): The row index (0–4) of the square being checked.
        column (int): The column index (0–4) of the square being checked.

    Returns:
        int: The number of adjacent squares (0–8) that contain mines ('X').

    Notes:
        - Adjacent squares include horizontal, vertical, and diagonal neighbors (up to 8
        surrounding cells).
        - The board is treated as a 5 × 5 grid stored in a list; the index is calculated
        using: index = row * 5 + col.
        """

    mine_count = 0 # initializes number of mines that are adjacent to given position

    surrounding = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)] # the
    # relative locations of the 8 adjacent positions

    for relative_row_pos, relative_col_pos in surrounding:
        neighbor_row = row + relative_row_pos # actual position of adjacent row(s)
        neighbor_col = column + relative_col_pos #actual position of adjacent column(s)

        if 0 <= neighbor_row < 5 and 0 <= neighbor_col < 5: # makes sure surrounding positions
            # are in bounds
            index = neighbor_row * 5 + neighbor_col # convert 2D position to 1D index

            if board[index] == 'X': # check if surrounding positions are mines
                mine_count += 1

    return mine_count


def play_turn(board, row, column):
    """
    Plays a turn in the Minesweeper game by selecting a square and updating the board accordingly.

    Arguments:
        board (list): A list of 25 strings representing the current state of the Minesweeper board.
        row (int): The row index (0–4) of the selected square.
        column (int): The column index (0–4) of the selected square.

    Returns:
        updated board (list): The board after the turn has been played, with the selected square
        updated.
        mine_hit (bool): True if a mine was selected, False otherwise.

    Notes:
        - The function returns a new state of the board (even though lists are mutable).
        - It is assumed the row and column inputs are within the valid range (0 to 4).
        - Selecting a square that has already been played is allowed and will simply do nothing
        and will ask for another input.
        """
    index = row * 5 + column  # converts 2D input to 1D array

    if board[index] == 'X':
        board[index] = '#'  # Replace mine with '#'
        return board, True  # Return updated board and hash indicating a mine was hit

    else:
        adjacent_mines = count_adjacent_mines(board, row, column) # counts number of mines

    # Update the position based on the number of adjacent mines
    if adjacent_mines > 0:
        board[index] = str(adjacent_mines)  # Convert the number to a string and replace O with
        # number of adjacent mines
    else:
        board[index] = ' '  # Replace with a space if no adjacent mines

    return board, False  # Return the updated board and flag indicating no mine was hit


def check_win(board):
    """
    Checks if the player has won the Minesweeper game.

    Arguments:
        board (list): A list representing the current state of the Minesweeper board.

    Returns:
        has won (bool): True if all non-mine positions have been revealed, False otherwise.

    Notes:
        - A win is achieved when every square that is *not* a mine ('X') has been revealed.
        - Unrevealed squares are marked with 'O' and should not be present unless they are mines.
        - The function assumes that mines are marked with 'X' and only unrevealed non-mine squares use 'O'.
        - The board list should represent a full 5 × 5 Minesweeper grid (25 items).
        """
    for position in board:
        if position == '#' or position == 'O': # if a mine is selected, or there are unselected
            # positions, the game has either been lost or not won yet
            return False

    return True  # if no '#' or 'O' exists, the player has won


def play_game(mine_positions):
    """
    Plays a complete game of Minesweeper with user input until the game is won or lost.

    Arguments:
        mine_positions (list of lists of int): A list where each inner list contains two integers
        representing the row and column indices of a mine to be placed on the board.

    Returns:
        No Outputs

    Notes:
        - The board is assumed to be of fixed dimensions (5x5)
        - The mine_positions list must contain valid indices within the board range.
        - The game ends when the player reveals all non-mine cells (win) or selects a mine (loss).
        - The board is printed to the console after each move, showing the current game state.
        - Final result ("You win!" or "You hit a mine! Game over.") is printed upon game conclusion.
        """

    board = initialise_board() # initialises board as all Os

    insert_mines(board, mine_positions) #put mines into the board

    print("Welcome to Minesweeper!") # Explain game to user
    print("The board is a 5x5 grid. Each position is a row and column, both starting from 0.")
    print("Enter your moves in the format 'X, X' where X is a number (e.g., '2, 3').")
    print("Here is your starting board (mines are hidden):")
    display_board(board) # shows starting board

    while True: # game loop
        user_move = input("Enter your move (row, column):") # get user input
        row, column = user_move.split(",")  # split the input into row and column

        row = int(row) # turns into integer
        column = int(column)

        board, mine_location = play_turn(board, row, column)

        print("Updated board:") # display the updated board
        display_board(board)

        if mine_location:  # if mine is hit
            print("Game Over! You hit a mine.")
            print("Final board:")
            display_board(board)
            break

        if check_win(board):  # if all safe positions cleared
                print("Congratulations, you win!")
                print("Final board:")
                display_board(board)  # Show the full board state
                break




