
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Ximena Yepez
# Section: Section 548
# Assignment: LAB 9 (individual)
# Date: 19/11/25
#

def parta(list):

    mini = min(list)
    print(mini)
    
    list_sorted = sorted(list)
    list_length = len(list_sorted)

    if ((list_length % 2) == 1): # odd length
        median_value = list_sorted[list_length  // 2]
  
    else: # even length
        mid1 = list_sorted[list_length // 2 - 1]  
        mid2 =  list_sorted[list_length  // 2]     
        median_value = (mid1 + mid2) / 2
  
    maximum = max(list)
    print(maximum)

    return mini, median_value, maximum

def partb(times, distances_traveled):
    #ex ( times : [2, 3, 3] )( distances :[30, 30,30])

    #new list with velocity between consecutive time measurements
    #velocity = displacement / time 
    # (position2 - position1) / (time2 - time1)

    velocities = []

        #calculating average velocity
    for i in range(len(times)- 1):
        # x1 and x2 is positions t1 and t1 time
        change_time = times[i+1] - times[i]
        change_distance = distances_traveled[i+1] - distances_traveled[i]
        velocity = (change_distance / change_time)
        velocities.append(velocity)
    
    return velocities

def partc(list):
    for i in range(len(list)):
         for j in range(i + 1, len(list)):

            if (list[i] + list[j]) == 2029:
                return list[i] * list[j] #product of two numbers
        
    return False

def partd(n):
    #check if two can be calculated as the sum of 2 or more consecutive positive 

    for i in range(2, n, 2):
        sum = 0
        even_nums = []
        current_number = i

        while sum < n: #append consecutive even, positive numbers
            even_nums.append(current_number)
            sum += current_number

            if sum == n and len(even_nums) >= 2: # confirm there is two numbers and they equal to n
                return even_nums
            if sum > n:
                break

            current_number += 2

    return False

def parte(r_sphere, r_hole):
    import math # V = (π/6) * H³
    h = 2 * math.sqrt(r_sphere**2 - r_hole**2)
    bead = (math.pi * h**3) / 6
    return bead
  

def partf(character, name, company, email):

    entries = [name, company, email]
    longest = max(len(entry) for entry in entries)
    width = longest + 4 + 2

    border = ""
    for i in range(width):
        border = border + character
    
    #create each line with centered text and padding
    lines = []
    for entry in entries:
        padded_line = f"{entry:^{width - 2}}"
        lines.append(f"{character}{padded_line}{character}")

    business_card = f"{border}\n" + "\n".join(lines) + f"\n{border}"
    
    
    return business_card

def partg(x, tolerance):
    total = 0
    n = 1
    
    while True:
        #calculate (2/(2n-1)) * x^(2n-1)
        numerator = 2
        denominator = 2 * n - 1
        term = (numerator / denominator) * (x ** (2 * n - 1))
        
        if abs(term) < tolerance:
            break

        total += term
        n += 1
    
    return total

