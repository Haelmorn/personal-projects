player = 0

def show_board():
    for i in range(0, len(field)):
        print(*field[i], sep=" ")

def move_player(player, used):
    while True:
        print(f"Please, enter the coordinates for player {player}: ")
        move = input("> ").upper()
        if move in movelist and move not in used:
            used.append(move)
            return move
            break
        elif move in used:
            print("This spot is taken. Please, enter another one.")
            continue
        elif move not in movelist:
            print("Sorry, wrong input. Please enter the coordinates in (X, Y) format, for ex. 'A1'")
            continue
       
def parse_move(coordinates):
    if coordinates[0] == "A" and coordinates[1] == "1":
        coords = (1, 0)
    elif coordinates[0] == "B" and coordinates[1] == "1":
        coords = (1, 2)
    elif coordinates[0] == "C" and coordinates[1] == "1":
        coords = (1, 4)
    elif coordinates[0] == "A" and coordinates[1] == "2":
        coords = (3, 0)
    elif coordinates[0] == "B" and coordinates[1] == "2":
        coords = (3, 2)
    elif coordinates[0] == "C" and coordinates[1] == "2":
        coords = (3, 4)
    elif coordinates[0] == "A" and coordinates[1] == "3":
        coords = (5, 0)
    elif coordinates[0] == "B" and coordinates[1] == "3":
        coords = (5, 2)
    elif coordinates[0] == "C" and coordinates[1] == "3":
        coords = (5, 4)
    return coords   

def mark(xy, arena):
    global field
    if player == 1:
        arena[xy[0]][xy[1]] = "X"
    elif player == 2:
        arena[xy[0]][xy[1]] = "O"

def wincond(arena):
    if arena[1][0] == arena[1][2] == arena[1][4] and arena [1][0] != " ":
        return True
    elif arena[3][0] == arena[3][2] == arena[3][4] and arena [3][0] != " ":
        return True
    elif arena[5][0] == arena[5][2] == arena[5][4] and arena [5][0] != " ":
        return True
    elif arena[1][0] == arena[3][0] == arena[5][0] and arena[1][0] != " ":
        return True
    elif arena[1][2] == arena[3][2] == arena[5][2] and arena[1][2] != " ":
        return True
    elif arena[1][4] == arena[3][4] == arena[5][4] and arena[1][4] != " ":
        return True            
    else:
        return False
def restart():
    global moves
    global field
    moves = []
    field = [["A", " ", "B", " ", "C"],
        [" ", "|", " ", "|", " ", "1"],
        ["-", "-", "-", "-", "-"],
        [" ", "|", " ", "|", " ", "2"], 
        ["-", "-", "-", "-", "-"],
        [" ", "|", " ", "|", " ", "3"]]
        
moves = []
field = [["A", " ", "B", " ", "C"],
        [" ", "|", " ", "|", " ", "1"],
        ["-", "-", "-", "-", "-"],
        [" ", "|", " ", "|", " ", "2"], 
        ["-", "-", "-", "-", "-"],
        [" ", "|", " ", "|", " ", "3"]]

movelist = ("A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3")


def game_loop():
    global player
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

if __name__ == "__main__":
    game_loop()