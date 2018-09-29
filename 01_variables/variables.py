#this is our constant values...
import constant

import math

#this is a VARIABLE - its value can be changed.
THIS_YEAR_VARIABLE = '2005'

#here we are printing the value of the christmas day constant (this gets imported in the line 'import chrimbo').
print('Christmas day is on the : ' + constant.CHRISTMAS_DAY_CONSTANT )

#Whilst a VARIABLE can hold different values at different times - now it prints '2005'
print('now we are printing the value of the variable : ' + THIS_YEAR_VARIABLE )

print("the value of the constant pi is.... " + str(math.pi))

#the value of our variable is just about to change - now we are asking python to tell us the year and assign it to our variable.
THIS_YEAR_VARIABLE = '2018'

#The value has now been changed - so we can say that its value is ...well VARIABLE!
print('now the value of our  THIS_YEAR_VARIABLE has been changed : ' + THIS_YEAR_VARIABLE )

# CONCATENATION just means stick this variable, on to that variable.
# the + operator tells python to do this.
print('Christmas day is on the : ' + chrimbo.CHRISTMAS_DAY_CONSTANT + ' ' +  THIS_YEAR_VARIABLE)
