# Heliodex 2020/11/19
# Last edited 2022/03/18 -- add sphere etc
# 2021/08/20 I come back to fix this program and I see "2020/12/12" then i see the code

from math import pi

print("Calculates the volume of various 3D shapes")


def cyl(h, w):
    return str((pi * ((w / 2) ** 2)) * h)


def tri(b, h, l):
    return str(((b * h) / 2) * l)


def con(r, h):  # defcon 5 lmao
    return str((pi * (r**2)) * (h / 3))


def pyr(w, h, l):
    return str((l * w) * (h / 3))


def sph(r):
    return str((pi * (r**3) * (4 / 3)))


while True:
    print(" ")
    print("1 for cylinder, 2 for tri prism,")
    print("3 for cone, 4 for pyramid, ")
    c = input("5 for sphere ")
    # i DESPISE this, when the string for
    # "input" is too long, it returns nil

    if c == "1":  # cylinder
        h = float(input("Height? "))
        w = float(input("Width? "))
        print(" ")
        print("Volume:")
        print(cyl(h, w))

    elif c == "2":  # triangular prism
        b = float(input("Base length? "))
        h = float(input("Height? "))
        l = float(input("Length? "))
        print(" ")
        print("Volume:")
        print(tri(b, h, l))

    elif c == "3":  # cone
        r = float(input("Base radius? "))
        h = float(input("Height? "))
        print(" ")
        print("Volume:")
        print(con(r, h))

    elif c == "4":  # squase based pyramid
        w = float(input("Width? "))
        h = float(input("Height? "))
        l = float(input("Length? "))
        print(" ")
        print("Volume:")
        print(pyr(w, h, l))

    elif c == "5":  # sphere
        r = float(input("Radius? "))
        print(" ")
        print(sph(r))

    else:
        break
