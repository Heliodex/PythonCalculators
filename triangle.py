# Heliodex 2020/11/03 calc
# Last edited 2021/08/20 calc

print("Calculates area and perimiter of a triangle")

while True:
  c = input("1 for area, 2 for perimiter ")
  if (c == "1"):
    ph = float(input("height? "))
    pb = float(input("breadth? "))
    print("area, " + str(ph*pb/2))
    
  elif (c == "2"):
    px = float(input("side 1? "))
    py = float(input("side 2? "))
    pz = float(input("side 3? "))
    print("perimiter, " + str(px+py+pz))
  else:
    break