#find the missing number in an array 
#ex 1 2 3 4  6 7 8 9 10
li=list(map(int,input().split()))
n=int(input())
a=n*(n+1)//2
s=0
for i in li:    
    s+=i
print(a-s)    

