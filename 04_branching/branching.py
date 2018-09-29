
#1. Lets make a list of bank holidays - we get these off school.....
publicHolidaysList = ["Christmas", "Easter", "New Years Day", "May Day", "August Bank Holiday"]

#2. Lets make a list of special days in the year...
specialDaysInTheYear = ["Christmas", "New Years Day","Easter", "My Birthday", "May Day", "August Bank Holiday", "Halloween", "Bonfire Night", "Christmas Eve."]


#3. take the value for each item in the list and put it in a variable called 'day'.
for day in specialDaysInTheYear:

    #2. is day in the list of bank holidays?
    if day in publicHolidaysList:
        #2.1 we got a value of true, this means that it is, so now print...
        print("yippee, " + day + " means a day off school!!")

    #3. the if.. above gave us false, this means it is not a bank holiday, but lets see if it is my birthday? we do this by using ...else if (elif)
    elif day == "My Birthday":
        #3.1 the else if (elif) just came back true - this means it is my birthday so print out...
        print("yippee, " + day + " means presents!!")

    #4. The above elif just returned false, so it is not a bank holiday and it is not my birthday
    else:
        #4.1 so then just print out
        print( day + " is just another ordinary day... ")

#5. Now we go back to the loop (line 3.)and get the next value from the list, put into the variable called day and then examine it again.


issie = 12

if issie >= 11:
    print("go to big school")
else:
    print("go to little school")
