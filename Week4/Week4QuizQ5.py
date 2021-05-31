#Set the sum equal to 0 
sum=0
#let the user able to input the number and set whatever that number is equal to num
num = input("Enter some number (Press x to stop)")
#then i used the while loop to set whenever the number is not equal to x then the sum will keep on adding the value of the input number until
#x input is detected
while (num !="x"):
    sum=sum+int(num)
    num = input("Enter some number (Press x to stop)")
# then the total of all those number added up will be presented as Total = whatever that number is
print("Total =",sum)
