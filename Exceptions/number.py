
def main():
    x = get_number("Enter a number: ")
    print(f"Your number is: {x}")


def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
            #return x
            #break
        except ValueError:
            #print("Invalid input! Please enter a valid number.")
            pass
            
    #return x        

main()

'''
while True:
    try:
        x=int(input("Enter a number: "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    else:
        break

print(f"The number is: {x}")    
'''


'''
try:
    x=int(input("Enter a number: "))

except ValueError:
    print("Invalid input! Please enter a valid number.")
else:
    print(f"The number is: {x}")
'''


'''
try:
    x=int(input("Enter a number: "))
    print(f"The number is: {x}")

except ValueError:
    print("Invalid input! Please enter a valid number.")
'''