import random
import time
player = 0

##Pretty self-explanatory. Prints out the playing field to the terminal
def show_board():
    print("A", " ", "B", " ", "C",)
    print(field[0], "|", field[1], "|", field[2], "1")
    print("-", "-", "-", "-", "-")
    print(field[3], "|", field[4], "|", field[5], "2") 
    print("-", "-", "-", "-", "-")
    print(field[6], "|", field[7], "|", field[8], "3")

##Takes input from the player, checks if 1) input is quit 2)the move is allowed and the spot is free 3)the spot is taken 4)move is allowed (ie. is a proper place on the board)
def move_player(player, used):
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
            print("Sorry, wrong input. Please enter the coordinates in (X, Y) format, for ex. 'A1'")
            continue

#Takes coordinates argument (coming from player_move() or aimove() function)
# and parses it to form a target for mark() function
def parse_move(coordinates):
    if coordinates[0] == "A" and coordinates[1] == "1":
        coords = 0
    elif coordinates[0] == "B" and coordinates[1] == "1":
        coords = 1
    elif coordinates[0] == "C" and coordinates[1] == "1":
        coords = 2
    elif coordinates[0] == "A" and coordinates[1] == "2":
        coords = 3
    elif coordinates[0] == "B" and coordinates[1] == "2":
        coords = 4
    elif coordinates[0] == "C" and coordinates[1] == "2":
        coords = 5
    elif coordinates[0] == "A" and coordinates[1] == "3":
        coords = 6
    elif coordinates[0] == "B" and coordinates[1] == "3":
        coords = 7
    elif coordinates[0] == "C" and coordinates[1] == "3":
        coords = 8
    return coords   

##Marks x spot on arena playing field with either X or O, depending on current player
def mark(x, arena):
    if player == 1:
        arena[x] = "X"
    elif player == 2:
        arena[x] = "O"

##Checks the field for possible winning combinations
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
##Pseudo-ai code, returns a move (same as player_move()), but first checks if any move can win it the game. If not, returns a random free spot
def aimove():
    open = []
    for m in movelist:
        if m not in moves:
            open.append(m)
    choice = random.choice(open)
    moves.append(choice)
    return choice





moves = []
field = [" ", " ", " "," ", " ", " "," ", " ", " "]
movelist = ("A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3")


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
            mark(coords, field)
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
            mark(coords, field)
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
