import wikipedia
def calc():
    a=input("operate two numbers ")
    # 1 function
    b=a.split()
    x=[]
    for i in b:
        if i.isdigit() and 'add' in b:
            k=int(i)
            x.append(k)
        elif i.isdigit() and 'subtract' in b:
            k=int(i)
            x.append(k)
        elif i.isdigit() and 'divide' in b:
            k=int(i)
            x.append(k)
        elif i.isdigit() and 'multiply' in b:
            k=int(i)
            x.append(k)
    if 'add' in b :
        c=x[0]+x[1]
    elif 'subtract' in b :
        c=x[0]-x[1]
    elif 'multiply' in b :
        c=x[0]*x[1]
    elif 'divide' in b :
        c=x[0]/x[1]
    print(c)    
def interact():
    def greet():
        print("Hello sir, I am your personal AI ")
    greet()
    ask=input("What do you want to do today ? ")
    if "who are you" in ask.lower():
        print("I am Bot_1 , your personal AI created by PrateekIndustries pvt. ltd. ")
    elif "write a story" in ask.lower():
        print("writing the story... ")
        z="once upon a time in jungle lived a parrot... "
        with open("story.txt","a") as f:
            f.write(z)
        read_s=input("wanna read it (yes/no) ")
        if read_s.lower()=="yes" :
            with open("story.txt","r") as f1:
                a=f1.read()
            print(a)
    elif "open calculator" in ask.lower():
        calc()
    elif "play game" in ask.lower():
        pass
    elif "search" in ask.lower():
        search_results = wikipedia.search(ask, results=5)
        print(search_results)
    elif "exit" in ask.lower():
        print("Thank you ")
        print("Deactivating...")
        print(".done..")

act=input("For activating say 'Wake Up' - ")
if act.lower() == "wake up" :
    print("AI activated... ")
    interact()
else:
    print("__invalid__")

