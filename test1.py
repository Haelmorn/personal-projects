import random as rand

height = 5
width = 7


def random_filled(height, width):
    """
    Create a random board with given dimensions.
    A board is represented as a list of columns.
    """
    board = [[]] * width

    # Choose a random number of moves
    # - at least 8
    # - no more than 80% of the board is full
    plays = 8#rand.randint(8, int(0.8*height*width))

    player = 'X'
    for i in range(plays):
        while True:
            col_choice = rand.randrange(0, width)
            col = board[col_choice]
            if len(board[col_choice]) < height:
                col = col + [player]
                break
        if player == 'X':
            player = 'O'
        else:
            player = 'X'

        for c in board:
            while len(c) < height:
                c = c + ['.']
    return board


def swap_players(player):
    """
    Change player from X to O and vice versa
    """


    if player == 'X':
        player = 'O'
    else:
        player = 'X'


def display_board(board):
    """
    Display the board to the console.
    The "front" of each column is "down".
    """
    print(height, width)
    for i in range(-1, -height-1, -1):
        for j in range(0, width):
            print(board[i], end='')
            print(board[j], end='')
        print()


# generate a bunch
examples = 8

print(examples)
for i in range(examples):
    height = rand.randint(5,7)
    width = rand.randint(6,9)
    bd = random_filled(height, width)
    display_board(bd)
    print()