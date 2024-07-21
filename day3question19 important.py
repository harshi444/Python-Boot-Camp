#reverse of a number
n=int(input())
rev=""#empty string
while(n>0):
    t=n%10
    rev=rev+str(t)
    n=n//10
print(int(rev))  
