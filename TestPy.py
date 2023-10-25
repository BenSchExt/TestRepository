import math;

a = 1
b = 2
the_world_is_flat = True
astring = "abcdefghijklmnopqrstuvwxyz"

c = a + b
print(c)

if the_world_is_flat:
    print("Be careful not to fall off!")

print(astring[:4])
print(astring[4:])
astring = astring + "_appendix"
print(astring)

a, b = 0, 1
while a < 10000:
    print(a, end=",")
    a, b = b, a+b

for n in range(2, 9):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

class MyClass:

    prop0: str
    prop1 = 2
    prop2: bool
    prop3: list
    prop4: str

    def __init__(self):
        self.prop0 = "lululu"
        self.prop1 = 1
        self.prop2 = False
        self.prop3 = [2,3]
        self.prop4 = "4"

    def f(self):
        return "hello world"

x = MyClass()
print(x.prop1)
print(x.prop2)
x.f()

class MyClass2(MyClass):
    def __init__(self):
        self.prop0 = "lelele"

    def q(self):
        return self.y

p = MyClass2()

print(p.prop0)
print(p.prop1) #inherited from MyClass