import re
address = input("Enter your email address: ")
    # Regular expression for validating email addresses
regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Check if the email matches the pattern
if re.match(regex, address):
     print("valid email")
else:
    print('not matched ')
