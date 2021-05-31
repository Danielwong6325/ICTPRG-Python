def Getpasswordfromuser():
    SpecialSym =['$', '@', '#', '%','!','*','?','/','-','^','&']
    while True:
        try:
            pas = str(input("Please enter your password"))
            for i in len(pas):
                if pas.upper <1:
                    raise ValueError("You need at least one uppercase letter")
                if pas.lower <1:
                    raise  ValueError("You need at least one lowercase letter")
                if len(i) <7:
                    raise ValueError("You need to have a longer password")
                if pas == ("Password"):
                    raise ValueError("The password word should not contain the word ""password")
                if not any(SpecialSym in pas):
                    raise ValueError("Password should have at least one of the symbols $@#")
                else:
                    print("You have a valid password")
            return pas
        except  ValueError as err:
                print(err)
Getpasswordfromuser()    

            
