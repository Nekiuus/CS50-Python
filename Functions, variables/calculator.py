'''
x= float(input("Enter first number: ")) #float for decimal numbers, int for whole numbers
y= float(input("Enter second number: "))

z= x / y
print(f"{z:.2f}") 
'''

#z= round(x + y) #rounding the number to 2 decimal places, can also use int() to convert to whole number

#z= round(x / y, 2) #rounding the number to 2 decimal places
#print(f"{z:,}") #using f-string to format the number with commas



#print(round(x + y))

'''
x= input("Enter first number: ")
y= input("Enter second number: ")

z= int(x) + int(y)
print(z)
'''

'''
#Even or odd number
if x % 2 == 0:
    print("x is even")
else:
    print("x is odd")
'''

def main():
    x = int(input("Enter first number: ")) 
    if is_even(x):
        print(f"{x} is even")
    else:
        print(f"{x} is odd")

def is_even(n):
    return n % 2 == 0
    #return True if n % 2 == 0 else False
    '''
    if n % 2 == 0:
        return True
    else:
        return False
    '''
main()

