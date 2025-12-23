
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Ximena Yepez
# Melanie Barrientos
# Sophia Treviño
# Section: Section 548
# Assignment: Linear Interpolation Lab 3
# Date: 09/16/2025


#variables = time (1, 2), positions (x, y, z)
#Display the times using two (2) decimal places
#Display the positions using three (3) decimal places

time1= (float(input("Enter time 1: "))) 
x1 = (float(input("Enter the x position of the object at time 1:")))
y1 = (float(input ("Enter the y position of the object at time 1:")))
z1 = (float(input ("Enter the z position of the object at time 1:")))

time2 = (float(input ("Enter time 2: ")))
x2 = (float(input("Enter the x position of the object at time 2:")))
y2 = (float(input ("Enter the y position of the object at time 2:")))
z2 = (float(input ("Enter the z position of the object at time 2:")))


# (time0 - time1)/(time2 - time1)

slope_x = (x2 - x1) / (time2 - time1)
slope_y = (y2 - y1) / (time2 - time1)
slope_z = (z2 - z1) / (time2 - time1)

interval = (time2 - time1) / 4 

for i in range(5):
    current_time = time1 + i * interval
    x_current = x1 + slope_x * (current_time - time1)
    y_current = y1 + slope_y * (current_time - time1)
    z_current = z1 + slope_z * (current_time - time1)
    
    print(f"At time {current_time:.2f} seconds the object is at ({x_current:.3f}, {y_current:.3f}, {z_current:.3f})")



