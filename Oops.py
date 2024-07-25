class Myswec:
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a *b
    def div(a,b):
        return a//b
    def mod(a,b):
        return a%b
obj1=Myswec
obj2=Myswec
print(obj1.add(2,5))
print(obj1.sub(7,2))
print(obj2.add(4,5))
print(obj2.sub(10,5))
print(obj1.mul(4,5))
print(obj1.div(6,3))
print(obj1.mod(6,2))
print(obj2.mul(4,5))
print(obj2.div(20,5))
print(obj2.mod(20,5))