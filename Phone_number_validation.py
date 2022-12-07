import re
phone_regex = '^(\+?\d{0,2}\-?\s?)?\(?\d{3,4}\)?[\s.-]?\d{3}[\s.-]?\d{3,4}$'
phone_number=input("Enter the Phone Number")
match = re.search(phone_regex, phone_number)
print(match)
if match:
    print("Valid")
else:
    print("Invalid")
