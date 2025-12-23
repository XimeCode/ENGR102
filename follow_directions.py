#By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do."
#  "I have not given or received any authorized aid on this assignment."
#
#Name:          Ximena Yepez
#Section:       ENGR 102, Section 548
#Assignment:    LAB: Topic 1
#Date:          02/09/2025
#


print("This shows the evaluation of ((1 - cos(x))/ x^2), evaluated close to x=0")
print("My guess is 1")

from math import *
import math
#evaluate close to x = 0
print((1 - cos(1.0))/(1.0)**2)
print((1 - cos(0.1))/(0.1)**2)
print((1 - cos(0.01))/(0.01)**2)
print((1 - cos(0.001))/(0.001)**2)
print((1 - cos(0.0001))/(0.0001)**2)
print((1 - cos(0.00001))/(0.00001)**2)
print((1 - cos(0.000001))/(0.000001)**2)
print((1 - cos(0.0000001))/(0.0000001)**2)
print(" ")
print("My guess was a little off")
