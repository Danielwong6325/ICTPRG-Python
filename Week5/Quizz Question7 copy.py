#creating two list, one for putting user input, one for putting replicate
SB = []
RP = []
#define num and allow the user to input number
num = input("Enter some number (press x to stop):")
while (num!='x'):
#using while loop and allow the number to be added to the SB list after each round
   SB.append(num)
   num = input("Enter some number (press x to stop):")
#using i for the first element on the list
for i in range(len(SB)):
#using x for any element from i onward 
    for x in range(i,len(SB)):
#set i does not equal x to avoid element from the same position comparing against itself
        if i!=x:
#after going through the list, if the number are repeated which is same in position i and x
#the number will be added to the RP list
            if SB[i] == SB[x]:
                RP.append(SB[i])
                break
#The sorted and set function allow the list to avoid repeated number and sorted properly
print("Repeating numbers:",sorted(set(RP)))