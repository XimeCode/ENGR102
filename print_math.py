#By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do."
#  "I have not given or received any authorized aid on this assignment."
#
#Name:          Ximena Yepez
#Section:       ENGR 102, Section 548
#Assignment:    LAB: Topic 1
#Date:          02/09/2025
#


#Calculate the reynolds number for a fluid
#Velocity = 9 m/s, kinematic viscosity = 0.0015 m^2/s, characteristic linear dimension = 0.875 m
print("Reynolds number is", 9 * 0.875 / 0.0015)

from math import *
import math
#calculate the wavelength of x-rays scattering from a crystal lattice 
#distance between crystal layers = 0.029 nm, scattering angle = 35 degrees
print ("Wavelength is", 2 * 0.029 * math.sin(math.radians(35)), "nm")

#Calculate the production well after 10 days
#initial production rate = 100 barrels/day, initial decline rate = 2/day, hyperbolic constant = 0.8
print("Production rate is", 100 / ((1 + 0.8 * 2 * 10) ** ( 1 /0.8)), "barrels/day")


#Calculate change of velocity of a fighter jet
#initial mass = 11000 kg, final mass = 8300 kg, exhaust velocity = 2029 m/s
print("Change of velocity is", 2029 * math.log(11000 / 8300), "m/s")