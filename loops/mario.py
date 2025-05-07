def main():
    print_Square(3)

def print_Square(size):
    for i in range(size):
        print("#" * size)

main()



'''
def main():
    print_Square(3)

def print_Square(size):
    #For each row
    for i in range(size):
        #For each column in the row
        for j in range(size):
            print("#", end="")
        #Print a new line after each row
        print()

main()
'''


'''
def main():
    print_row(4)

def print_row(width):
    print("?" * width)

main()
'''

'''
def main():
    print_column(3)

def print_column(height):
    print("#\n" * height, end="")

main()
'''
