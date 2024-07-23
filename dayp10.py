n=input()
s=""
count=0
for i in n:
    if ord(i)==ord('-'):
        count+=1
    else:
        s+=i
print("-"*count+s)        




