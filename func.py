def even_odd(num):
    if num%2==0:
        print("the num is even")
    else:
        print("te num is odd")
even_odd(24)

#### multiple parameters
def add(a,b):
    return a+b
print(add(5,6))

### default parameter
def greet(name="guest"):
    print(f"Hello {name},Welcome to the world")
greet("vidya")