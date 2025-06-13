import re
#function to validate 


email= input("Enter your email: ").strip()
#[^@] for any character except @
#[a-zA-Z0-9_] for any alphanumeric character or underscore
#r"^\w{1,20}@\w{1,6}\.(com|edu|org)$" #matches any string that starts with one or more characters, followed by @, followed by one or more characters, followed by .com
if re.search(r"^\w{1,20}@(\w+\.)?\w{1,6}\.(com|edu|org)$", email, re.IGNORECASE): #r"^.+@.+\.com$" #matches any string that starts with one or more characters, followed by @, followed by one or more characters, followed by .com
    print("Valid email")
else:
    print("Invalid email")






'''

username, domain = email.split("@")

#if username and "." in domain:
if username and domain.endswith(".com"):
    print("Valid email")
else:
    print("Invalid email")
'''