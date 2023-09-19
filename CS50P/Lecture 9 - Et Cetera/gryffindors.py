"""
students =[
    {"name":"Hermonie","house":"Gryffindor"},
    {"name":"Harry","house":"Gryffindor"},
    {"name":"Ron","house":"Gryffindor"},
    {"name":"Draco","house":"Slytherin"},
    
]

gryffindors=[
    student["name"] for student in students if student["house"]=="Gryffindor"
]

for gryffindor in sorted(gryffindors):
    print(gryffindor)

def is_gryffindor(s):
    return s["house"] == "Gryffindor"

gryffindors=filter(is_gryffindor,students)

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])
    
"""

students=["Hermione","Harry","Ron"]
"""
gryffindor=[]

for student in students:
    gryffindor.append({"name":student,"house":"Gryffindor"})

gryffindor=[{"name":student,"house":"Gryffindor"} for student in students]

gryffindor={student:"Gryffindor" for student in students}

print(gryffindor)
"""
"""
for i in range(len(students)):
    print(i+1,students[i])
"""
for i, student in enumerate(students):
    print(i+1,student)