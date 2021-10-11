# Heliodex 2021/08/18
# Last edited 2021/08/23

from math import pi # no more "import *"
print("Calculates area of a sector of a circle")

while True:
  deg = float(input("Degrees? "))
  rad = float(input("Radius? "))
  f = deg/360 
  
  print("Sector 1, " + str(f*(pi*(rad**2))))
  f = (360-deg)/360
  
  print("Sector 2, " + str(f*(pi*(rad**2))))
  
  print("Circumference, " + str(pi*(rad*2)))