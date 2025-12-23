
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

def partc(list_nums):
    if len(list_nums) == 1:
        list_nums = list_nums[0]

    product = 0
    #list of nums [1, 2, 3]
    for i in range(len(list_nums) - 1):
        if 2029 == (list_nums[i] + list_nums[i+1]):

            for j in list_nums:
                product += j #sum numbers in list
            return product
        
    return False

print(partc(([1149, 5926, 1111, 2222, 3333, 918, 5555])))
