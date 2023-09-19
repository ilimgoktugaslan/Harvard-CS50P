import sys
import argparse

"""
MEOWS=3

for i in range(3):
    print("meow")
"""
"""
class Cat:
    MEOWS=3
    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")

cat=Cat()
cat.meow()
"""
"""
def meow(n:int) -> str:
    
    for _ in range(n):
        print("meow")
    
    #Meow n times
    Meow n times.
    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows , one per line
    :rtype:str
    

    return "meow\n"*n

number:int=int(input("Number: ")) # :int means value has to be integer.
meows:str=meow(number)
#meow(number)
print(meows,end="")
"""
"""
if len(sys.argv)==1:
    print("meow")
elif len(sys.argv)==3 and sys.argv[1]=="-n":
    n=int(sys.argv[2])
    for _ in range(n):
        print("meow")
else:
    print("usage:meows.py")
"""

parser=argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n",default=1, help="number of times to meow", type=int)
args=parser.parse_args()

for _ in range(args.n):
    print("meow")





