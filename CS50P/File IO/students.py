import csv

"""
with open ("students.csv") as file:
    for line in file:
        name,number=line.rstrip().split(",")
        print(f"{name} is in {number}")
"""
"""
students=[]

with open ("students.csv") as file:
    for line in file:
        name,number=line.rstrip().split(",")
        students.append(f"{name} is in {number}")

for student in sorted(students):
    print(student)
"""


"""
with open ("students.csv") as file:
    for line in file:
        name,number=line.rstrip().split(",")
        student={"name":name , "number":number}
        students.append(student)
"""
"""
def get_name(student):
    return student["name"]
"""
"""
students=[]

with open ("students.csv") as file:
    reader=csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"],"number":row["number "]})


for student in sorted(students,key=lambda student:student["name"]):
    print(f"{student['name']} is in {student['number']}")
"""

name=input("What's your name?")
number=input("What's your number?")

with open ("students.csv","a") as file:
    #writer=csv.writer(file)
    writer=csv.DictWriter(file,fieldnames=["name","number"])
    #writer.writerow([name,number])
    writer.writerow({"name":name,"number":number})


