def main_welcome(fun): ##function as parameter
    def sub_welcome():
        print("welcome to the family")
        fun()
        print("please respect elders")
    return sub_welcome()

## Manual method
"""def family_info():
    print("Malayil family")
main_welcome(family_info)
"""
##### using decorators
@main_welcome
def family_info():
    print("Malayil family")

