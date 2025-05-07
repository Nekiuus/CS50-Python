'''
students= ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print (i + 1, students[i])
'''
    
'''
for student in students:
    print (student)
'''

'''
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
'''

students = [
    {"name": "Harry", "house": "Gryffindor", "patrons": "Stag"},
    {"name": "Hermione", "house": "Gryffindor", "patrons": "Otter"},
    {"name": "Ron", "house": "Gryffindor", "patrons": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patrons": None},
]


for student in students:
    print(student["name"], student["house"], student["patrons"], sep=", ")