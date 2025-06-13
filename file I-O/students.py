
import csv

name= input("Enter your name: ").strip().title()
country= input("Enter your country: ").strip().title()  

with open("students.cvs", "a") as file:
    writer=csv.DictWriter(file, fieldnames=["name", "country"])
    writer.writerow({"name": name, "country": country})

    #writer=csv.writer(file)
    #writer.writerow([name, country])


'''
students=[]
#readin a dictionary from a file and printing it in sorted order
with open("students.cvs") as file:
    reader=csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "country": row["country"]})  #or just .append(row)

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['country']}")
'''


''' ##reading names from a file using csv reader and printing them in sorted order (short version)
    reader=csv.reader(file)
    for name, country in reader:
        students.append({"name": name, "country": country})
    '''

'''#reading names from a file and printing them in sorted order (long version)
    for line in file:
        name, country = line.rstrip().split(",")
        student={"name": name, "country": country}
        students.append(student)
        '''



'''
def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name):
        print(f"{student['name']} is in {student['country']}")
'''



'''
        students.append(f"{name} is in {country}")

for student in sorted(students):
    print(student)
'''

        #row = line.rstrip().split(",")
        #print(f"{row[0]} is in {row[1]}")

