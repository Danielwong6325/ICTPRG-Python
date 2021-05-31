
number_list = [1,2,3,5,8,2,5.2,10.5,12,15.9]
total= 0
i= 0
while i< len(number_list):
    total = total + number_list[i]
    i = i + 1
    avg = total / len(number_list)
print("The average is: %.2f" %(avg))

