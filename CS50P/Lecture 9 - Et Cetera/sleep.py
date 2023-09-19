def main():
    n=int(input("What's n?"))
    for s in sheep(n):
        print(s)


def sheep(n):
    for i in range(n):
        yield "sheep"*i




"""
    #return "sheep"*n
    flock=[]
    for i in range(n):
        flock.append("sheep"*i)
    return flock
"""





if  __name__ == "__main__":
    main()