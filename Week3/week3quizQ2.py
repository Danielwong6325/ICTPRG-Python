#I make a line which allow user to input their year of birth  
Yob = int(input(" what is your Year of birth"))
# I Stated this year as 2021 
Thisyear = 2021
#Then i make a line calculating the age by subtrcting year of birth from this year so 2021- the year of birth of the user and output it 
print("You are", str(Thisyear-Yob),"Years old")
# making a condition if the result of the calculation show the age of the user is greating than or equal to 18 
if ((Thisyear-Yob)>=18) :
#if the age of the user is greater than or equal to 18 the output come in and have a drink will be display
    print("Come in and have a drink")
#Id the age of the user is less than 18 than the output Go away child will be displayed
else:
    print("Go away. Child.")