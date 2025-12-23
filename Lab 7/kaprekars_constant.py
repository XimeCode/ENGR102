# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Ximena Yepez
# Section: Section 548
# Assignment: LAB Topic 7
# Date: 28/10/2025
#

#make a loop to sort digits in ascending/descending order and substract until reaching 6174 or 0 
user_num = input("Enter a four-digit integer: ")
original_num = user_num

while not user_num.isdigit():
    user_num = input("Enter a four-digit integer: ")

num_value = int(user_num)
if num_value < 0 or num_value > 9999:
    print("Enter a four-digit integer: ")
    exit()

#add leading zeros for numbers with fewer than four digits
if len(user_num) < 4:
    user_num = '0' * (4 - len(user_num)) + user_num 

new_num = int(user_num)
sequence_of_nums = (f"{original_num}") #initialize string to track sequence of numbers to reach 6174
iterations = 0 

#apply kapreka's routine
while new_num != 6174 and new_num != 0:
    iterations += 1
    
    user_num = str(new_num)
    if len(user_num) < 4:
        user_num = '0' * (4 - len(user_num)) + user_num 

    list_num = list(user_num)

    #sort digits in ascending order
    list_num.sort()
    ascending = "".join(list_num)
    ascending_int = int(ascending)

    #sort digits in descending order
    descending = "".join(list_num[::-1]) 
    descending_int = int(descending)

    #substract the smaller number from larger number
    if descending_int > ascending_int:
            new_num = descending_int - ascending_int
    else:
            new_num = ascending_int - descending_int
    
    sequence_of_nums += (f" > {new_num}")

    if new_num == 0:
        break

print(sequence_of_nums)
if new_num == 0:
     print (f"{original_num} reaches {new_num} via Kaprekar's routine in {iterations} iterations")
else:
     print(f"{original_num} reaches {new_num} via Kaprekar's routine in {iterations} iterations")
     





