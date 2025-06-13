students = [
    {"name": "Alice", "age": 20, "grade": "A"},
    {"name": "Bob", "age": 22, "grade": "B"},
    {"name": "Charlie", "age": 21, "grade": "C"},
    {"name": "David", "age": 23, "grade": "A"},
    {"name": "Eve", "age": 20, "grade": "B"},
    {"name": "Frank", "age": 22, "grade": "C"},
    {"name": "Grace", "age": 21, "grade": "A"},
    {"name": "Heidi", "age": 23, "grade": "B"},
    {"name": "Ivan", "age": 20, "grade": "C"},
    {"name": "Judy", "age": 22, "grade": "A"}
]

ages= set()
for student in students:
    ages.add(student['age'])

for age in sorted(ages):
    print(f"Age: {age}")
    for student in students:
        if student['age'] == age:
            print(f"  Name: {student['name']}, Grade: {student['grade']}")


