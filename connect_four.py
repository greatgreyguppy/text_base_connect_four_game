"""
    Game of Connect 4
    The game board of spaces with 6 rows and 7 columns
    The piece falls to the lowest available row in the column
    The game ends when a player gets 4 in a row
"""

def create_grid():
    """ Create a game board of spaces
    with 6 rows and 7columns"""
    grid = []
    for row in range(6):
        grid.append([])
        for column in range(7):
            grid[row].append(' ')
    return grid

def print_grid(grid):
    """ 
    Print the grid.
    :param grid: The game board
    """
    print('\n--- Game of Connect 4 ---\n')
    print('    +-+-+-+-+-+-+-+')
    for row in range(6):
        print('    |', end='')
        for column in range(7):
            print(grid[row][column] + '|', end='')
        print()
        print('    +-+-+-+-+-+-+-+')
    print('     1 2 3 4 5 6 7')

def get_user_input(player):
    """ 
    Get the user's input. 
    :param player: The player number
    :return: The column number
    """
    while True:
        user_input = input(f'Player {player} Enter a column number: ')
        if user_input in '1234567':
            return int(user_input)
        else:
            print('Invalid input. Please select a Column 1-7.')

def drop_piece(grid, column, piece):
    """ 
    Drop a piece into the game board. 
    :param grid: The game board
    :param column: The column number
    :param player: The player number
    :return: True if piece was dropped, False if column is full
    """
    # array is zero based, so subtract 1 from column
    column -= 1
    for row in range(5, -1, -1):
        if grid[row][column] == ' ':
            grid[row][column] = piece
            return True
    return False


def check_for_winner(grid, piece):
    """ Check if there are 4 in a row. """
    # check for horizontal win
    for row in range(6):
        for column in range(4):
            if (grid[row][column] == piece
                and grid[row][column + 1] == piece
                and grid[row][column + 2] == piece
                and grid[row][column + 3] == piece):
                return 'horizontal'

    # check for vertical win
    for row in range(3):
        for column in range(7):
            if (grid[row][column] == piece
                and grid[row + 1][column] == piece
                and grid[row + 2][column] == piece
                and grid[row + 3][column] == piece):
                return 'vertical'

    # check for diagonal win
    for row in range(3):
        for column in range(4):
            if (grid[row][column] == piece
                and grid[row + 1][column + 1] == piece
                and grid[row + 2][column + 2] == piece
                and grid[row + 3][column + 3] == piece):
                return 'diagonal'

    # check for diagonal win
    for row in range(3):
        for column in range(4):
            if (grid[row][column + 3] == piece
                and grid[row + 1][column + 2] == piece
                and grid[row + 2][column + 1] == piece
                and grid[row + 3][column] == piece):
                return 'diagonal'

    return None

game_grid = create_grid()
turn_player = 1
player_piece = [' ','@','O']

while True:
    print_grid(game_grid)
    if turn_player > 2:
        turn_player = 1
    turn = get_user_input(turn_player)
    success = drop_piece(game_grid, turn, player_piece[turn_player])
    if not success:
        print('Column is full. Please select another column.')
        continue

    winner = check_for_winner(game_grid, player_piece[turn_player])
    if winner is not None:
        print_grid(game_grid)
        print(f'Player {turn_player} has a {winner} win!')
        break

    turn_player += 1
