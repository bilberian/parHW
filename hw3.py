board = [1,2,3,
         4,5,6,
         7,8,9]

victories = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
 
def print_board():
    print(board[0], end = " | ")
    print(board[1], end = " | ")
    print(board[2])
 
    print(board[3], end = " | ")
    print(board[4], end = " | ")
    print(board[5])
 
    print(board[6], end = " | ")
    print(board[7], end = " | ")
    print(board[8])    
 
def player_input(step,symbol):
    if step in board:
        index = board.index(step)
        board[index] = symbol
    else:
        print ("This cell is taken or no such cell. You miss your move.")
 
def get_result():
    winner = ""
    for i in victories:
        if board[i[0]] == "X" and board[i[1]] == "X" and board[i[2]] == "X":
            winner = "Player1"
        if board[i[0]] == "O" and board[i[1]] == "O" and board[i[2]] == "O":
            winner = "Player2"   
    return winner
 
game_over = False
player1 = True
 
while game_over == False:
    print_board()
    if player1 == True:
        symbol = "X"
        step = int(input("Player1, your move: "))
    else:
        symbol = "O"
        step = int(input("Player2, your move: "))
 
    player_input(step,symbol) 
    winner = get_result() 
    if winner != "":
        game_over = True
    else:
        game_over = False
 
    player1 = not(player1)        
   
print_board()
print(winner + " won")