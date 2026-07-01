'''
QUESTION:Subsequence Checker: Write a function that takes two strings,
S and T, and checks if S is a subsequence of T (order matters, continuity does not).
EXAMPLE: 'ace' is the subsequence of 'abcde', but 'aec' is not
'''
t=input("Enter the target string")
s=input("Enter the subsequence string")
list_of_indexes=[]
for i in s:
    list_of_indexes.append(t.find(i))

if -1 in list_of_indexes:
    print("false")
elif ( list_of_indexes== sorted(list_of_indexes)):
    print("true")
else:
    print("false")
