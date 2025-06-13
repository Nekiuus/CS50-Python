import re

name=input("Enter your name: ").strip().title()

if matches := re.search(r"^(.+), (.+)$", name):
#if matches:
    name= f"{matches.group(2)} {matches.group(1)}"
    #last, first = matches.groups()
    #name= f"{first} {last}"
print(f"Hello, {name}")
