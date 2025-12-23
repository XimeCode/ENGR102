# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Ximena Yepez
# Section: Section 548
# Assignment: LAB Topic 7
# Date: 28/10/2025
#

numbers = (input("Enter numbers: "))

#split input string into list and convert each element into integer
list_nums = [int(x) for x in numbers.split()]

num_len = len(list_nums)

#initialize varibales for sum and split
left_sum = 0
right_sum = 0
total_sum = 0
split = False #track if split is found

#calculate total sum of all numbers 
for i in range(num_len):
    total_sum += list_nums[i]

#initialize lists to track left numbers and right numbers
left_nums = []
right_nums = []

#find split point where left sum equals right sum
for i in range(num_len):
    left_sum += list_nums[i] 
    left_nums.append(list_nums[i])
    right_sum = total_sum - left_sum # calculate right sum 

    #check for balanced split
    if right_sum == left_sum: 
        right_nums = (list_nums[i+1: ]) #remaining numbers go to right side 
        split = True 
        break
        
if split:
    print(f"Left: {left_nums}")
    print(f"Right: {right_nums}")
    print(f"Both sum to {left_sum}")
else:
    print("Cannot split evenly")
        

