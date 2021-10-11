# Heliodex 2021/08/23 calc
# Last edited 2021/08/23 calc

from math import pi
print("Calculates the length of radius based on arc length")

while True:
  arc = float(input("Arc? "))
  deg = float(input("Degrees? "))
  f = deg/360 
  
  print("Arc 1, " + str(f*(pi*dia)))
  f = (360-deg)/360
  
  print("Arc 2, " + str(f*(pi*dia)))
  
  print("Circumference, " + str(pi*dia))
  # the only part I don't gotta change
  