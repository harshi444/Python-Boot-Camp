a=int(input())
b=int(input())
x=a*b
while b!=0:
    a,b=b,a%b
print(x//a)