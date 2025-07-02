def password_checker(password):
    if len(password)<8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in "!@#$%^&*" for char in password):
        return False
    return True
print(password_checker("ASDsdf"))
print(password_checker("Asdfg2QWE2@"))