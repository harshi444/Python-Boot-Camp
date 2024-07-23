n=int(input())
count=0
for i in range(2,n**int(0.5)+1):
    if n%i==0:
        count+=1
if count==0:
    print("num is prime")  
else:
    print("num is not prime")          