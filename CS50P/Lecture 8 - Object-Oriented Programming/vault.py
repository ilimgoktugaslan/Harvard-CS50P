class Vault:
    def __init__(self,galleons=0,sickles=0,knuts=0):
        self.galleons=galleons
        self.sickles=sickles
        self.knuts=knuts

    def __str__(self):
        return f"{self.galleons} Galleons,{self.sickles} Sickles,{self.knuts} Knuts"
    
    def __add__(self,other):
        galleons=self.galleons+other.galleons
        sickles=self.sickles+other.sickles
        knuts=self.knuts+other.knuts
        return Vault(galleons,sickles,knuts)
    

ilim=Vault(100,50,25)
print(f"İlim:{ilim}")

ecem=Vault(25,50,100)
print(f"Ecem:{ecem}")
"""
galleons=ilim.galleons+ecem.galleons
sickles=ilim.sickles+ecem.sickles
knuts=ilim.knuts+ecem.knuts
"""

#total=Vault(galleons,sickles,knuts)
total=ilim+ecem
print(total)


        