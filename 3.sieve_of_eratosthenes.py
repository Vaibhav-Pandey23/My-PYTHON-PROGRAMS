'''
QUESTION:SIEVE OF ERATOSTHENES: Generate all prime numbers up to N using this
specific algorithm, optimizing memory by using a boolean list.
'''

import math
n=int(input("Enter the number"))
num_till_n=[]
bool_list=[]

#ADDING THE NUMBERS TILL N, AND DEFINING WHOLE BOOLEAN LIST AS TRUE(DEFAULT)
for i in range(1, n+1):
    num_till_n.append(i)
    bool_list.append(True)

#MAIN ALGORITHM
for i in range(2, math.isqrt(n)+1):

    # CHECKING IF THE NUMBER IS ALREADY FALSE(COMPOSITE)
    if(bool_list[i-1]==False):
        continue
    else:
        # DECLARING THE NUMBER AS TRUE(PRIME), AND ITS NUMBERS DIVISIBLE BY IT AS FALSE(COMPOSITE) 
        for j in range(i+1, n+1):
            if(j%i==0):
                bool_list[j-1]=False

#PRINTING ALL THE PRIME NUMBERS TILL N
for i in range(1, len(bool_list)):
    if(bool_list[i]==True):
        print(num_till_n[i])



    

