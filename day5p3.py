#unique elements in a string
n=input()
a=n.lower()
s=""
for i in a:
    if i not in s:
        s+=i
print(s)
