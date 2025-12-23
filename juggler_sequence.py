# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Ximena Yepez
# Section: Section 548
# Assignment: LAB Topic 6 
# Date: 15/10/ 2025
#


from math import *

n = int(input("Enter a positive integer: "))
while n <= 0:
    n = int(input("Enter a positive number please: "))

#initialize variables
count = 0
jugglers_sequence = str(n) 
current = n

#loop until 1 is reached
while current != 1:  
    if current % 2 == 0:
        current = floor(sqrt(current))
    else:
        current = floor(current ** 1.5)
    
    jugglers_sequence += ', ' + str(current)
    count += 1 #keep count of how may iterations it took to reach value 1 

print(f"The Juggler sequence starting at {n} is: ")
print(jugglers_sequence)
print(f"It took {count} iterations to reach 1")
