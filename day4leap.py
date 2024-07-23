inp=int(input())
ip2=int(input())
for i in range(inp,ip2+1):
    if (i%4==0 and i%100!=0):
        print(i)   