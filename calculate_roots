# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Ximena Yepez
# Section: Section 548
# Assignment: Lab: Topic 4 activity #3
# Date: 23/09/2025
#

from math import *
roota = (float(input("Please enter the coefficient A:")))
rootb = (float(input("Please enter the coefficient B:")))
rootc= (float(input("Please enter the coefficient C:")))


#Use (b^2 - 4ac) to solve for roots
#Pos discriminant = two distinct real solutions, Zero discriminant = one real solution, neg discriminant = 2 completx solutions
if roota != 0:
    discriminant = (rootb ** 2) - 4 * roota * rootc

    if discriminant > 0:
        root1 = (-(rootb) + sqrt((rootb ** 2) - 4 * (roota)*(rootc)))/ (2 *(roota))
        root2 = (-(rootb) - sqrt((rootb ** 2) - 4 * (roota)*(rootc)))/ (2 *(roota))

        if root1 > root2:
               print (f"The roots are x = {root1} and x = {root2}")
        else:
               print (f"The roots are x = {root2} and x = {root1}")

    # one repeated root
    elif discriminant == 0: 
        oneroot = -rootb / (2 * roota)
        print(f"The root is x = {oneroot}")

    #imaginary numbers
    else:
         realnum = -rootb / (2 * roota)
         imaginary = sqrt(-discriminant) / (2 * roota)
         print(f"The roots are x = {realnum} + {imaginary}i and x = {realnum} - {imaginary}i")

#Solve x = -C/B in case of (A = 0, B does not equal 0)
elif rootb != 0:
     root = -rootc / rootb
     print(f"The root is x = {root}")
 
elif (roota == 0, rootb == 0, rootc > 0):
    print("You entered an invalid combination of coefficients!")



