'''
QUESTION: Matrix Rotation: Given an N X N 2D matrix (nested list),
rotate it by 90 degrees clockwise in-place (without allocating another 
matrix).
'''
# for transposing the matrix
def transpose(l):
    return list(map(list,zip(*l)))

l=[[1,2,3,4],[5,6,7,8],[9,10,11,12], [13, 14,15,16]]
trans=transpose(l) 

#exchanging the columns of transposed matrix to show the matrix rotated

lower=0
upper=len(l)-1 
for i in range(len(trans)):
    while(lower<upper):
        t=trans[i][lower]
        trans[i][lower]=trans[i][upper]
        trans[i][upper]=t
        lower+=1
        upper-=1
    lower=0
    upper=len(l)-1

# printing the matrix
for i in range(len(trans)):
    for j in range(len(trans[0])):
        print(f"{trans[i][j]}\t", end="")
    print("")

        




