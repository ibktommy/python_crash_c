# Password Checker

# get user details
username = input("Enter your name: \n")
password = input("Enter your password: \n")

# convert user password to '*' character
length_password = len(password)
coded_password = "*" * length_password

# print user details
print(f'{username.title()}, your password {coded_password} is {length_password} letters long')