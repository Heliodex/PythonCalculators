# Heliodex 2021/08/18
# Last edited 2021/11/30 -- new program style

from math import pi # no more "import *"
print("Calculates area of a sector of a circle")

while True:
  deg = float(input("Degrees? "))
  rad = float(input("Radius? "))
  print(" ")
  f = deg/360
  
  # 2021/11/30 new program style,
  # makes it easier to select and see results
  
  print("Sector 1:")
  print(f*(pi*(rad**2)))
  f = (360-deg)/360
  
  print("Sector 2:")
  print(f*(pi*(rad**2)))
  
  print("Total area:")
  print(pi*(rad**2))
  print(" ")
