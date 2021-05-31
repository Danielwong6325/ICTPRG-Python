#The fisrt line is the allow the user to enter the number and also define the word number as the number user put in
number = int(input("Enter a number:"))
#Then i created a while loop for number that is not in the range and print the word not within range as well as allowing the user to reenter a number
while(number<50 or number>70):
    print("not within range")
    number = int(input("Enter a number:"))
#else condition to say if the number is within range, just print it is within the range 
else:
    print("within range")
    