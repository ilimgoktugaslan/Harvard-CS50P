def main():
    name=input("What's your name?")
    print=hello(name)
    #hello(name)

def hello(to="world"):
    return f"hello,{to}"
    #print("hello,",to)

if __name__=="__main__":
    main()