num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
operation=input("Enter the operator(+,-,/,*,%,**):")
if operation=='+':
    print(num1+num2)
elif operation=='-':
    print(num1-num2)
elif operation=='*':
    print(num1*num2)
elif operation=='%':
    print(num1%num2)
elif operation=='**':
    print(num1**num2)
elif operation=='/':
    if num2!=0:
        print(num1/num2)
    else:
        print("Division by zero error")
else:
    print("Not a valid operator")