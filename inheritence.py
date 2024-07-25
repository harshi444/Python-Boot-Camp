#single level inheritence
#class Animal:
    #def speak():
        #return "animal is speaking"
#class Dog(Animal):
    #def bark():
        #return "bow"
#obj1=Animal
#obj2=Dog
#print(obj1.speak()) 
#print(obj2.speak())
#print(obj2.bark())   



#Multilevel inheritence
#class Animal:
    #def speak():
        #return "animal is speaking"
#class Dog(Animal):
    #def bark():
        #return "bow"
#class Puppy(Dog):
    #def boo():
        #return "boo"
#obj1=Animal
#obj2=Dog
#obj3=Puppy
#print(obj3.speak())
#print(obj3.bark())
#print(obj3.boo())


# Multiple inheritence


class Mother:
    def speak():
        return "hi"
class Father:
    def shout():
        return "hello"
class Kid(Father,Mother):
    def talk():
        return "whatsapp"
obj1=Mother
obj2=Father
obj3=Kid
print(obj3.speak())
print(obj3.shout())
print(obj3.talk())