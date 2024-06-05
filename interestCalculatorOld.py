# Heliodex 2021/08/24
# Last edited 2021/12/01 -- new program style
# edit of vatRemover

print("Calculates amount after adding a percentage a number of times")

while True:
    val = float(input("Current value? "))
    int = float(input("Interest %? "))
    times = float(input("Number of times? "))
    print(" ")

    b = val
    print("Values:")
    for i in range(times + 1):
        print(b)
        b = b * (1 + int / 100)

    print(" ")  # Line 24, converseOfPythagoras.tns
