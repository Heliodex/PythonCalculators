# Heliodex 2021/08/19 calc
# Last edited 2021/08/23 calc

from math import pi
print("Calculates angle of a sector from arc+radius")

while True:
  c = input("1 for with arc, 2 for with area ")
  
  if (c == "1"):
    arc = float(input("Arc? "))
    rad = float(input("Radius? "))
    
    print("Angle, " + str((arc/((rad*2)*pi))*360))
    print("Circumference, " + str(pi*(rad*2)))
  
  if (c == "2"):
    area = float(input("Area? "))
    rad = float(input("Radius? "))
    
    print("Angle, " + str((area/(pi*(rad**2)))*360))
    print("Circumference, " + str(pi*(rad*2)))
  
  else:
    break
# randomly exits sometimes, idk why    