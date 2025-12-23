# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Ximena Yepez
# Section: Section 548
# Assignment: Lab: Topic 4 activity #1
# Date: 23/09/2025
#



from math import *

#Ask for user input
num1 = (float(input("Enter number 1:")))
num2 = (float(input("Enter number 2:")))
num3 = (float(input("Enter number 3:")))


#check for greater number
if (num1 > num2) and (num1 > num3) :
    greatest = num1
elif (num2 > num3) and (num2 > num3) :
    greatest = num2
else:
    greatest = num3

#state greatest
print (f"The largest number is {greatest}")
