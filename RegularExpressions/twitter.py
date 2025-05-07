import re

url=input("URL: ").strip()

if matches := re.search(r"^(https://)?(www\.)?twitter\.com/([a-zA-Z0-9_]+)", url, re.IGNORECASE): #r"^https://twitter.com/(.+)$"

    print(f"Username:", matches.group(3))
'''
#username= re.sub(r"^(https://)?(www\.)?twitter\.com/", "", url)
#username= url.removeprefix("https://twitter.com/", "")
#username= url.replace("https://twitter.com/", "")
print(f"Username: {username}")  
'''