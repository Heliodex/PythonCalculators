# Heliodex 2021/08/17 calc
# Last edited 2021/08/21 calc

from math import pi
print("Calculates the size/lenth of an arc")

while True:
  deg = float(input("Degrees? "))
  dia = float(input("Diameter? "))
  f = deg/360 
  
  print("Arc 1, " + str(f*(pi*dia)))
  f = (360-deg)/360
  
  print("Arc 2, " + str(f*(pi*dia)))
  
  print("Circumference, " + str(pi*dia))