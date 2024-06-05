# Heliodex 2021/10/07
# Last edited 2021/12/01 -- new program style

print("Finds internal angles of polygons")

while True:
    a = float(input("Number of sides? "))  # ...float?
    print(" ")
    print("Internal angle:")
    print((180 * (a - 2)) / a)
    print("Total internal angle:")
    print(180 * (a - 2))
    print(" ")
