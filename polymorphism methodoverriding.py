# method over riding
class Animal:
    def speak():
        return "Speaking"
class Dog(Animal):
    def speak():
        return "talking" 
class Puppy(Dog):
    def speak():
        return "sleeping"
obj3=Puppy
print(obj3.speak())           
    

    
    