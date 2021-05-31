#creat a list called SB
SB = []
#Prompt the user to enter a name
nam = str(input("Please enter a name :"))
#create a while loop and keep asking for name until empty space bar is entered 
while nam!='':
#add the name to the list each with a seperate line
      SB.append(nam +"\n")
#allow the user to enter their name if it is not a space bar
      nam = str(input("Please enter a name :"))
#open the file called people.txt and paster the list of name in it 
q2file = open("people.txt","w")
q2file.writelines(SB)
q2file.close()
