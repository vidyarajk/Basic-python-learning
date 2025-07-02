def sum(a,b):
    return(a+b)
print(sum(1,3))
def squareOfNum(x):
    return x*x
print(squareOfNum(5))
def SquareOfEachNum(l1):
    l2=[]
    for i in l1:
        l2.append(squareOfNum(i))
    return l2
print( SquareOfEachNum([1,2,3,4]))

            ##OR We can pass function as arg
def squareRootOfNum(x):
    return x**0.5
def cubeOfNum(x):
    return x**3
def squareofeachnum(l1,functionWeNeedToApply):
    l2=[]
    for i in l1:
        l2.append(functionWeNeedToApply(i))
    return l2
print(squareofeachnum([1,2,3,4],squareOfNum))
print(squareofeachnum([1,2,3,4],squareRootOfNum))
print(squareofeachnum([1,2,3,4],cubeOfNum))

