class Student:
    #... # This is a placeholder for the Student class
    def __init__(self, name, house): # , patronum):
        #if not name:
            #raise ValueError("Name cannot be empty")
        #if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            #raise ValueError("Invalid house")
        self.name = name
        self.house = house
        #self.patronum = patronum

    def __str__(self):
        return f" Hi {self.name} from {self.house}! you are welcome to Hogwarts!"
    
    '''
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Name cannot be empty")
        self._name = name
    
    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house
    '''

    @classmethod
    def get(cls):
        name = input("Name: ").title()
        house = input("House: ").title()
        #patronum = input("Patronum: ").title()
        return cls(name, house)

    '''
    def charm(self):
        match self.patronum:
            case "Stag":
                return "Expecto Patronum! 🐎"
            case "Otter":
                return "Expecto Patronum! 🐛"
            case "Hare":
                return "Expecto Patronum! 🐕"
            case _:
                return "Unknown Patronus 🤷‍♀️"
        '''


def main():
    #name= get_name()
    #house= get_house()

    student=Student.get()
    #print(f"Hello, {student['name']} from {student['house']} house!")
    '''
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    '''
    #student.house = "Neverland"
    print(student)
    #print(student.charm())
    #🦉print(f"Hello, {student.name} from {student.house} house!")
    #print(f"Hello, {student['name']} from {student['house']} house!")
    
    #name, house = get_student()
    #print(f"Hello, {name} from {house} house!")

'''
def get_student():
    name= input("name: ").title()
    house= input("house: ").title()
    #patronum= input("patronum: ").title()
    student=Student(name, house) #, patronum)
    return student
'''

'''
    student=Student()
    student.name= input("Name: ").title()
    student.house= input("House: ").title()
    return student
'''

    # This function prompts the user for their name and house, and returns a dictionary with the information
'''
    name= input("Name: ").title()   
    house= input("House: ").title()
    return {"name": name, "house": house}
'''


    #defines a dictionary with keys name and house
'''
    student={}
    student["name"] = input("Name: ").title()
    student["house"] = input("House: ").title()
    return student

'''

'''    
    name = input("Name: ").title()
    house = input("House: ").title()
    return [name, house]
'''


'''
def get_name():
    return input("Name: ").title()

def get_house():
    return input("House: ").title()
'''


if __name__ == "__main__":
    main()