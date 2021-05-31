#Ask user for the input of their username and password
user = input("Username? ")
pas = input("password? ")
#Create a dictionary in a file called logins.txt and then close the file
Q3file=open ("logins.txt","w")
passworddic= dict({"user1":"password0", 
"usere2":"password1","user3":"password2","user4":"password3", })
Q3file.close()
#Open the file i just created and read the list in the file for comparing username and password
Q3file=open ("logins.txt","r")
userlist = Q3file.read()
Q3file.close()
#set the condition if the user is in the dictionary and if the password is also in the dictionary and matching, it will print access granted otherwise, it will print access denied
if user in passworddic and passworddic.get(user) == pas:
    print("Access Granted")
else:
    print("Access Denied")