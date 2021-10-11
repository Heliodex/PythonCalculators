# Heliodex 2021/08/24 calc
# Last edited 2021/08/25 calc
# edit of vatRemover

print("Calculates amount after adding a percentage a number of times")

while True:
  val = float(input("Current value? "))
  int = float(input("Interest %? "))
  times = float(input("Number of times? "))
  
  b = val
  print("Values, ")
  for i in range(times+1):
    print(b)
    b = b * (1 + int/100)
  