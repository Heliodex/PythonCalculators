# Heliodex 2022/11/04
# Last edited 2022/11/04

from math import floor

print("Calculates how boxes fit into a larger container")

while True:
    c = [
        float(input("Container length? ")),
        float(input("Container breadth? ")),
        float(input("Container height? ")),
    ]
    b = [
        float(input("Box length? ")),
        float(input("Box breadth? ")),
        float(input("Box height? ")),
    ]
    stack = floor(c[2] / b[2])
    lengthways = floor(c[0] / b[0]) * floor(c[1] / b[1]) * stack
    breadthways = floor(c[0] / b[1]) * floor(c[1] / b[0]) * stack

    print(lengthways)
    print(breadthways)
