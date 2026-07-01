'''
QUESTION:8.	Balanced Parentheses (The Multi-Bracket Problem): Given a
string containing (), [], and {}, determine if the input string is valid 
using a list as a manual stack.
'''
s = "()[]{(()}" 
mapping = {"]": "[", ")": "(", "}": "{"}
stack=[]
is_valid=True
for char in s:
    #pushing the opening brackets into the stack
    if(char in mapping.values()):
        stack.append(char)
    
    #if closing bracket then, checking if the top element is same opening
    #bracket or not 
    elif(char in mapping):
        if stack and stack[-1]==mapping[char]:
            stack.pop()
        else:
            is_valid=False
            break

print(is_valid)