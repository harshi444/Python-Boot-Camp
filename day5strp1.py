#print(ord('H'))
#print(ord('H')+3)
#123-127 special chars
#91-96 special char
#0 - 48
#A - 65
#a - 97
# check no of vowels in a string and consonants inn a string
n=input()
a=n.lower()
count=0
c=0
abc="bcdfghjklmnpqrstvwxyz"
li=['a','e','i','o','u']
for i in a:
    if i in li:
        count+=1
print(count)        
for i in a:   
    if i in abc:
        c+=1    
print(c)           