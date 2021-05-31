#set the flag to false
validvalue = False
#cearting a while loop to allow repeated value input
while not validvalue:
#while it is not the flag name
    legitnumber =input("Please enter a valid number:")
#The condition set for the flag name to be true 
    if legitnumber.isdigit():
         validvalue = True
#Else print statement to remind user to input a valid number
    else:
        print("You must enter a valid number")
#or print the number that enter by the user. 
print("You are" + " " + str(legitnumber))