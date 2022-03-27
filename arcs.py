# Heliodex 2021/08/17
# Last edited 2022/03/27 -- allow using radius too

from math import pi
print("Calculates the size/lenth of an arc")

while True:
    deg = float(input("Degrees? "))
    dia = float(input("Diameter? ") or float(
        input("Radius? "))*2)  # best i could come up with
    f = deg/360
    print(" ")

    print("Arc 1:")
    print(f*(pi*dia))
    f = (360-deg)/360

    print("Arc 2:")
    print(f*(pi*dia))

    print("Circumference:")
    print(pi*dia)
    print(" ")
