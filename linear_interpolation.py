# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Ximena Yepez
# Melanie Barrientos
# Sophia Treviño
# Section: Section 548
# Assignment: Linear Interpolation Lab 2 
# Date: 06/06/2025

#Part #1:

x1 = 10
y1 = 2029
x2 = 55
y2 = 23029
x0=25

#speed/slope
slope = float((y2 - y1) / (x2 - x1))

#Set two expressions for the slope equal to each other
#Calculate position using linear interpolation y = (slope)(x-x1)+y1 whem time = 25
position = ((slope) * (x0 - x1)) + y1

#print time and position with a line describing what is being output
print ("Part 1:")
print ("For t = 25 minutes, the position p =", position ,"kilometers")
print()



#PART #2:

# distance from houston 
# every time ISS passes houston distance is reset to zero

import math 

#caculate the total distance around the circle the ISS travels 
#Making it not surpass the radius but to go around as if starting over after getting to the position 6745
time = 300
radius = 6745
circumference = 2 * math.pi * 6745

#calculate a distance greater than the orbit's circumference.
y = (float((slope) * (time - x1)) + y1)

#Calculate position with respect to houston 
distance = y % circumference

print("Part 2:")
print("For t = 300 minutes, the position p =", awnser,"kilometers")
