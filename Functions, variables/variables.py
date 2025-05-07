#Ask user for their name
#a="Hello,"

#Say hello to the user
name = input("what is your name? ").strip().title()

print(f"hello, {name}")


#name = name.title() #convert the string to Upercase
#name = name.capitalize() #capitalize the first letter of the string, but just the first letter
'''
print(f'{a}', end='') #can use end to not go to the next line, and can use sep to separate the strings
print(f'{name}')
'''
#print(f'{a} {name}') #f-string is a way to format strings in python, it is a way to embed expressions inside string literals


