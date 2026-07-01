'''
QUESTION:5.	Roman Numeral Converter: Write a program that converts integers
to Roman numerals and vice versa up to 3999 using an optimized dictionary 
mapping
'''

glossary={ 
    1 :"I",
    2 :"II",
    3 :"III",
    4 :"IV",
    5 :"V",
    6 :"VI",
    7 :"VII",
    8 :"VIII",
    9 :"IX",
    10 :"X",
    20 :"XX",
    30 :"XXX",
    40 :"XL",
    50 :"L",
    60 :"LX",
    70 :"LXX",
    80 :"LXXX",
    90 :"XC",
    100 :"C",
    200 :"CC",
    300 :"CCC",
    400 :"CD",
    500 :"D",
    600 :"DC",
    700 :"DCC",
    800 :"DCCC",
    900 :"CM",
    1000:"M",
    2000:"MM",
    3000: "MMM",   
}

num=int(input("Enter the number"))
l=[]
count=0
result=""
while(num!=0):
    rem=num%10
    num=num//10
    l.append(rem*10**count)
    count+=1

roman_string=""
for items in reversed(l):
    roman_string+=glossary[items]
print(f"The roman number of above integer is {roman_string}")

# for i in range(1, 4000):
s=input("Enter the roman number")
actual_number=0
for characters in s:
    if [k for k, v in glossary.items() if v == 2][0]==characters:
        actual_number





    
