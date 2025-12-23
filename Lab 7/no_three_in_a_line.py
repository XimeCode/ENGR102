# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Ximena Yepez
# Melanie Barrientos
# Sophia Treviño
# Section: Section 548
# Assignment: LAB Topic 10 (team)
# Date: 11/26/2025


def no_three_in_line(n):

    def collinear(p1, p2, p3):
        (x1, y1), (x2, y2), (x3, y3) = p1, p2, p3
        return x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2) == 0 #if area euqals 0, then the three points are collinear

    points = []
    
    #produce every integer grid point in row order
    potentials = [(x, y) for x in range(n) for y in range(n)]
    
    for potential in potentials: 
        valid = True
        #checks the candidate against all pairs of points currently in points
        for i in range(len(points)):
            if not valid:
                break
            for j in range(i + 1, len(points)):
                if collinear(points[i], points[j], potential): #if existing pair collinear, mark invalid
                    valid = False
                    break
        if valid:
            points.append(potential)
    
    return points

