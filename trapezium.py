# Heliodex 2020/11/04 calc
# Last edited 2021/08/20 calc

print("Calculates the area of trapezium")

while True:
  s1 = float(input("side 1? "))
  s2 = float(input("side 2? "))
  h = float(input("height? "))
  
  print("area, " + str((s1 + s2) / 2 * h))