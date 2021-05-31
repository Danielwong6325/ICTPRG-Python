#the first two line is to define the correct password as usernamet and passwordt
usernamet='bob'
passwordt='password1234'
username2='fred'
password2='happyPass122'
username3='lock'
password3='passwithlock44'
#the two input allow the users to enter the username and password also define the username and password as whatever they enter 
username = input("Please enter your username:")
password = input("Please enter your password:")
#in the following i am using two id statement if both the username and the password, if username and password are true print access granted,
#  else access denied 
if (username == usernamet):
    if(password == passwordt):
        print("access granted")
else:
    print("access denied")