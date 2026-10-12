students = []

with open("students.csv") as file:
    for line in file:
        name, country, age = line.rstrip().split(",")
        student = {"name": name, "country": country, "age": age}
        students.append(student)


def get_age(student):
    return student["age"]


for student in sorted(students, key=get_age):
    print(f"{student['name']} is {student['age']} year old in {student['country']}")
