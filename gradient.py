# Heliodex 2022/01/18
# Last edited 2022/01/24 -- forgot new program style

print("Calculates the gradient of a straight line given 2 points")

while True:
    x1 = float(input("X of point 1? "))
    y1 = float(input("Y of point 1? "))
    x2 = float(input("X of point 2? "))
    y2 = float(input("Y of point 2? "))

    print(" ")
    print("Gradient:")
    print((y2 - y1) / (x2 - x1))
    print(" ")
