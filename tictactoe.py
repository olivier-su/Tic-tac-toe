#Creating the board

board = [" " for i in range(9)]

def print_board():
    row1 = "|{}|{}|{}|".format(board[0],board[1],board[2])
    row2 = "|{}|{}|{}|".format(board[3],board[4],board[5])
    row3 = "|{}|{}|{}|".format(board[6],board[7],board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

#How the players move on the board
def player_move(icon):

    if icon =="X":
        number = 1
    elif icon == "O":
        number = 2
        
    print("It's player {}'s turn".format(icon))
    
    choice = int(input("Enter your move(1-9): ").strip())
    if board[choice-1] ==" ":
        board[choice-1] = icon
    else:
        print()
        print("You can't place it on that space")
        print_board()
        player_move(icon)

# Victory condition

def is_victory(icon):
    if(board[0] == icon and board[1] == icon and board[2] == icon) or \
      (board[3] == icon and board[4] == icon and board[5] == icon) or \
      (board[6] == icon and board[7] == icon and board[8] == icon) or \
      (board[0] == icon and board[3] == icon and board[6] == icon) or \
      (board[1] == icon and board[4] == icon and board[7] == icon) or \
      (board[2] == icon and board[5] == icon and board[8] == icon) or \
      (board[0] == icon and board[4] == icon and board[8] == icon) or \
      (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

# Draw condition

def is_draw():
    if " " not in board:
        return True
    else:
        return False

#The game
    
while True:

    print_board()
    player_move("X")
    print_board()
    if is_victory("X"):
        print("Player X wins!")
        new_game = input("Do you want to start a new game? Type y to restart").strip().lower()
        if new_game == "y":
            board = [" " for i in range(9)]
            print_board()
            print("The losing player starts")
        else:
            break
    elif is_draw():
        print("It's a draw")
        new_game = input("Do you want to start a new game? Type (y/n)").strip().lower()
        if new_game == "y":
            board = [" " for i in range(9)]
            print_board()
            print("Player O starts")
        else:
            break
    player_move("O")
    if is_victory("O"):
        print_board()
        print("Player O wins!")
        new_game = input("Do you want to start a new game? Type (y/n)").strip().lower()
        if new_game == "y":
            board = [" " for i in range(9)]
            print_board()
            print("The losing player starts")
        else:
            break
    elif is_draw():
        print("It's a draw")
        new_game = input("Do you want to start a new game? Type (y/n)").strip().lower()
        if new_game == "y":
            board = [" " for i in range(9)]
            print_board()
            print("Player X starts")
        else:
            break
    
    
    
    

