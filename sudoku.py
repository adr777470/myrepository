import numpy as np
import random

def check_sudoku_low(main_sudoku,x,y,k):
    
    for j in range (0,9):
        if(main_sudoku[x][j] == k and j != y):
            return False
    
    for i in range (0,9):
        if(main_sudoku[i][y] == k and i != x):
            return False
            
    p1 = (x // 3) * 3
    p2 = (y // 3) * 3
    for i in range (p1,p1+3):
        for j in range (p2,p2+3):
            if(i == x and j == y):
                continue
            else:
                if(main_sudoku[i][j] == k):
                    return False

    return True
# check_low is finished

def remove_sudoku_numbers(sudoku,n):
    w = 0
    while(w<n):
        ran = random.randint(0,80)
        x1 = ran % 9
        y1 = ran // 9
        if(sudoku[x1][y1] != 0):
            sudoku[x1][y1] = 0
            w += 1
        
    return
# remove_sudoku_numbers is finished

def find_solutions(sudoku,add):
    x = add // 9
    y = add % 9
    
    if(add == 81):
        global count1
        count1 += 1
        print("solution",count1,":")
        print(sudoku)
        return False
    
    if(sudoku[x][y] == 0):
        for i in range (1,10):
            flag = check_sudoku_low(sudoku,x,y,i)
            if(flag):
                s = sudoku
                s[x][y] = i
                flag2 = find_solutions(s,add+1)
                s[x][y] = 0
                    
    else:
        return find_solutions(sudoku,add+1)
    
    return False
#find_solutions is finished.


main_sudoku = np.zeros((9,9),dtype = int)
row = np.arange(9) + 1
n = 51
count1 = 0

for x in range (0,9):
    f = False
    while (f == False):
        np.random.shuffle(row)
        for y in range (0,9):
            k = row[y]
            flag = check_sudoku_low(main_sudoku,x,y,k)
            if(flag == False):
                break
            if(flag == True and y == 8):
                f = True
                main_sudoku[x] = row

print("...لطفا صبور باشيد")                
print("main_sudoku:")
print(main_sudoku)
sudoku = main_sudoku
remove_sudoku_numbers(sudoku,n)
print("sudoku:")
print(sudoku)
find_solutions(sudoku,0)
