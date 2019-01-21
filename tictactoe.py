from random import randint
player = 0

def show_board():
    print("A", " ", "B", " ", "C",)
    print(field[0], "|", field[1], "|", field[2], "1")
    print("-", "-", "-", "-", "-")
    print(field[3], "|", field[4], "|", field[5], "2") 
    print("-", "-", "-", "-", "-")
    print(field[6], "|", field[7], "|", field[8], "3")

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

def mark(xy, arena):
    global field
    if player == 1:
        arena[xy] = "X"
    elif player == 2:
        arena[xy] = "O"

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

def restart():
    global moves
    global field
    moves = []
    field = [" ", " ", " "," ", " ", " "," ", " ", " "]

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

def aimove():
    tempfield = field
    try:
        for i in range(0, len(tempfield)):
            mark(i, tempfield)
            if wincond(tempfield) == True:
                return i
            else:
                tempfield = field
    except ValueError:
        pass
    else:
        while True:
            move = randint(0, 8)
            if field[move] == " ":
                return i
            elif field[move] != " ":
                pass




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
        player = 1
        while True:
            show_board()
            if player == 2:
                player = 1
                coords = aimove()
            elif player == 1:
                coords = parse_move(move_player(player, moves))
                player = 2
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

aimove()


if __name__ == "__main__":
    game_loop()