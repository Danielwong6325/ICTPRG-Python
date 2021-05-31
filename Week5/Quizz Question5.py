#Define a square bracket for the input number to be placed in SB= square bracket 
SB=[]
#allow the user to input number 
num = input("Enter some number (press x to stop):")
#Create a while loop that allow user to continue enter number as long as it is not x 
while (num!='x'):
#using append funtion so that the number input from the user will add on to the bracket 
#at first there is no number so it will be the first number the user input then continue add on until x is type in, then 
#list of number in square bracket will print out
   SB.append(num)
   num = input("Enter some number (press x to stop):")
print(SB)