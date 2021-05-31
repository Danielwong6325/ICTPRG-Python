#Allow the user to enter an input 
largein = input("Enter a large number: ")
#
list = [int(x) for x in str(largein)]
print("Sum of the digits: ",end= "")
print(*list,sep = " + " ,end= "")
print(" =", sum(list))
