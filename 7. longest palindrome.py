'''
QUESTION: Longest Palindromic Substring: Find the longest substring
 within a given string that reads the same backwards.
'''
s="babad"
def checkPalindrome(s):
    rev=s[::-1]
    if(rev==s):
        return True
    else:
        return False

list_of_longest_palindromes=[]
l=0 # for calculating the length of the longest palindrome
for i in range(len(s)-1):
    for j in range(i+1,len(s)):
        substring=s[i:j+1]
        if(checkPalindrome(substring)==True):
            if(len(substring)>l):
                list_of_longest_palindromes.clear()
                list_of_longest_palindromes.append(substring)
                l=len(substring)
            elif(len(substring)==l):
                list_of_longest_palindromes.append(substring)
                l=len(substring)

print(list_of_longest_palindromes , f" are longest palindromes having length of: {l}")

            
