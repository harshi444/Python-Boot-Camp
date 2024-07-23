#wap to print all the vowels followed by consonants
vowel="aeiou"
consonant="bcdfghjklmnpqrstvwxyz"
n=input()
a=n.lower()
ans=""
for i in a:
    if i in vowel:
        ans+=i              
for i in a:
    if i in consonant:
        ans+=i
print(ans)                