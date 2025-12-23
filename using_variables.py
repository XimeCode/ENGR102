#By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do."
#  "I have not given or received any authorized aid on this assignment."
#
#Name:          Ximena Yepez
#Section:       ENGR 102, Section 548
#Assignment:    LAB: Topic 2 
#Date:          10/09/2025
#



#Calculate the reynolds number for a fluid
#Velocity 9 m/s, kinematic viscosity 0.0015 m^2/s, and characteristic linear dimension = 0.875 m
velocity = 9 # m/s
viscosity = 0.0015 # m^2/s 
dimension = 0.875 # m

print("Reynolds number is", velocity * dimension/ viscosity)

from math import *
import math
#calculate the wavelength of x-rays scattering from a crystal lattice 
#distance between crystal layers 0.029 nm, scattering angle 35 degrees

distance = 0.029 #nm
angle = 35 #degrees
print ("Wavelength is", 2 * distance * math.sin(math.radians(angle)), "nm")

#Calculate the production well after 10 days
#initial production rate 100 barrels/day, initial decline rate 2/day, and hyperbolic constant 0.8

days = 10 
production = 100 #barrels/day
decline = 2 #per day 
constant = 0.8 
print("Production rate is", production / ((1 + constant * decline * days) ** ( 1 /constant)), "barrels/day")


#Calculate change of velocity of a fighter jet
#initial mass 11000 kg, final mass = 8300 kg, exhaust velocity = 2029 m/s

initial = 11000 #kg
final = 8300 #kg
velocity = 2029 #m/s
print("Change of velocity is", velocity * math.log(initial / final), "m/s")