# Heliodex 2021/08/17
# Last edited 2021/12/01 -- new program style

from math import pi
print("Calculates the size/lenth of an arc")

while True:
  deg = float(input("Degrees? "))
  dia = float(input("Diameter? "))
  f = deg/360 
  print(" ")
  
  print("Arc 1:")
  print(f*(pi*dia))
  f = (360-deg)/360
  
  print("Arc 2:")
  print(f*(pi*dia))
  
  print("Circumference:")
  print(pi*dia)
  print(" ")
