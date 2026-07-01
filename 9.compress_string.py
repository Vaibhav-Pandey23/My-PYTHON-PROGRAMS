'''
QUESTION:9.	String Compression (Run-Length Encoding): Compress a string 
like aabcccccaaa to a2b1c5a3. If the "compressed" string is not smaller
than the original, return the original.
'''

s=input("Enter the string")
compressed_string=s[0]
current_char=s[0]
count_char=0
for i in s:
    if(i==current_char):
        count_char+=1
    
    else:
        compressed_string+=str(count_char)
        count_char=1
        current_char=i
        compressed_string+=i

final_string=compressed_string+str(count_char)  
if(final_string==("1".join(s)+"1")):
    print(s)     
else:
    print(final_string)