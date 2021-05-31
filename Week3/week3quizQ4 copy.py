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
#in the following i am using two id statement if both the username and the password, if username and password are true print access granted,
#  else access denied 
if (username == ua):
    if(password == pa):
        print("access granted")
    elif (username == ua):
        if(password != pa):
            print("access denied")
    elif(username != ua):
        if(password == pa):
            print("access denied")
print("access denied")