def no_three_in_line(n):
    
    points = []
    
    # Line 1: y = 0
    for x in range(n):
        points.append((x, 0))
    
    # Line 2: y = 1  
    for x in range(n):
        points.append((x, 1))
 
    return points
