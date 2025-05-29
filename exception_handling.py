### try and except
try:
    a=b
except:
    print("value error")

        #### OR
try:
    a=b
except NameError as ex:
    print(ex)

#### try,except,else
try:
    num=int(input("Enter the number"))
    result=10/num
except ZeroDivisionError as ex1:
    print("Enter a number greater than 0")
else:
    print(f"Result is {result}")

#### try,except,else and finally
try:
    num=int(input("Enter the number"))
    result=10/num
except ZeroDivisionError as ex1:
    print("Enter a number greater than 0")
else:
    print(f"Result is {result}")
finally:
    print("Execution is complted")
