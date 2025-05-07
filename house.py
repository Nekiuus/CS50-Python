def main():
    #name= get_name()
    #house= get_house()
    name, house = get_student()
    print(f"Hello, {name} from {house} house!")

def get_student():
    name = input("Name: ").title()
    house = input("House: ").title()
    return name, house

'''
def get_name():
    return input("Name: ").title()

def get_house():
    return input("House: ").title()
'''


if __name__ == "__main__":
    main()