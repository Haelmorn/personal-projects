import random
import time

moves = []
coord_dict = {
    "A1": 0,
    "B1": 1,
    "C1": 2,
    "A2": 3,
    "B2": 4,
    "C2": 5,
    "A3": 6,
    "B3": 7,
    "C3": 8,
}
reparse_dict = {
    0: "A1",
    1: "B1",
    2: "C1",
    3: "A2",
    4: "B2",
    5: "C2",
    6: "A3",
    7: "B3",
    8: "C3",
}
field = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
movelist = ("A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3")


def show_board():
    print("A", " ", "B", " ", "C",)
    print(field[0], "|", field[1], "|", field[2], "1")
    print("-", "-", "-", "-", "-")
    print(field[3], "|", field[4], "|", field[5], "2") 
    print("-", "-", "-", "-", "-")
    print(field[6], "|", field[7], "|", field[8], "3")


def move_player(player, used):
#Takes input from the player, checks if 1) input is quit 2)the move is allowed and the spot is free 3)the spot is taken 4)move is allowed (ie. is a proper place on the board)
    while True:
        print(f"Please, enter the coordinates for player {player}: ")
        move = input("> ").upper()
        if move == "QUIT":
            quit()
        elif move in movelist and move not in used:
            used.append(move)
            return move
        elif move in used:
            print("This spot is taken. Please, enter another one.")
            continue
        elif move not in movelist:
            print("""Sorry, wrong input. Please enter the coordinates in (X, Y)
            format, for ex. 'A1'""")
            continue

# Pseudo-ai code, returns a move (same as player_move()), but first checks if
# any move can win it the game. 
# Then, chooses the middle spot if its free.
# If not, returns a random free spot
# TODO: Add a check for possible player win in their next turn (after checking
#       for win possibility)
# TODO: Make this function better organised and readable
# TODO: Take a random corner if middle is taken


def aimove():
    open = []
    for m in movelist:
        if m not in moves:
            open.append(m)
    if next_turn_win(open, field) is not False:
        choice = next_turn_win(open, field)
    elif "B2" in open:
        choice = "B2"
    else:
        choice = random.choice(open)
    moves.append(choice)
    return choice


def next_turn_win(moveset, arena):
    for m in range(0, 9):
        tempfield = arena.copy()
        if tempfield[m] == " ":
            mark(m, tempfield, 2)
            if wincond(tempfield) is True:
                a = reparse(m)
                return a
    return False


def reparse(move):
    if move in reparse_dict.keys():
        return reparse_dict[move]


def parse_move(coordinates):
#Takes coordinates argument (coming from player_move() or aimove() function)
# and parses it to form a target for mark() function
    if coordinates in coord_dict:
        return coord_dict[coordinates]

#Marks x spot on arena playing field with either X or O, depending on current player
def mark(x, arena, player):
    if player == 1:
        arena[x] = "X"
    elif player == 2:
        arena[x] = "O"

##Checks the field for possible winning combinations
# TODO: Again, shorten this
def wincond(arena):
    if arena[0] == arena[1] == arena[2] and arena [0] != " ":
        return True
    elif arena[3] == arena[4] == arena[5] and arena [3] != " ":
        return True
    elif arena[6] == arena[7] == arena[8] and arena [6] != " ":
        return True
    elif arena[0] == arena[3] == arena[6] and arena[0] != " ":
        return True
    elif arena[1] == arena[4] == arena[7] and arena[1] != " ":
        return True
    elif arena[2] == arena[5] == arena[8] and arena[2] != " ":
        return True
    elif arena[0] == arena[4] == arena[8] and arena[0] != " ":
        return True
    elif arena[2] == arena[4] == arena[7] and arena[2] != " ":
        return True
    else:
        return False

##Clears the field and used moves to get a fresh game
def restart():
    global moves
    global field
    moves = []
    field = [" ", " ", " "," ", " ", " "," ", " ", " "]

##Allows player to choose a gamemode (1 for pvp and 2 for pve)
def gamemode():
    while True:
        print("Choose game mode")
        print("1. Player vs Player")
        print("2. Player vs computer")
        mode = int(input("> "))
        if mode == 1:
            return mode   
        elif mode == 2:
            return mode
        elif mode != 1 and mode != 2:
            print("Please, choose a proper game mode (1 or 2)")
            continue


#TODO: Take common parts from both modes and somehow concantenate this function to make it shorter
def game_loop():
    global player
    gmod = gamemode()
    if gmod == 1:
        while True:
            if player == 2 or player == 0:
                player = 1
            elif player == 1:
                player = 2
            show_board()
            move = move_player(player, moves)
            coords = parse_move(move)
            mark(coords, field, player)
            if wincond(field):
                show_board()
                print(f"Congratulations! Player {player} wins!")
                print("Play again? (y/n)")
                if input("> ") == "y":
                    restart()
                else:
                    break
            elif len(moves)==9:
                show_board()
                print("It's a draw!")
                print("Play again? (y/n)")
                if input("> ") == "y":
                    restart()
                else:
                    break
    elif gmod == 2:
        show_board()
        player = 1
        while True:
            if player == 2:
                print("Computer's turn")
                time.sleep(1)
                coords = parse_move(aimove())
            elif player == 1 or player == 0:
                coords = parse_move(move_player(player, moves))
            mark(coords, field, player)
            show_board()
            if wincond(field):
                show_board()
                if player == 1:
                    print(f"Congratulations! You win!")
                elif player == 2:
                    print("The computer wins!")
                print("Play again? (y/n)")
                if input("> ") == "y":
                    restart()
                else:
                    break
            elif len(moves)==9:
                show_board()
                print("It's a draw!")
                print("Play again? (y/n)")
                if input("> ") == "y":
                    restart()
                else:
                    break
            if player == 1:
                player = 2
            elif player == 2:
                player = 1
                    
            
            
if __name__ == "__main__":
    game_loop()
