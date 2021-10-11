# Heliodex 2021/09/22
# Last edited 2021/09/22

print("Calculates segment depth from chord and circle")

while True:
  rad = float(input("Circle radius? "))
  chd = float(input("Chord length? "))
  
  print("Depth, " + str(rad-((rad**2)-((chd/2)**2))**0.5))