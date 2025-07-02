def is_palindrome(str):
    str=str.lower().replace(" ","")
    return str==str[::-1]

print(is_palindrome("AMMa"))
print(is_palindrome("Hello"))