n=input()
for i in range(len(n)//2):
    if(n[0]==n[-1]):
        print(f"{n} is palindrome")
    else:
        print(f"{n} not a palindrome")    