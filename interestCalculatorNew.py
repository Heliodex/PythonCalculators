# Heliodex 2021/08/24 calc
# Last edited 2021/09/02 calc
# edit of vatRemover
# uses Short Method, experimental

print("Calculates amount after adding a percentage a number of times")

while True:
  val = float(input("Current value? "))
  int = float(input("Interest %? "))
  times = float(input("Number of times? "))
  
  print("Values, ")
  for i in range(times+1):
    f = (((100 + int)/100) ** i) * val
    print(f)
    # i, not times    
    
  print("Total interest, " + str(f - val))