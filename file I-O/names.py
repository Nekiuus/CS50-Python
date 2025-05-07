'''
#reading names from a file and printing them in sorted order (short version)
with open("names.txt") as file:
    for line in sorted(file):
        print(f"Hello, {line.strip().title()}")
'''


names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip().title())

for name in sorted(names, reverse=True): #reverse=True will sort the names in descending order
    print(f"Hello, {name}") 
#reading names from a file and printing them in sorted order (long version)



#reading names from a file and printing them in sorted order (short version)
'''
with open("names.txt", "r") as file:
    for line in file:
        print(f"Hello, {line.strip().title()}")
'''


#long version of the above code
'''
    names = file.readlines()

for name in names:
    print(f"Hello,", name.rstrip().title())
'''

#writing names to a file
'''
name=input("Enter your name: ").strip().title()

with open("names.txt", "a") as file:
    file.write(f"{name}\n")
'''

## Storing names in a file and printing them in sorted order (short version)
'''
file=open("names.txt", "a")
file.write(name + "\n")
file.close()
'''


#storing names in a list and printing them in sorted order
'''
name=[]

for _ in range(3):
    name.append(input("Enter your name: ").strip().title())

for names in sorted(name):
    print(f"Hello, {names}")
'''


