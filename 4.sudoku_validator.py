valid_board = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]


invalid_subgrid_board = [
    [5, 3, 4, 6, 7, 8, 9, 1, 5],  # <-- Row 1: Two 5s (starts and ends with 5)
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 2],  # <-- Swapped to keep the 3x3 box valid
    [3, 4, 5, 2, 8, 6, 1, 7, 9]   # <-- Column 9: Also fails because of the top 5
]


invalid_subgrid_board = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 3, 3, 4, 2, 5, 6, 7],  # <-- [2][2] changed to 3. Top-left 3x3 box now has two 3s!
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

#validate the rows 
flag_rows=True
count=0
for i in range(1,10):
    for j in range(9):# rows
        for k in range(9):# columns
            if(invalid_subgrid_board[j][k]==i):
                count+=1
    
        if(count>1):
            flag_rows=False
        count=0

count=0
#validate the columns
flag_columns=True
for i in range(1,10):
    for j in range(9):# rows
        for k in range(9):# columns
            if(invalid_subgrid_board[k][j]==i):
                count+=1
    
        if(count>1):
            flag_columns=False
        count=0 


#validate the 3X3 matrices 
p=0
q=0
flag_matrices=True
for i in range(1,10):# to check the uniqueness of numbers 
    for j in range(3):# to 3 scoops 
        for k in range(3): # to run 3 matrices for a single scoop 
            for l in range(p, p+3):# rows in a 3X3 matrix
                for m in range(q, q+3):# columns in a 3X3 matrix
                    if(invalid_subgrid_board[l][m]==i):
                        count+=1
            if(count>1):
                flag_matrices=False
            count=0
            q+=3
        q=0
        p+=3
    p=0
    q=0        
   

print(f"Validity of rows: {flag_rows}")
print(f"Validity of columns: {flag_columns}")
print(f"Validity of subgrids: {flag_matrices}")

if(flag_rows==False or flag_matrices==False or flag_columns==False):
    print("invalid sudoku")
else:
    print(" congratulations ")


                

        
    
