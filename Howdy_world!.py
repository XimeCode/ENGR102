
#By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do."
#  "I have not given or received any authorized aid on this assignment."
#
#Name:          Ximena Yepez
#Section:       ENGR 102, Section 548
#Assignment:    LAB: Topic 2
#Date:          10/09/2025
#

#two observed 3D positions at two points in time

t0= 12 # seconds
x0 = 8
y0 = 6
z0 = 7

t2= 85 #seconds
x2 = -5
y2 = 30
z2 = 9

# Step 1: linearly interpolate between (t0, x0) and (t2, x2)
# for t1 with x1 as the result

#solve for slope 
#then calculate y = (slope)(x - x1)+y1

t1= 30 #seconds

slope = ((-5)-8)/(85-12)
x1= (slope * (t1 - t0))+x0

# Step 2: repeat for (t0, y0) and (t2, y2) for t1 with y1 as the result

slope_y1 = (30-6)/(85-12)
y1= (slope_y1 * (t1 - t0))+y0

# Step 3: repeat for (t0, z0) and (t2, z2) for t1 with z1 as the result.

slope_z1 = (9-7)/(85-12)
z1 = (slope_z1) * (t1 - t0)+z0

print ("At time 30.0 seconds:")
print ("x1 =", x1, "m")
print ("y1 =", y1, "m")
print ("z1 =", z1, "m")
print ("-----------------------")


# Calculate at 5 points
t3, t4, t5, t6, t7= (20, 40, 50, 60, 70)


x3 = (slope * (t3 - t0))+x0
y3 = (slope_y1 * (t3 - t0))+y0
z3 = (slope_z1) * (t3 - t0)+z0

print ("At time 20.0 seconds:")
print ("x3 =", x3, "m")
print ("y3 =", y3, "m")
print ("z3=", z3, "m")
print ("-----------------------")