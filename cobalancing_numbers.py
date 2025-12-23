# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Ximena Yepez
# Section: Section 548
# Assignment: LAB Topic 6 
# Date: 15/10/2025
#


#n is cobalancing if sum of nums from 1 to n is equal to sum of nums (n + 1 to (n + r ))
#r is pos

n = int(input("Enter a value for n: "))
while n < 1:
    n = int(input("Enter a value for n: "))

cobalancing = ''
sum1 = 0

for i in range(1, n + 1):
    sum1 += i

#r is iterations until sum1 == sum2
r = 0 
sum2 = 0
next_num = n + 1 

while sum2 < sum1:
    sum2 += next_num
    next_num += 1
    r += 1 

#Check if equal
if sum2 == sum1:
    print(f"{n} is a co-balancing number with r={r}")
else:
    print(f"{n} is not a co-balancing number")
