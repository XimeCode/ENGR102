# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Ximena Yepez
# Section: Section 548
# Assignment: LAB Topic 7
# Date: 28/10/2025
#

#first 4 nums
#add leading zeros 

user_num = input("Enter a four-digit integer: ")

original_num = user_num


iterations = 0



for num in range[0:10000]:

    iterations += num
        
    user_num = str(num)
    if len(user_num) < 4:
        user_num = '0' * (4 - len(user_num)) + user_num 
    
    if len(set(user_num)) == 1:
        # return 0

    
        list_num = list(user_num)

    #ascending order
    list_num.sort()
    ascending = "".join(list_num)
    ascending_int = int(ascending)

    descending = "".join(list_num[::-1]) 
    descending_int = int(descending)

    if descending_int > ascending_int:
            new_num = descending_int - ascending_int
    else:
            new_num = ascending_int - descending_int
     
    sequence_of_nums += (f" > {new_num}")

    if new_num == 0:
         break









# print(sequence_of_nums)
# if new_num == 0:
#      print (f"{original_num} reaches {new_num} via Kaprekar's routine in {iterations} iterations")
# else:
#      print(f"{original_num} reaches {new_num} via Kaprekar's routine in {iterations} iterations")
     
