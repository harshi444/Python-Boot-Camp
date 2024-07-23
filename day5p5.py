n=input()
s=""
a="0123456789"
rem=0
h=""
for i in n:
    if i in a:
        s+=i
print(s) 
b=int(s) 
while b>0:
    t=b%10
    rem=rem*10+t
    b=b//10
h+=str(rem)
print(h)         