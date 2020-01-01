from solver import *


isRun = 1


board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]


def get_input(row, col):
    board[row][col] = "*" # replace current position with cursor *
    print("")
    print_board(board)
    num = input("Please enter an integer between 1-9 in the position of the cursor (*), or enter 0 to indicate an empty grid: ")
    
    # if q is pressed, quit
    if num == "q": 
        global isRun
        isRun = 0
    else:
        try:
            if int(num) < 0 or int(num) > 9: # if entered number is above 9 or below 0, prompt user to retry
                print("\nPlease enter a valid integer.")
                get_input(row,col)
            else:
                board[row][col] = int(num)
        except: # if entered input is not an integer, prompt user to retry
            print("\nPlease enter an integer.")
            get_input(row,col)
    

def verify(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if valid(bo, bo[i][j], (i, j)) == False:
                return False
    return True


def main():
    global isRun
    isRun = 1
    print("\n-----------------------")
    print("Sudoku Solver Basic v1.0")
    print("By Justin Sun")
    print("Enter q at any time to quit")
    print("-----------------------")
    
    for i in range(len(board)):
        if isRun == 0:
            break
        for j in range(len(board[0])):
            get_input(i, j)
            if isRun == 0:
                break
            
    if isRun == 1:
        solve(board)
        if verify(board) == False: # verifies board once no grid is left empty
            print("\nInvalid board.")
        elif solve(board) == True:
            print("\nSolution:")
            print_board(board)
        else:
            print("\nNo solutions found.")
    
    
main()