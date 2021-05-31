#first, an input for the user to type in their name
Fn = input("Please enter your full name:")
#The name of the user is split using the split function so that it is easier to get the first letter for the initial
Funa = Fn.split()
initial =""
#using a for funtion to define the range of the length of the name 
for i in range(len(Funa)):
#the initial will be for i number of letter presented in a splited name, the first one, which is 0 
   initial = initial+Funa[i][0]
#Then printing out the full name and the initial 
print("email:", initial)
