
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
t3, t4, t5, t6, t7= (37.5, 40, 50, 60, 70)

#point 1 : 37.5 seconds
x3 = (slope * (t3 - t0))+x0
y3 = (slope_y1 * (t3 - t0))+y0
z3 = (slope_z1) * (t3 - t0)+z0

print ("At time 37.5 seconds:")
print ("x3 =", x3, "m")
print ("y3 =", y3, "m")
print ("z3=", z3, "m")
print ("-----------------------")

#point 2 : 40 seconds
x4 = (slope * (t4 - t0))+x0
y4 = (slope_y1 * (t4 - t0))+y0
z4 = (slope_z1) * (t4 - t0)+z0

print ("At time 40.0 seconds:")
print ("x4 =", x4, "m")
print ("y4 =", y4, "m")
print ("z4=", z4, "m")
print ("-----------------------")

#point 3 : 50 seconds
x5 = (slope * (t5 - t0))+x0
y5 = (slope_y1 * (t5 - t0))+y0
z5 = (slope_z1) * (t5 - t0)+z0

print ("At time 50.0 seconds:")
print ("x4 =", x5, "m")
print ("y4 =", y5, "m")
print ("z4=", z5, "m")
print ("-----------------------")

#point 4 : 60 seconds
x6 = (slope * (t6 - t0))+x0
y6 = (slope_y1 * (t6 - t0))+y0
z6 = (slope_z1) * (t6 - t0)+z0

print ("At time 60.0 seconds:")
print ("x4 =", x6, "m")
print ("y4 =", y6, "m")
print ("z4=", z6, "m")
print ("-----------------------")

#point 5 : 70 seconds
x7 = (slope * (t7 - t0))+x0
y7 = (slope_y1 * (t7 - t0))+y0
z7 = (slope_z1) * (t7 - t0)+z0

print ("At time 70.0 seconds:")
print ("x4 =", x7, "m")
print ("y4 =", y7, "m")
print ("z4=", z7, "m")
print ("-----------------------")



