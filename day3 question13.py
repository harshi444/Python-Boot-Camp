#replace the elements in an array with avg of maximum and minimum element
li=list(map(int,input().split()))
m=li[0]
a=li[0]
for i in range(len(li)):
    if li[i]>m:
        m=li[i]
for i in range(len(li)):
    if li[i]<a:
        a=li[i]
avg=(m+a)//2
for i in range (len(li)):
    li[i]=avg
print(li)           


