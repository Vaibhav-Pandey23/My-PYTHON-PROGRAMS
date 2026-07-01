'''
QUESTION: Anagram Grouping: Given a list of strings, group anagrams 
together. 
SAMPLE INPUT: ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
SAMPLE OUTPUT: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']].
'''

#to check if two entered strings are anagrams of each other
def check_anagrams(s1, s2):
    if("".join(sorted(s1))=="".join(sorted(s2))):
        return True
    else:
        return False

l = ["eat", "tea", "tan", "ate", "nat", "bat"]
grouped_anagrams=[]

for i in l:
    group=[]
    for j in l:
        if(check_anagrams(i, j)==True):
            group.append(j)
    grouped_anagrams.append(group)

print(grouped_anagrams)
grouped_anagrams=set(map(tuple, grouped_anagrams))
print(grouped_anagrams)