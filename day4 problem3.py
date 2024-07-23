#sort elements first half in ascending order second half in descnding order
li=list(map(int,input().split()))
b=li.sort()  
a=len(li)//2
for i in range(a,len(li)):
    b.reverse()
    
