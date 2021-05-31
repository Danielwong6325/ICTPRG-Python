#allow user to input the first and second number 
num1 = int(input("Please enter the first number:"))
num2 = int(input("Please enter the second number:"))
#total the two entered number 
total = num1 + num2
#open a file called maths.txt and paste the sum of the number in this text file
Q1file = open("maths.txt","w")
Q1file.write(str(total))
Q1file.close()