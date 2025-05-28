import re
def email_check(email):
    pattern= r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9.+-]+\.[a-zA-Z0-9.+-]+$'
    return re.match(pattern,email) is not None

print(email_check("user.name+filter@domain.co.in"))  # True
print(email_check("invalid-email.com"))  # False