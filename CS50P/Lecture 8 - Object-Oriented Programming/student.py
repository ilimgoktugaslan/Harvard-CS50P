import sys

class Student:
    def __init__(self,name,house):
        if not name: #== if name==""
            raise ValueError("Missing name")
        """
        if house not in ["ankara","manisa","izmir"]:
            raise ValueError("Invalid house")
        """
        self.name=name
        self.house=house
        #self.patronus=patronus


    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @property                       
    def house(self):
        return self._house
    
    @house.setter
    def house(self,house):
        if house not in ["ankara","manisa","izmir"]:
            raise ValueError("Invalid house")
        self._house=house

            
    """
    def charm(self):
        match self.patronus:
            case "Stag":
                return "stag"
            case "Otter":
                return "otter"
            case "Jack Russel terrier":
                return "Jack Russel terrier"
            case _:
                return "nothing"
    """

def main():
    #name=get_name()
    #house=get_house()
    student = get_student()
    #print(f"{student.name} from {student.house}")
    #print("Expecto Patronum!")
    #print(student.charm())
    print(student)
    


"""    
def get_name():
    return input("Name:")
    
def get_house():
    return input("House:")
"""

def get_student():
    """
    n=input("Name:")
    h=input("House:")
    return [n,h]
    """
    #return (n,h) we can use tuples when we don't want to change our datas.
    """
    student={}
    student["name"]=input("Name:")
    student["house"]=input("House:")
    """
    """
    name=input("Name:")
    house=input("House:")
    return {"name":name,"house":house}
    """
    """
    student=Student()
    student.name=input("Name: ")
    student.house=input("House: ")
    return student
    """
    name=input("Name: ")
    house=input("House: ")
    #patronus=input("Patronus: ")
    return Student(name,house)

    

if __name__=="__main__":
    main()


# Good design version

class Student:
    def __init__(self,name,house):
        if not name: #== if name==""
            raise ValueError("Missing name")
        self.name=name
        self.house=house


    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @classmethod
    def get(cls):
        name=input("Name: ")
        house=input("House: ")
        return cls(name,house)


def main():
    student = Student.get()
    print(student)
    
    

if __name__=="__main__":
    main()

