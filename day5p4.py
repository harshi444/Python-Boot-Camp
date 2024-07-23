#sum of numbers
#n=input()
#s="0123456789"
#c="aeiou"
#d="bcdfghjklmnpqrstvwxyz"
#sum=0
#a=n.lower()
#for i in a:
 #   if i in s:
 #       sum+=int(i)
#print(sum)        



n=input()
#s="0123456789"
#c="aeiou"
#d="bcdfghjklmnpqrstvwxyz"
sum=0
a=n.lower()
for i in a:
        if (ord(i)>=48 and ord(i)<=57):
          sum+=int(i)
print(sum)        
