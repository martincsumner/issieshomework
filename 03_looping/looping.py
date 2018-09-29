
# Lets make a list of bank holidays....
publicHolidaysList = ["Christmas", "Easter", "New Years Day", "May Day", "August Bank Holiday"]

# 1. Now lets print out the values of our publicHolidaysList longhand:
# WATCH OUT - lists start at 0, ie. 0 means first value in our list..
print(publicHolidaysList[0])
print(publicHolidaysList[1])
print(publicHolidaysList[2])
print(publicHolidaysList[3])
print(publicHolidaysList[4])

#2. This is all very nice but it means that we have to physically add a print line for every value in our list.
# we can do the same thing with ITERATION, and this means that we don't have to tell python to print every line.

# The Dictionary decribes ITERATION as....    'perform or utter repeatedly.''

# we are going to use this loop to print out the days of the week...

# this line means loop over our publicHolidaysList and take each value in turn and put it in the 'holiday' variable.
for holiday in publicHolidaysList:
# this line means now print out the value of "day is" and the value of holiday from the line above.
    print("day is",holiday)



#an index loop in python gives you a number for each time the loop runs.
for index, item in enumerate(publicHolidaysList):
    print(index, item);


#a conditional loop runs all the time that the expression being tested returns true.

#lets set a variable to = 0
aNumber=0

#here is a loop - that will run until the value of 'aNumber' is 11.
while aNumber < 10:
    #this line will add 1 to the value for aNumber.
    aNumber = aNumber + 1
    #this line will just print out the value of aNumber
    print(aNumber)
