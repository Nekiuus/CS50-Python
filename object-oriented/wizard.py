class Wizzard:
    def __init__(self, name):
        if not name:
            raise ValueError("Name cannot be empty")
        self.name = name

class Student(Wizzard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

class Professor(Wizzard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

def main():
    print(f"Welcome to Hogwarts, {student.name} from {student.house}!")
    print(f"Hello Professor {professor.name}, you teach {professor.subject}.")
    print(f"Hello Wizzard {wizzard.name}, welcome to the wizarding world!")

student = Student("Harry Potter", "Gryffindor")
professor = Professor("Severus Snape", "Potions")
wizzard = Wizzard("Albus Dumbledore")

if __name__ == "__main__":
    main()