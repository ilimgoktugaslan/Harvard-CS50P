def main():
    x=get_int("What's x?")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try : 
            return int(input(prompt))
        except ValueError:
            print("x is Not an integer")
        """
        else:
            #print(f"x is {x}")
            break
        """
    #print(f"x is {x}")
    return x

main()