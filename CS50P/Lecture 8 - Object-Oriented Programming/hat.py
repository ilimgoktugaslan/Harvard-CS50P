import random

class Hat:
    
    houses=["ankara","izmir","manisa"]

    @classmethod
    def sort(cls,name):
        print(name,"is in",random.choice(cls.houses))  


Hat.sort("ilim")