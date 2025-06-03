### Function inside a function

def main_welcome(msg="welcome everyone"): ##local variable inside the main metod also can be use
    #msg="welcome"
    def sub_welcome():
        print("welcome to the family")
        print(msg) ## it can print even it is not belongs to sub function
        print("please respect elders")
    return sub_welcome()
main_welcome()

def main_welcme(fun,lst): ##function as parameter
    def sub_welcome():
        print("welcome to the family")
        print(fun(lst))
        print("please respect elders")
    return sub_welcome()
main_welcme(len,[1,2,3,4,5])
