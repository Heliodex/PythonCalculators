# Heliodex 2020/11/13
# Last edited 2021/12/01 -- new program style

from math import pi

print("Calculates diameter or area of circle")

while True:
    x = input("1 for diameter, 2 for area ")

    if x == "1":
        c = float(input("Circumference? "))
        print("Diameter:")
        print(c / pi)
        print(" ")

    elif x == "2":
        r = float(input("Radius? "))
        print("Area:")
        print(pi * (r**2))
        print(" ")

    else:
        break
        # okay, 1 program per file next time
