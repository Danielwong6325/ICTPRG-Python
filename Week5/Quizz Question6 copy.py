#Allow the user to enter an input 
largein = input("Enter a large number: ")
#This line convert the input number to string 
list = [int(x) for x in str(largein)]
#then the below three lines allow the formatting of 2+9+8 ... and eventually equal the sum of the number in the list
print("Sum of the digits: ",end= "")
print(*list,sep = " + " ,end= "")
print(" =", sum(list))
