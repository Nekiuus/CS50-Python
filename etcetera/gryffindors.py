students=["Harry", "Hermione", "Ron", "Draco", "Neville", "Luna", "Ginny", "Fred"]

gryffindors = {student: 'Gryffindor' for student in students}  # dictionary comprehension
#gryffindors = [{'name': student, 'house': 'Gryffindor'} for student in students] #list comprehension

#long version
'''
for student in student:
    gryffindors.append({'name': student, 'house': 'Gryffindor'})
'''
print(gryffindors)




# This code filters students from a list based on their house and prints the names of Gryffindors in sorted order.
'''
students=[
    {
        "name": "Alice", "house": "Gryffindor"},
    {
        "name": "Bob", "house": "Hufflepuff"},
    {
        "name": "Charlie", "house": "Ravenclaw"},
    {
        "name": "Diana", "house": "Slytherin"},
    {
        "name": "Eve", "house": "Gryffindor"},
    {
        "name": "Frank", "house": "Hufflepuff"},
    {
        "name": "Grace", "house": "Ravenclaw"},
    {
        "name": "Heidi", "house": "Slytherin"}
]

gryffindors = filter(lambda student: student["house"] == "Gryffindor", students)

for gryffindoe in sorted(gryffindors, key=lambda student: student['name']):
    print(gryffindoe["name"])
'''


'''
gryffindors = [student["name"] for student in students if student["house"] == "Gryffindor"]

for gryffindor in sorted(gryffindors):
    print(gryffindor)
    '''