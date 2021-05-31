#Firstly have three input which allow the user to enter their name and age
f1 = input("Please enter your first name:")
f2 = input("Please enter your second name:")
f3 = int(input("Please enter your age:"))
# Then i adjust their age based on my student number
print("adjusted age:", str(f3), "(+1)")
#here i set all the variable and covert the different name input to title, lower and upper as well as strip to remove any space in between
passwordage = (2021 -int(f3 -1))
secondword = f2.title()
firstwordlow = f1.lower().strip()
secondwordlow =f1.lower().strip()
firbre= f1.split()
upp=""
#To extract the first letter i uses a for function and let it run through the splited word and identify the first letter
for x in range(len(firbre)):
    upp = upp + firbre[x][0]
#I then uses the upper function to make it capital as the question required
    up = upp.upper()
#This will be the resulting output
print("Email/password:" +str(secondword) + "."+str(firstwordlow) +"@dogngy.com|%" +str(up)+ str(passwordage)+ str(secondwordlow)+"!") 
#Then i create a while loop so that when the user is not entering empty space, it will continute to run until the user enter an empty space   
while f1!="":
    f1 = input("Please enter your first name:")
    f2 = input("Please enter your second name:")
    f3 = input("Please enter your age:")
    print("adjusted age:", str(f3), "(+1)")
    if f1!="":
        print("Email/password:" +str(secondword) + "."+str(firstwordlow) +"@dogngy.com|%" +str(up)+ str(passwordage)+ str(secondwordlow)+"!")
    else:
        break
