#find min element
li=list(map(int,input().split()))
m=li[0]
for i in range(len(li)):
    if li[i]<m:
        m=li[i]
print(m)       
