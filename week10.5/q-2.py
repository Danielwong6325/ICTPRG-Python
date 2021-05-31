# ask user to input email and number 
ema = str(input("Please enter an email:"))
num = int(input("Please enter a number"))
# use a for function to put a range from 1 to the number of user
for num in range(1,num+1):
    print (num ,"_" + str(ema))
# the function will repeat until the number of time is reaches for entered number