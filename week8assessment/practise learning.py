f1 = input("Please enter your first name:")
f2 = input("Please enter your second name:")
f3 = int(input("Please enter your age:"))
print("adjusted age:", str(f3), "(+1)")
passwordage = (2021 -int(f3 -1))
secondword = f2.title()
firstwordlow = f1.lower().strip()
secondwordlow =f2.lower().strip()
firbre= f1.split()
upp=""
for x in range(len(firbre)):
    upp = upp + firbre[x][0]
    up = upp.upper()
    print("Email:" +str(secondword) + "."+str(firstwordlow) +"@dogngy.com|%" +str(upp)+ str(passwordage)+ str(secondwordlow)+"!")    
while f1!="":
    f1 = input("Please enter your first name:")
    f2 = input("Please enter your second name:")
    f3 = input("Please enter your age:")
    print("adjusted age:", str(f3), "(+1)")
    for x in range(len(firbre)):
        upp = upp + firbre[x][0]
        up = upp.upper()
        print("Email:" +str(secondword) + "."+str(firstwordlow) +"@dogngy.com|%" +str(upp)+ str(passwordage)+ str(secondwordlow)+"!")  
    break