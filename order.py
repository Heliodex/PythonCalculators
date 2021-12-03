# Heliodex 2021/11/12
# Last edited 2021/12/03 -- new program style

print("Orders a comma-separated list of data")

while True:
  list = input("List? ")
  print(" ")
  if not(list):
    break
  
  list2 = list.split(",")
  list3 = str(sorted(list2))
  
  print("Ordered list:") 
  print(list3)
  print(" ")
# doesnt work with 1 and 2 digit numbers  
