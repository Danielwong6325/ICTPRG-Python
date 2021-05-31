#define the list of number provided as numlist
numlist = [66,43,1,6,2,99,4]
#define variable i equal 0
i=0
#using a while loop to stated that the number of variable i will be less than the length of the numlist defnied which is true.
while i < len(numlist):
#using an if statement to say that if the number presented in the list is less than 10 than print the number out
    if numlist[i] <10:
        print(numlist[i])
    i+=1
#the eqution make sure that the loop run through all the character in the list