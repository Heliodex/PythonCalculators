# Heliodex 2020/11/13 calc
# Last edited 2021/08/19 calc

from math import pi
print("calculate diameter or area of circle")

while True:
  x = input("1 for diameter, 2 for area ")
  
  if (x == "1"):
    c = float(input("circumference? "))
    print("diameter, " + str(c/pi))
    
  elif (x == "2"):
    r = float(input("radius? "))
    print("area, " + str(pi*(r**2)))
  
  else:
    break
    # ok, 1 program per file next time