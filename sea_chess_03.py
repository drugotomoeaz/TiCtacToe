board = []
turn = 0

for i in range(3):
    z = ["X", "X", "X"]
    board.append(z)


def print_board(board):
    for b in board:
        print (" ".join(b))
        
print_board(board)


#Player 0 & 1:
def show_board(player):
    exception = True
    while exception:
        try:
            type_row = int(input("***Player %d***\nType row: " % (0 if player == 0 else 1)))
            type_col = int(input("Type column: "))
            if type_row not in (0,1,2) or type_col not in (0,1,2):
                print("It's not on the board.")
            elif board[type_row][type_col] != "X":
                print("That one is chosen already")
            else:
                board[type_row][type_col] = "%d" % (0 if player == 0 else 1)
                print_board(board)
                exception = False
        except:
            print("Warning message: You entered incorrect value")
 #          raise


def check_board(board, player):
    m = str(player)
    if turn == 9:
        print("That was your last turn! Thank you for playing my game!")
        return False
    show_board(player)
    for z in (0,1,2):
        #columns, rows, diagonal 1, diagonal 2
        if (board[0][z] == m and board[1][z] == m and board[2][z] == m)\
                or (board[z][0] == m and board[z][1] == m and board[z][2] == m)\
                or (board[0][0] == m and board[1][1] == m and board[2][2] == m)\
                or (board[0][2] == m and board[1][1] == m and board[2][0] == m):
            print("Congratulations, player %d! You won a victory over your opponent!\n\
                Thank you for playing my game!"% (0 if player == 0 else 1))
            return True
        return False


while not check_board(board, turn % 2) and turn <= 8:
#    print(turn)
    turn += 1
    
end = str()
while end.lower() != "q":
    end = input("This is the end of the game. Please press 'Q' to quit the window! ")   

        
