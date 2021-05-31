def Getwordsformuser(min,max):
    while True:
        try:
            if(min >= max):
                print("The minimum should not be greater than maximum")
                break
            multiword = input("Please enter a sentence between" +str(min) +"to" + str(max))
            multiword = multiword.lower()
            tesword = multiword.split(" ")
            if len(tesword) < min or len(tesword)> max:
                raise ValueError ("You have enter an incorrect number of words")
            else:
                print("you enter words under the limitation")
                print(tesword)
                return tesword
        except ValueError as err:
            print(err)


Getwordsformuser(1,4)