'''
i = 3
while i != 0:
    print("meow") 
    i -= 1
'''

'''
i=0
while i < 3:
    print("meow")
    i += 1
'''

'''
for i in [0, 1, 2]:
    print("meow")
'''

'''
for i in range(3):
    print("meow")
'''

'''
print("meow\n" * 3, end="")
'''

'''
while True:
    n = int(input("Enter a number: "))
    if n > 0:
        break

for i in range(n):
    print("meow")
'''

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("Enter a number: "))
        if n > 0:
            return n

def meow(n):
    for i in range(n):
        print("meow")

main()