# Heliodex <2021/08/18
# Last edited 2021/12/01 -- new program style

print("Calculates whether a triangle is a right-angled triangle ")

while True:
    a = input("Side 1? ")
    b = input("Side 2? ")
    c = input("Hypoteneuse? ")
    a = float(a)
    b = float(b)
    c = float(c)
    print(" ")

    if ((a**2) + (b**2)) == (c**2):
        print("Right-angled")
    else:
        print("Not right-angled")

    print(a**2)
    print(b**2)
    print((a**2) + (b**2))
    print(c**2)
    print(" ")  # "new program style" didn't do much...
