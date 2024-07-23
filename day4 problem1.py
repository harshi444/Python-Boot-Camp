n=input("enter the password")
l=len(n)
str="@/"
count=0
if l<8:
    print("invalid") 
for i in n:
    if i==str[0] or str[1] and i!=" ":
        count+=1
        break;
if count==1:
    print("**")
if l>8 and l<12:
    print("weak")  
elif l>12 and l<15:
    print("medium")
elif l==15:
    print("strong")  
else:
    print("please follow and reenter")      
