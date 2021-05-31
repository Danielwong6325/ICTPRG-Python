#create a text file and write the messed up name in it with two lines
Q3_1file = open("names.txt","w")
Q3_1file.write(str("lAchlan velDen" "\n" "Frank joe"))
Q3_1file.close()
#open from the above file and read the content 
Q3_2file = open("names.txt","r")
line = Q3_2file.read()
print(line)
#format the content from the read file using title function
lines = line.title()
#paste the correctly formatted file in to the new text file called the names-formatted.txt
Q3_3file = open("names-formated.txt","w")
Q3_3file.write(str(lines))
Q3_3file.close()