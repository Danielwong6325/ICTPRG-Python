#There are three set of username and password and i just define all three of them with the first username as ua short for usernamea
#second one and ub short for usernameb and so on
ua='bob'
pa='password1234'
ub='fred'
pb='happyPass122'
uc='lock'
pc='passwithlock44'
#the two input allow the users to enter the username and password also define the username and password as whatever they enter 
username = input("Please enter your username:")
password = input("Please enter your password:")
#from line 13-18 i give them three set of condition to make sure the specific username only link with the correct password
#so when username="bob" and the password= "password1234", print access granted
if (username == ua):
    if(password == pa):
        print("access granted")
#if username is equal to "bob" but the password does not equal to "password1234" it will deny access 
    elif (username == ua):
        if(password != pa):
            print("access denied")
#if the username does not equal to "bob" and the password is correct, it will also deny access 
    elif(username != ua):
        if(password == pa):
            print("access denied")
#the process and explanation from 12-24 will be the same for the following code but the username and password will change 
#  to the two other different username and password combinations              
if (username == ub):
    if(password == pb):
        print("access granted")
    elif (username == ub):
        if(password != pb):
            print("access denied")
    elif(username != ub):
        if(password == pb):
            print("access denied")
if (username == uc):
    if(password == pc):
        print("access granted")
    elif (username == uc):
        if(password != pc):
            print("access denied")
    elif(username != uc):
        if(password == pc):
            print("access denied")