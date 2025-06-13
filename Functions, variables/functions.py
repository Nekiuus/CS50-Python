#Functions

#def hello(to): #defining a function, to is the parameter of the function, can use any name for the parameter

'''
def hello(to="World"):
    print("Hello,", to) 

hello()
name = input("what is your name? ").strip().title()

hello(name) 
'''

#Calls the function hello with the argument name, which is the name of the user
'''
def main():
    hello()
    name = input("what is your name? ").strip().title()
    hello(name)

def hello(to="World"):
    print("Hello,", to) 
   
main()
'''

def main():
    x= float(input("Enter first number: "))
    print("the square of x is:", square(x)) #calling the function square with the argument x, which is the number entered by the user

def square(m):
    return m * m #returning the square of the number entered by the user

main()