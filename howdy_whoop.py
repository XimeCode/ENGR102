# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Ximena Yepez
# Section: Section 548
# Assignment: LAB Topic 6 
# Date: 15/10/2025
#


first_int = int(input("Enter an integer: "))
second_int =  int(input("Enter another integer: "))

#output nums 1 to 100 unless
#condition0 = num is evenly divisile by one or both of the integers entered by user
#condition1 = i%first_int == 0 , we print howdy
#condition2 = i%second_int == 0 , we print Whoop

#check for positive numbers in input 
if first_int <= 0 or second_int <= 0:
    print("Please enter positive integers only.")
    first_int = int(input("Enter an integer: "))
    second_int =  int(input("Enter another integer: "))
else:
    for i in range(1, 101):
        if i%first_int == 0 and i%second_int == 0:
            print("Howdy Whoop")
        elif i%first_int == 0:
            print ("Howdy")
        elif i%second_int == 0: 
            print ("Whoop")
        else:
            print(i)


        