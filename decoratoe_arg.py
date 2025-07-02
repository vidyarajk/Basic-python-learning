def repeat(n):
    def decorator(fun):
        def wrapper(*args,**kwargs):
            for _ in range(n):
                fun(*args,**kwargs)
        return wrapper
    return decorator
@repeat(3)
def sayHello():
    print("Hello")
sayHello()