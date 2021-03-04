#ealmonte32
# We need to import the math library in order to use the math square root built in
import math

print("==================================================")
print("\nCompute and display the distance between two points (x1,y1) and (x2,y2).\n")

# we ask for integers for the x and y values for both points
print("Point 1")
x1 = int(input(" Enter value for x1: "))
y1 = int(input(" Enter value for y1: "))

print("\nPoint 2")
x2 = int(input(" Enter value for x2: "))
y2 = int(input(" Enter value for y2: "))

# To be more organized and clear with the complete formula, I write the inside part first
# then I take the square root of that inside part and this gives me the distance result
formula_inside = ((x2 - x1)**2 + (y2 - y1)**2)
distance = math.sqrt(formula_inside)

print("\nThe distance between the two points is:", distance)
