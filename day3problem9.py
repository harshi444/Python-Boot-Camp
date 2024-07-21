#find the elements present in k+N index  
#k is given by user for ex=k=3 
#input parameters are 3 6 8 4 61 2
#N=2
# k=3 N=2 
#80 70 54 36 72
li=list(map(int,input().split()))
k=int(input())
n=int(input())
l=len(li)
if(l<k+n):
    print("ERROR")
else:
    for i in range(len(li)):
        print(li[k+n],end=" ")
        break
        














    #0r
    #for i in range(len(li))
         #i==k+n
    #print(li[i])

           #print(my_list[k+n],end=" ")
           #break