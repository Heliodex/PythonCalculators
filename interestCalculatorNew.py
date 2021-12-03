# Heliodex 2021/08/24
# Last edited 2021/12/01 -- new program style
# edit of vatRemover
# uses Short Method, experimental

print("Calculates amount after adding a percentage a number of times")

while True:
  val = float(input("Current value? "))
  int = float(input("Interest %? "))
  times = float(input("Number of times? "))
  print(" ")
  
  print("Values:")
  for i in range(times+1):
    f = (((100 + int)/100) ** i) * val
    print(f)
    # i, not times    
    
  print("Total interest:")
  print(f - val)
  print(" ")
