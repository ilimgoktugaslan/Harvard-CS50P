"""
print("meow")
print("meow")
print("meow")
"""
"""
i=0
while i < 3:
    print("meow")
    i+=1
"""
"""
for _ in range(3):
    print("meow")
"""
"""
print("meow \n"*3,end="")
"""

"""
while True:
    n=int(input("What's n?"))
    if n>0:
        break
for _ in range(n):
    print("meow")
"""
"""
def main():
    number = get_number()
    meow (number) # meow function is going to work 3 times.
def get_number():
    while True:
        n=int(input("What's n?"))
        if n>0:
            break
    return n   
def meow(n):
    for _ in range(n):
        print("meow")

main()
"""

# List
"""
students = ["st1","st2","st3","st4"]

for student in students:
    print(student)

for i in range(len(students)):
    print(i+1,students[i])

lessons=["l1","l1","l1","l2"]
"""
"""
students={
    "st1":"l1",
    "st2":"l1",
    "st3":"l1",
    "st4":"l2"
}
print(students["st1"])
print(students["st2"])
print(students["st3"])
print(students["st4"])

for student in students:
    print(student,students[student], sep=",")
"""
"""
students= [
    {"name":"st1","h":"l1","p":"otter"},
    {"name":"st2","h":"l1","p":"stag"},
    {"name":"st3","h":"l1","p":"terrier"},
    {"name":"st4","h":"l2","p":None}

]
for student in students:
    print(student["name"],student["h"],student["p"], sep=",")
"""

# Mario
"""
for _ in range(3):
    print("#")
"""
"""
def main():
    print_column(3) 

def print_column(height): 
    print("#\n"*height, end="")

main()
"""
"""
def main():
    print_row(4)

def print_row(width):
    print("?"* width)
main()
"""
"""
def main():
    print_square(3)

def print_square(size):
    # For each row in square 
    for i in range(size):
        # For each brick in row
        for j in range(size):
            # Print brick 
            print("#", end="")
        print("\n")

main()

"""
"""
def main():
    print_square(3)

def print_square(size):
    # For each row in square 
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#"*width)


main()

"""