# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Ximena Yepez
# Section: ENGR 102, Section 548
# Assignment: LAB: Topic 5 (individual)
# Date: 08/10/2025

from math import *

#Ask user for excess temperature 
temp = float(input("Enter the excess temperature: "))

# Define the five points on the boiling curve
# Point A: onset of free convection
x0 = 1.3 
y0 = 1000
# Point B: onset of nucleate boiling
x1 = 5
y1 = 7000
# Point C: critical heat flux
x2 = 30
y2 = 1.5 * 10 ** 6 
# Point D: Leidenfrost point
x3 = 120
y3 = 2.5 * 10 ** 4 
# Point E: end of film boiling region
x4 = 1200
y4 = 1.5 * 10 ** 6

#Check which region the temperature falls in and calculate surface heat flux
#calculate logarithmic interpolation: y = y0 * (x/x0)^m , Calculate slope using m = log(y1/y0) / log(x1/x0)

if 1.3 <= temp <= 5:  #A-B: Free convection
    m = log(y1/y0) / log(x1/x0)
    y = y0 * (temp / x0) ** m 
    print(f"The surface heat flux is approximately {y:.0f} W/m^2")

elif 5 < temp <= 30:  #B-C: Nucleate boiling
    m = log(y2/y1) / log(x2/x1)
    y = y1 * (temp / x1) ** m 
    print(f"The surface heat flux is approximately {y:.0f} W/m^2")

elif 30 < temp <= 120:  #C-D: Transition boiling
    m = log(y3/y2) / log(x3/x2)
    y = y2 * (temp / x2) ** m 
    print(f"The surface heat flux is approximately {y:.0f} W/m^2")

elif 120 < temp <= 1200:  #D-E: Film boiling
    m = log(y4/y3) / log(x4/x3)
    y = y3 * (temp / x3) ** m 
    print(f"The surface heat flux is approximately {y:.0f} W/m^2")

else: #less than A (below 1.3°C) or More than E (above 1200°C) = Surface heat flux is not available 
    print("Surface heat flux is not available")