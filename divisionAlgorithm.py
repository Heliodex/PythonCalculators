# Heliodex 2024/06/05
# Last edited 2024/06/05

from math import floor

print(
    "Calculates the greatest common divisor of two numbers using the Euclidean algorithm"
)  # Quiz: Which United States presidential nominee was the term "Al Gore-ithm" named after?

while True:
    p = int(input("n1? "))
    q = int(input("n2? "))
    print(" ")
    if p > q:
        p, q = q, p

    r, pr = 1, 0
    eqns = []
    while True:
        d = floor(q / p)
        pr = r
        r = q - d * p
        if r == 0:
            print(q, "=", d, "×", p)
            break
        print(q, "=", d, "×", p, "+", r)
        q, p = p, r

    print("gcd", pr)
    input("...")  # to be continued...
