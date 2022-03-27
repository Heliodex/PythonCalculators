# Heliodex 2021/08/19
# Last edited 2021/12/01 -- new program style

from math import pi
print("Calculates angle of a sector from arc+radius")

while True:
    c = input("1 for with arc, 2 for with area ")

    if (c == "1"):
        arc = float(input("Arc? "))
        rad = float(input("Radius? "))
        print(" ")

        print("Angle:")
        print((arc/((rad*2)*pi))*360)

        print("Circumference:")
        print(pi*(rad*2))
        print(" ")

    elif (c == "2"):  # ah yes. classic "ellif"
        area = float(input("Area? "))
        rad = float(input("Radius? "))
        print(" ")

        print("Angle:")
        print((area/(pi*(rad**2)))*360)

        print("Circumference:")
        print(pi*(rad*2))
        print(" ")

    else:
        break
