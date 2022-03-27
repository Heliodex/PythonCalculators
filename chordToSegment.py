# Heliodex 2021/09/22
# Last edited 2021/12/03 -- calculate second depth

print("Calculates segment depth from chord and circle")

while True:
    rad = float(input("Circle radius? "))
    chd = float(input("Chord length? "))

    segmDepth = rad-((rad**2)-((chd/2)**2))**0.5
    # Least optimal equation ever
    print(" ")

    print("Depth 1:")
    print(segmDepth)
    print("Depth 2:")
    print((rad*2)-segmDepth)
    print(" ")
