"""
first,_=input("What's your name? ").split(" ")
print(f"Hello,{first}")
"""

def total(galleons,sickles,knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins=[100,50,20]

print(total(coins[0],coins[1],coins[2]),"Knuts") 

