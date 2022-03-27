# Heliodex 2021/08/24
# Last edited 2022/02/16 -- count number of steps and add reverse mode
# edit of vatRemover
# uses Short Method

print("Calculates amount after adding a percentage a number of times")

while True:
    c = input("1 for normal, 2 for reverse, 3 for catchup ")
    if c == "1":
        val = float(input("Current value? "))
        int = float(input("Interest %? "))
        times = float(input("Number of times? "))
        print(" ")

        print("Values:")
        for i in range(times+1):
            f = (((100 + int)/100) ** i) * val
            print(str(i) + ": " + str(f))  # funny c
            # i, not times

        print("Total interest:")
        print(f - val)
        print(" ")

    elif c == "2":
        val1 = float(input("Current value? "))
        val2 = float(input("Ending value? "))
        int = float(input("Interest %? "))
        print(" ")

        decrease = False
        if val1 > val2:
            if int >= 0:
                print("Will never reach end value")
                continue
            decrease = True
        elif int <= 0:
            print("Will never reach end value")
            continue

        print("Values:")
        i = 0
        while True:
            f = (((100 + int)/100) ** i) * val1
            print(str(i) + ": " + str(f))
            # i, not times
            if f < val2 and decrease or f > val2 and not decrease:
                break

            i += 1

        print("Total times taken:")
        print(i)
        print(" ")
    elif c == "3":
        val1 = float(input("First value? "))
        int1 = float(input("First interest %? "))
        val2 = float(input("Second value? "))
        int2 = float(input("Second interest %? "))
        print(" ")

        if int1 == int2:
            print("Interest is equal")
            continue
        elif val1 > val2:
            int1, int2 = int2, int1  # swap 2 vars
            val1, val2 = val2, val1

        print("Values:")
        i = 0  # idk how infinite for loops python
        while True:
            f1 = (((100 + int1)/100) ** i) * val1
            f2 = (((100 + int2)/100) ** i) * val2

            print(str(i) + ": " + str(f1) + ", " + str(f2))
            # i, not times

            if f1 > f2:
                break
            i += 1

        print("Time taken to catchup:")
        print(i)
        print(" ")

    else:
        break
