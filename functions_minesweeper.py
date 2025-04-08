def initialise_board():
    return ['O' for i in range(25)]


def display_board(board):
    count = 0
    for i in range(5):  # Loop for each row
        row = ""
        for j in range(5):
            if board[count] == 'X':
                row = row + 'O'
            else:
                row = row + board[count]
            if j < 4:  # Add a space between elements but not after the last element
                row = row + " "
            count = count + 1
        print(row)


def insert_mines(board, positions):
    for pos in positions:  # Loop through each mine position
        row = pos[0]  # Extract the row index
        column = pos[1]  # Extract the column index
        index = row * 5 + column  # Convert 2D position to 1D index
        board[index] = 'X'


def count_adjacent_mines(board, row, column):
    # Keep track of the number of adjacent mines
    mine_count = 0

    surrounding = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for relative_row_pos, relative_col_pos in surrounding:
        # Calculate the neighbor's row and column
        neighbor_row = row + relative_row_pos
        neighbor_col = column + relative_col_pos

        # Check if neighbor is within bounds (0 <= row < 5 and 0 <= column < 5)
        if 0 <= neighbor_row < 5 and 0 <= neighbor_col < 5:
            # Convert 2D position to 1D index
            index = neighbor_row * 5 + neighbor_col

            # Check if the neighbor contains a mine ('X')
            if board[index] == 'X':
                mine_count += 1

    return mine_count


def play_turn(board, row, column):
    index = row * 5 + column  # Convert 2D input to 1D array

    if board[index] == 'X':
        board[index] = '#'  # Replace mine with '#'
        return board, True  # Return updated board and flag indicating a mine was hit

    else:
        adjacent_mines = count_adjacent_mines(board, row, column)

    # Update the position based on the number of adjacent mines
    if adjacent_mines > 0:
        board[index] = str(adjacent_mines)  # Convert the number to a string
    else:
        board[index] = ' '  # Replace with a space if no adjacent mines

    return board, False  # Return the updated board and flag indicating no mine was hit


def check_win(board):
    for position in board:
        if position == '#' or position == 'O':
            return False  # if a mine is selected, or there are unselected positions, the game has either been lost or not won yet

    return True  # if no '#' or 'O' exists, the player has won


def play_game(mine_positions):

    # Step 1: Initialize the board
    board = initialise_board()

    # Step 2: Insert mines into the board
    insert_mines(board, mine_positions)

    # Step 3: Explain the game to the user
    print("Welcome to Minesweeper!")
    print("The board is a 5x5 grid. Each position is a row and column, both starting from 0.")
    print("Enter your moves in the format 'X, X' where X is a number (e.g., '2, 3').")
    print("Here is your starting board (mines are hidden):")
    display_board(board)

    # Step 4: Game loop
    while True:
        # Get user input and split into row and column
        user_move = input("Enter your move (row, column):")

        row, column = user_move.split(",")  # Split the input into row and column

        row = int(row)
        column = int(column)

        board, mine_location = play_turn(board, row, column)

        # Display the updated board
        print("Updated board:")
        display_board(board)

        # Step 6: Check if the game is over (win or loss)
        if mine_location:  # Mine was hit
            print("Game Over! You hit a mine.")
            print("Final board:")
            display_board(board)  # Optionally reveal the whole board
            break

        if check_win(board):  # All safe positions cleared
                print("Congratulations, you win!")
                print("Final board:")
                display_board(board)  # Show the full board state
                break




