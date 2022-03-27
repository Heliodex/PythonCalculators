# Heliodex 2021/12/01
# Last edited 2021/12/02
# This is gonna be a long one.

from math import pi, sin, cos, radians

print("Calculates the area of a segment from angle and radius")

while True:
    rad = float(input("Radius? "))
    deg = float(input("Angle degrees? "))
    print(" ")

    adj = cos(radians(deg/2)) * rad  # trigonometry!!  aaa
    opp = sin(radians(deg/2)) * rad  # radians is correct. took too long

    print("Adjacent:")
    print(adj)
    print("Opposite:")
    print(opp)
    print("Chord:")
    print(opp * 2)
    print(" ")

    # isosceles triangle with chord as base, A = (1/2)*B*H
    triArea = (adj * opp)
    # no need to /2 , as we would double it anyway
    print("Triangle area:")
    print(triArea)

    # Basically copied from sector.tns
    sectArea = (deg/360)*(pi*(rad**2))
    print("Sector area:")
    print(sectArea)

    print("Segment area:")
    print(sectArea - triArea)  # its finally done
    print(" ")
