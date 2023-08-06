#from random import choice
import random
import cowsay
import sys
import statistics
import requests
import json

"""
# we can use random to make someting randomly
coin = random.choice(["heads","tails"]) # or choice(["heads","tails"])
print(coin)
"""
"""
# we can use random.randint(x,y) to find random numbers between (x,y)
number=random.randint(0,100)
print(number)
"""
"""
# we can use random.shuffle(x) to shuffle someting randomly
cards=["jack","queen","king"]
random.shuffle(cards)
for card in cards:
    print(card)
"""
"""
# we can use statistics to find some statistics
print (statistics.mean([100,90]))
"""
"""
try:
    print("hello, my name is",sys.argv[1])
except IndexError:
    print("Too few arguments")
"""
"""
# Check for errors
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2 :
    print("Too many arguments")
# Print name tags
print("hello, my name is",sys.argv[1])
"""
"""
if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])
"""

if len(sys.argv) !=2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]) 
#print (json.dumps(response.json(),indent=2))
o = response.json()
for result in o["results"]:
    print(result["traclName"])
