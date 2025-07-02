"""def square(n):
    for i in range(3): #only got the value 0
        return i**2

print(square(3))"""

def square(n):
    for i in range(3):
        yield i**2

"""print(square(3))

for i in square(3):
    print(i)"""
a=square(3)
a
print(next(a))
print(next(a))
print(next(a))


def my_generator():
    yield 1
    yield 2
    yield 3
gen=my_generator()
#print(next(gen))
   ### or

for i in gen:
    print(i)