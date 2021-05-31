#Printing out the sum

#the list of value from the question
value =[89, 456, 4, 55, 232, 2, 54, 78, 65, 45, 12, 459, 35616, 45 ,78]
#defining the varable i and total as equal to 0
i=0
total=0
#create a while loop and state that i <0 which is true 
while i < len(value):
#The total will be 0 intially and adding on to the value of the listvalue as it run through the loop i times 
   total = total + value[i]
#the eqution enable the loop to go through the list
   i=i+1
#then printing out the total number 
print(total)

#Printing out the average 

#The first part is same as the sum which create a loop and allow the number to be added to the total as it run through the valuelist
value =[89, 456, 4, 55, 232, 2, 54, 78, 65, 45, 12, 459, 35616, 45 ,78]
i=0
total=0
while i < len(value):
   total = total + value[i]
   i=i+1
#Then for the calculation of the average, we are using the total number of value of the valuelist 
# and dividing the length of the list which give us the average
average = total/len(value)
print('%.f' %(average))

#For the maximum output

#We are using the maximum output max function to print out the maximum funtion present in the valuelist
maximumoutput=max(value)
print(maximumoutput)
