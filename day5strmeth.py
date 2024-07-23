#isalpha
#isdigit
#isalam             alpha numeric
#isupper
#islower
#converting lo lower case
#converting to upper case
#title case
#swap case




n=input()
print(n.swapcase())        #converts lower unte upper upper unte lower
print(n.strip())           #removes spaces front and back and doesnt remove the spaces in middle
print(n.replace('a','z'))  # replace a particular element only a replced with z
print(n.split())           # automatic ga string converted into list
print(n.split('a'))        # splits from particular mentioned character
print(n.capitalize())      # only starting letter two words unte only first word letter capital ex: HELLO WORLD->Hello world 
print(n.lower())           # converting into lower
print(n.upper())           # ex-> hello world->HELLO WORLD
print(n.title())           #change first letter into capital  ex-> hello world-> Hello World





n=input()
print(n.isalpha())        #check whether all are aplhabets without spaces and returns true
print(n.isnumeric())      #check whether string is numeric all numbers 
print(n.isalnum())        #checks whether all the characters consists of alphas and numerics
print(n.isascii())        # checks whether the given num is asscii or not
print(n.islower())        # checks if str is converted into lower or not
print(n.isupper())        # checks if str is convertec into upper or not
print(n.istitle())        # checks if str is converted into title or not
print(n.isdigit())        # checks if it is a digit or not ie from 0-9






