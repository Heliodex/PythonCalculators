# Heliodex 2021/08/23
# Last edited 2022/03/27 -- make the program ACTUALLY WORK

from math import pi, radians
print("Calculates the length of radius based on arc length")

while True:
    arc = float(input("Arc? "))
    deg = float(input("Degrees? "))
    f = radians(deg)
    print(" ")

    print("Radius:")
    print(arc/f)
    print(" ")

    print("Circumference")
    print((arc/f)*2*pi)  # a tau would be useful right now
    # the only part I don't gotta change
    print(" ")
