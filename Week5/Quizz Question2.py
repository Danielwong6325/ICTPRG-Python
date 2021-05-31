#allow the user to input the date 
date = input("Please enter the date in the form of dd/mm/yyyy")
#make a split function that will split the input date information from the / 
seperateda = date.split("/")
#we are printing the first element in the list of input and present in the form of date: input, Month from the second element and 
# year from the third
print("Date:", seperateda[0])
print("Month:", seperateda[1])
print("Year:", seperateda[2])

