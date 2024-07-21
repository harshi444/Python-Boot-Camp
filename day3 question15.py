#find the duplicates remove
li=list(map(int,input().split()))
l=[]
for i in li:
    if i not in l:
        l.append(i)
print(l)        