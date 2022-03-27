# Heliodex 2020/11/03
# Last edited 2021/12/03 -- new program style

print("Calculates area and perimiter of a triangle")
# most useless program out of the bunch

while True:
    print(" ")
    c = input("1 for area, 2 for perimiter ")

    if (c == "1"):
        ph = float(input("Height? "))
        pb = float(input("Breadth? "))
        print(" ")
        print("Area:")
        print(ph*pb/2)

    elif (c == "2"):
        px = float(input("Side 1? "))
        py = float(input("Side 2? "))
        pz = float(input("Side 3? "))
        print(" ")
        print("Perimiter:")
        print(px+py+pz)

    else:
        break
