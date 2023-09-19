def main():
    yell(["This", "is", "CS50"])

def yell(*words):
    """
    print(phrase.upper())
    for word in words:
        print(word,end="")
    
    uppercased=[]
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)
    """
    uppercased=[word.upper() for word in words]
    print(*uppercased)




if __name__ =="__main__":
    main()
    