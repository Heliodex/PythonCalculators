# Heliodex 2023/08/31
# Last edited 2023/09/01

from math import floor, log10, sqrt

print(
    "Solves SUVAT equations: displacement, initial & final velocity, acceleration, time"
)


def r(x: float):
    if x == 0:
        return "0"
    r = round(x, -int(floor(log10(abs(x)))) + 2)
    # diff = r/10000
    # if r > int(r) - diff and r < int(r) + diff:
    if r == int(r):
        r = int(r)
    return str(r)


def done(*args):
    for i in args:
        if i == None or i == "n":
            return False
    return True


while True:
    suvat = [
        input("s? "),
        input("u? "),
        input("v? "),
        input("a? "),
        input("t? "),
    ]

    count = 0
    for i in range(len(suvat)):
        if suvat[i] == "":
            suvat[i] = None
        elif suvat[i] != "n":
            # else:
            count += 1
            suvat[i] = float(suvat[i])

    if count < 3:
        print("Not enough information.")
        break

    s, u, v, a, t = suvat
    print(" ")

    for i in range(3):
        if s == None and s != "n":
            if done(u, v, t):  # desirable
                s = (v + u) / 2 * t
                print("s = t(u + v)/2")
                print("s = " + r(t) + "(" + r(v) + " + " + r(u) + ")/2")
            elif done(u, a, t):  # desirable
                s = u * t + 0.5 * a * t**2
                print("s = ut + ½at²")
                print("s = " + r(u) + "×" + r(t) + " + ½" + r(a) + "×" + r(t) + "²")
            elif done(u, v, a) and i > 1:  # undesirable
                s = (u**2 + v**2) / (2 * a)
                print("v² = u² + 2as")
                print("s = (u² + v²)/(2a)")
                print("s = (" + r(u) + "² + " + r(v) + "²)/(2×" + r(a) + ")")

            if s:
                print("s =", r(s) + "m")
                input("...")

        if v == None and v != "n":
            if done(s, u, t) and i > 1:  # undesirable
                v = 2 * s / t - u
                print("s = (u + v)/2*t")
                print("v = 2s/t - u")
                print("v = 2×" + r(s) + "/" + r(t) + " - " + r(u))
            elif done(u, a, t):  # desirable
                v = u + a * t
                print("v = u + at")
                print("v = " + r(u) + " + " + r(a) + "×" + r(t))
            elif done(s, u, a) and i > 1:  # undesirable
                v = sqrt(u**2 + 2 * a * s)
                print("v² = u² + 2as")
                print("v = √(u² + 2as)")
                print("v = √(" + r(u) + "² + 2×" + r(a) + "×" + r(s) + ")")

            if v:
                print("v =", r(v) + "ms⁻¹")
                input("...")

        if u == None and u != "n":
            if done(s, u, a):  # undesirable
                u = sqrt(v**2 - 2 * a * s)
                print("v² = u² + 2as")
                print("u = √(v² - 2as)")
                print("u = √(" + r(v) + "² - 2×" + r(a) + "×" + r(s) + ")")
            elif done(v, a, t):  # undesirable
                u = v - a * t
                print("v = u + at")
                print("u = v - at")
                print("u = " + r(v) + " - " + r(a) + "×" + r(t))
            elif done(s, v, t):  # undesirable
                u = 2 * s / t - v
                print("s = (u + v)/2*t")
                print("u = 2s/t - v")
                print("u = 2×" + r(s) + "/" + r(t) + " - " + r(v))
            elif done(s, v, a):  # undesirable
                u = sqrt(v**2 - 2 * a * s)
                print("v² = u² + 2as")
                print("u = √(v² - 2as)")
                print("u = √(" + r(v) + "² - 2×" + r(a) + "×" + r(s) + ")")
            elif done(s, a, t):  # undesirable
                u = (2 * s - a * t**2) / (2 * t)
                print("s = ut + ½at²")
                print("u = (2s - at²)/(2t)")
                print(
                    "u = (2×" + r(s) + " - " + r(a) + "×" + r(t) + "²)/(2×" + r(t) + ")"
                )

            if u:
                print("u =", r(u) + "ms⁻¹")
                input("...")

        if a == None and a != "n":
            if done(s, u, t):  # undesirable
                a = 2 * (s - u * t) / t**2
                print("s = ut + ½at²")
                print("a = 2(s - ut)/t²")
                print("a = 2(" + r(s) + " - " + r(u) + "×" + r(t) + ")/" + r(t) + "²")
            elif done(u, v, t):  # undesirable
                a = (v - u) / t
                print("v = u + at")
                print("a = (v - u)/t")
                print("a = (" + r(v) + " - " + r(u) + ")/" + r(t))
            elif done(s, u, v):  # undesirable
                a = (v**2 - u**2) / (2 * s)
                print("v² = u² + 2as")
                print("a = (v² - u²)/(2s)")
                print("a = (" + r(v) + "² - " + r(u) + "²)/(2×" + r(s) + ")")
            elif done(s, v, t) and i > 2:  # i give up
                raise "f*ck you"

            if a:
                print("a =", r(a) + "ms⁻²")
                input("...")

        if t == None and t != "n":
            if done(s, u, a):  # undesirable
                t = (sqrt(2 * a * s + u**2) - u) / a
                print("s = ut + ½at²")
                print("t = (√(2as + u²) - u)/a")
                print(
                    "t = (√(2×"
                    + r(a)
                    + "×"
                    + r(s)
                    + " + "
                    + r(u)
                    + "²) - "
                    + r(u)
                    + ")/"
                    + r(a)
                )
            elif done(u, v, a):  # undesirable
                t = (v - u) / a
                print("v = u + at")
                print("t = (v - u)/a")
                print("t = (" + r(v) + " - " + r(u) + ")/" + r(a))
            elif done(s, u, v):  # undesirable?
                t = 2 * s / (u + v)
                print("s = (u + v)/2*t")
                print("t = 2s/(u + v)")
                print("t = 2×" + r(s) + "/(" + r(u) + " + " + r(v) + ")")
            elif done(s, v, a) and i > 2:  # i give up
                raise "you're on your own"

            if t:
                print("t =", r(t) + "s")
                input("...")

        if done(s, u, v, a, t):
            break
