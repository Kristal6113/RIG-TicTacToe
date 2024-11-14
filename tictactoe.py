print()
print("                  Tic Tac Toe")
print("------------------------------------------------")
# create array for board
# player selects spot 1-9
# player is x or o
# player x starts
# check rows, columns, and diagonal

print("Player X goes first")
print("Player O goes second")
print("Choose spot 1-9 to place X or O")
print("Winner declared when a Player gets three in a row")
print("------------------------------------------------")
print("Player X's Turn")
print()

winner = ""
player = "X"
valid_moves=[1,2,3,4,5,6,7,8,9]
used_moves=[]

board=[[1,2,3],
        [4,5,6],
        [7,8,9]]
for row in board:
    for col in row:
        print("|",col,"|", end=" ")
    print()
print()


while winner == "":
    if player == "X" and winner=="":
        move = int(input("Player X's Move: "))
        if (move in used_moves) or (move not in valid_moves):
            print()
            print("-----INVALID MOVE-----")
            print()
            continue
        else:
            for row in range(len(board)):
                for col in range(len(board[row])):
                    if move == 1 and board[0][0]==1:
                        board[0][0]='X'
                        used_moves.append(1)
                        player="O"
                    elif move ==2 and board[0][1]==2:
                        board[0][1]='X'
                        used_moves.append(2)
                        player="O"
                    elif move ==3 and board[0][2]==3:
                        board[0][2]='X'
                        used_moves.append(3)
                        player="O"
                    elif move ==4 and board[1][0]==4:
                        board[1][0]='X'
                        used_moves.append(4)
                        player="O"
                    elif move ==5 and board[1][1]==5:
                        board[1][1]='X'
                        used_moves.append(5)
                        player="O"
                    elif move ==6 and board[1][2]==6:
                        board[1][2]='X'
                        used_moves.append(6)
                        player="O"
                    elif move ==7 and board[2][0]==7:
                        board[2][0]='X'
                        used_moves.append(7)
                        player="O"
                    elif move ==8 and board[2][1]==8:
                        board[2][1]='X'
                        used_moves.append(8)
                        player="O"
                    elif move ==9 and board[2][2]==9:
                        board[2][2]='X'
                        used_moves.append(9)
                        player="O"

                    print("|", board[row][col],"|", end=" ")
                print()
            print()
            if board[0][0]=='X' and board[0][1]=='X' and board [0][2]=='X':
                winner = 'X'
                print("-----WINNER: PLAYER X-----")
                break
            if board[1][0]=='X' and board[1][1]=='X' and board [1][2]=='X':
                winner = 'X'
                print("-----WINNER: PLAYER X-----")
                break
            if board[2][0]=='X' and board[2][1]=='X' and board [2][2]=='X':
                winner = 'X'
                print("-----WINNER: PLAYER X-----")
                break
            if board[0][0]=='X' and board[1][0]=='X' and board [2][0]=='X':
                winner = 'X'
                print("-----WINNER: PLAYER X-----")
                break
            if board[0][1]=='X' and board[1][1]=='X' and board [2][1]=='X':
                winner = 'X'
                print("-----WINNER: PLAYER X-----")
                break
            if board[0][2]=='X' and board[1][2]=='X' and board [2][2]=='X':
                winner = 'X'
                print("-----WINNER: PLAYER X-----")
                break
            if board[0][0]=='X' and board[1][1]=='X' and board [2][2]=='X':
                winner = 'X'
                print("-----WINNER: PLAYER X-----")
                break
            if board[0][2]=='X' and board[1][1]=='X' and board [2][0]=='X':
                winner = 'X'
                print("-----WINNER: PLAYER X-----")
                break
    if player == "O":
        move = int(input("Player O's Move: "))
        if (move in used_moves) or (move not in valid_moves):
            print()
            print("-----INVALID MOVE-----")
            print()
            continue
        else:
            for row in range(len(board)):
                for col in range(len(board[row])):
                    if move == 1 and board[0][0]==1:
                        board[0][0]='O'
                        used_moves.append(1)
                        player="X"
                    elif move ==2 and board[0][1]==2:
                        board[0][1]='O'
                        used_moves.append(2)
                        player="X"
                    elif move ==3 and board[0][2]==3:
                        board[0][2]='O'
                        used_moves.append(3)
                        player="X"
                    elif move ==4 and board[1][0]==4:
                        board[1][0]='O'
                        used_moves.append(4)
                        player="X"
                    elif move ==5 and board[1][1]==5:
                        board[1][1]='O'
                        used_moves.append(5)
                        player="X"
                    elif move ==6 and board[1][2]==6:
                        board[1][2]='O'
                        used_moves.append(6)
                        player="X"
                    elif move ==7 and board[2][0]==7:
                        board[2][0]='O'
                        used_moves.append(7)
                        player="X"
                    elif move ==8 and board[2][1]==8:
                        board[2][1]='O'
                        used_moves.append(8)
                        player="X"
                    elif move ==9 and board[2][2]==9:
                        board[2][2]='O'
                        used_moves.append(9)
                        player="X"
                        
                    print("|", board[row][col],"|", end=" ")
                print()
            print()
            if board[0][0]=='O' and board[0][1]=='O' and board [0][2]=='O':
                winner = 'O'
                print("-----WINNER: PLAYER O-----")
                break
            if board[1][0]=='O' and board[1][1]=='O' and board [1][2]=='O':
                winner = 'O'
                print("-----WINNER: PLAYER O-----")
                break
            if board[2][0]=='O' and board[2][1]=='O' and board [2][2]=='O':
                winner = 'O'
                print("-----WINNER: PLAYER X-----")
                break
            if board[0][0]=='O' and board[1][0]=='O' and board [2][0]=='O':
                winner = 'O'
                print("-----WINNER: PLAYER O-----")
                break
            if board[0][1]=='O' and board[1][1]=='O' and board [2][1]=='O':
                winner = 'O'
                print("-----WINNER: PLAYER O-----")
                break
            if board[0][2]=='O' and board[1][2]=='O' and board [2][2]=='O':
                winner = 'O'
                print("-----WINNER: PLAYER O-----")
                break
            if board[0][0]=='O' and board[1][1]=='O' and board [2][2]=='O':
                winner = 'O'
                print("-----WINNER: PLAYER O-----")
                break
            if board[0][2]=='O' and board[1][1]=='O' and board [2][0]=='O':
                winner = 'O'
                print("-----WINNER: PLAYER O-----")
                break
    print()
print()