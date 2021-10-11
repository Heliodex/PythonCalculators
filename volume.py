# Heliodex 2020/11/19 calc
# Last edited 2021/08/20 calc
# I come back to fix this program and I see "2020/12/12" then i see the code

from math import pi
print("Calculates the volume of various 3D shapes")

# cylinder
def cyl(h, w):
  return str((pi*((w/2)**2))*h) 

# triangular prism
def tri(b, h, l):
  return str(((b*h)/2)*l)

# cone
def con(r, h): # defcon 5 lmao
  return str((pi*(r**2))*(h/3))

# square based pyramid
def pyr(w, h, l):
  return str((l*w)*(h/3))

while True:
  print("1 for cylinder, 2 for tri prism,")
  c = input("3 for cone, 4 for pyramid ")
  # i DESPISE this, when the string for
  # "input" is too long, it returns nil
  
  if (c == "1"):
    h =  float(input("Height? "))
    w =  float(input("Width? "))
    print("Volume, " + str(cyl(h, w)))
  
  elif (c == "2"):
    b =  float(input("Base length? "))
    h =  float(input("Height? "))
    l =  float(input("Length? "))
    print("Volume, " + str(tri(b, h, l)))
  
  elif (c == "3"):
    r = float(input("Base radius? "))
    h = float(input("Height? "))
    print("Volume, " + str(con(r, h)))
  
  elif (c == "4"):
    w = float(input("Width? "))
    h = float(input("Height? "))
    l = float(input("Length? "))
    print("Volume, " + str(pyr(w, h, l)))
  
  else:
    break