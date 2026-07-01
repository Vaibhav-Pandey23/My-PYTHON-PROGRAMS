'''
QUESTION.The Collatz Conjecture Tracker: 
Take a number n. If even, n/2; if odd, 3n + 1. 
Repeat until n=1. Return the path and the
number that produces the longest chain under 100,00.
'''
def collatz_score(n):
    count=0
    while(True):
        n=n//2 if (n%2==0) else 3*n+1
        count+=1
        if(n==1):
            break
    
    return count

answer=1 # to store the number with highest collatz score 
largest=0 # to store the score of winning number
for i in range(1, 10000):
    if (collatz_score(i)> largest):
        largest=collatz_score(i)
        answer=i

print(f"WINNNER IS {answer} WITH A SCORE OF {largest}")

    


    