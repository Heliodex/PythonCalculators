# Heliodex 2022/03/31
# Last edited 2022/03/31

print("Calculates a minimum and maximum value based on a percentage tolerance")

while True:
	print(" ")
	val = float(input("Value? "))
	tol = float(input("Tolerance %? "))

	print("Min value:")
	print(val * (1 - tol / 100))
	print("Max value:")
	print(val * (1 + tol / 100))
