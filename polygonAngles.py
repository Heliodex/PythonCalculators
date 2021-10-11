# Heliodex 2021/10/07
# Last edited 2021/10/11
# im putting these on github! woo

print("Finds internal angles of polygons")

while True:
  a = float(input("Number of sides? ")) # ...float?
  intangle = 180*(a-2)/a
  intangles = intangle * a
  
  print("Internal angle, " + str(intangle))
  print("Total internal angle, " + str(intangles))
  