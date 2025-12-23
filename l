#By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do."
#  "I have not given or received any authorized aid on this assignment."
#
#Name:          
#Section:       
#Assignment:    
#Date:          10/09/2025
#

t0= 12
x0 = 8
y0 = 6
z0 = 7

t2= 85 
x2 = -5
y2 = 30
z2 = 9

#use formula for interpolation

t1= 30 

slope = ((-5)-8)/(85-12)
x1= (slope * (t1 - t0))+x0

slope_y1 = (30-6)/(85-12)
y1= (slope_y1 * (t1 - t0))+y0

slope_z1 = (9-7)/(85-12)
z1 = (slope_z1) * (t1 - t0)+z0

print ("At time 30.0 seconds:")
print ("x1 =", x1, "m")
print ("y1 =", y1, "m")
print ("z1 =", z1, "m")
print ("-----------------------")

t3 = 37.5
t4 = 38
t5 = 39
t6 = 40
t7 = 411

= (37.5, 38, 39, 40, 41)

x3 = (slope * (t3 - t0))+x0
y3 = (slope_y1 * (t3 - t0))+y0
z3 = (slope_z1) * (t3 - t0)+z0

x4 = (slope * (t4 - t0))+x0
y4 = (slope_y1 * (t4 - t0))+y0
z4 = (slope_z1) * (t4 - t0)+z0

x5 = (slope * (t5 - t0))+x0
y5 = (slope_y1 * (t5 - t0))+y0
z5 = (slope_z1) * (t5 - t0)+z0

x6 = (slope * (t6 - t0))+x0
y6 = (slope_y1 * (t6 - t0))+y0
z6 = (slope_z1) * (t6 - t0)+z0

x7 = (slope * (t7 - t0))+x0
y7 = (slope_y1 * (t7 - t0))+y0
z7 = (slope_z1) * (t7 - t0)+z0

print ("At time 37.5 seconds:")
print ("x3 =", x3, "m")
print ("y3 =", y3, "m")
print ("z3=", z3, "m")
print ("-----------------------")

print ("At time 38 seconds:")
print ("x4 =", x4, "m")
print ("y4 =", y4, "m")
print ("z4=", z4, "m")
print ("-----------------------")

print ("At time 39 seconds:")
print ("x4 =", x5, "m")
print ("y4 =", y5, "m")
print ("z4=", z5, "m")
print ("-----------------------")

print ("At time 40 seconds:")
print ("x4 =", x6, "m")
print ("y4 =", y6, "m")
print ("z4=", z6, "m")
print ("-----------------------")

print ("At time 41 seconds:")
print ("x4 =", x7, "m")
print ("y4 =", y7, "m")
print ("z4=", z7, "m")
print ("-----------------------")

