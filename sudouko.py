board = [
    [0,1,0,9,0,0,0,0,0],
    [0,0,0,9,5,0,0,9,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]
def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        x,y=find
       # print(find)
    for i in range(1,10):
        if valid(i,bo,x,y): 
            bo[x][y]= i
            if solve(bo): return True
            bo[x][y]=0
    
    return False
def valid(num,bo,x,y):
    #check row
    for i in range(9):
        if bo[x][i]==num and i!=y: return False
    #check col
    for i in range(len(bo)):
         if bo[i][y]==num and i!=x: return False
    box_x=x//3
    box_y=y//3
    for i in range(box_y*3,box_y+3):
        for j in range(box_x*3,box_x+3):
            if bo[i][j]==num and (i,j)!=(x,y): return False
    return True
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None
print_board(board)
print("___________________________________________")
print(solve(board))
print_board(board)
