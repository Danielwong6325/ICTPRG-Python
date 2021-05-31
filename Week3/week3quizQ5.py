# this start by allowing the student to enter their grade
grade =int(input("What was your grade:"))
#if the grade is greater than or equal to 90, so from 90 onward, High Distinction will be print, in order for the maximum limit to not be over 100, i set and grade less than 
# or equal to 100 for every grade below
if (grade>=90 and grade<=100):
    print("You will receive a", "High Distinction")
# using else if to set another condtion when the grade is greater than or equal to 80 Distinction will present a Distinction
else:
    if (grade>=80 and grade<=100):
        print("You will receive a Distinction")
# using else if to set another condtion when the grade is greater than or equal to 70 Distinction will present a credit
    else:
        if (grade>=70 and grade<=100):
            print("You will receive a Credit")
# using else if to set another condtion when the grade is greater than or equal to 50 Distinction will present a pass
        else:
            if (grade>=50 and grade<=100):
                print("you will receive a Pass")