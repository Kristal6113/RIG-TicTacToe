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
board=[[1,2,3],
        [4,5,6],
        [7,8,9]]
for row in board:
    for col in row:
        print("|",col,"|", end=" ")
    print()
print()


while winner == "":
    if player == "X":
        move = int(input("Player X's Move: "))
        for row in board:
            for col in row:
                if move == 1 and col==1:
                    col=chr(88)
                if move ==2 and col==2:
                    col='X'
                if move ==3 and col==3:
                    col='X'
                if move ==4 and col==4:
                    col='X'
                if move ==5 and col==5:
                    col='X'
                if move ==6 and col==6:
                    col='X'
                if move ==7 and col==7:
                    col='X'
                if move ==8 and col==8:
                    col='X'
                if move ==9 and col==9:
                    col='X'
                print("|",col,"|", end=" ")
            print()
        
        print()

            
                    

        



#val = input("Player X's Move: ")

#    for col in row:
#        if col == val:
#            board[row][col] = val
#            print("|",col,"|", end=" ")
#    print()

print()
