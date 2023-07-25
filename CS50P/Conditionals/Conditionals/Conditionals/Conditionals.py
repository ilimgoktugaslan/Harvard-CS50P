"""
x=int(input("What's x?"))
y=int(input("What's y?"))

if (x<y):
    print("x is less than y")

elif (x>y):
    print("x is greater than y")

else:
    print("x is equal to y")


if (x<y) or (x>y):
    print("x is not equal to y")


if (x!=y):
    print("x is not equal to y")

if (x==y):
    print("x is equal to y") 

else:
    print("x is not equal to y")
"""
"""
score=int(input("Score:"))

if 90<=score<=100:
    print("Grade:A")
elif 80<=score<90:
    print("Grade:B")
elif 70<=score<80:
    print("Grade:C")
elif 60<=score<70:
    print("Grade:D")
else:
    print("Grade:F")
"""
"""
x=int(input("What's x?"))
if (x%2==0):
    print("Even")
else:
    print("Odd")
"""
"""
def main():
    x=int(input("What's x?"))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if (n%2==0):
        return True
    else:
        return False

# Different type of is_even
def is_even(n):
    return True if n%2==0 else False

# Different type of is_even
def is_even(n):
    return  (n%2==0)
main()
"""

name=input("What's your name?")
"""
if name=="Harry" or name=="Hermione" or name=="Ron":
    print("Gryffindor")
elif name=="Draco":
    print("Slytherin")
else:
    print("Who?")
"""
match name:
    case "Harry"|"Hermione"|"Ron" :
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Drago":
        print("Slytherin")
    case _:
        print("Who?")
