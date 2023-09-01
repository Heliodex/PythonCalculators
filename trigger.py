# Heliodex 2022/01/13
# Last edited 2022/01/21

# Likely my biggest ever calculator program. Almost FOUR KILOBYTES!!!

# Prior warning: I was trying to program this to put on my calculator for the maths test on Friday 2022/01/21.
# It is all hastily hacked together, pretty unsafe, and accuracy of calculations is not guaranteed.

# My first attempt at the program took a week to write, and was much more difficult to write and test. This one took me about a day. Learned a lot about trig tho.
# Rewrite was inspired by https://brownmath.com/ti83/triangle.htm for the TI-83, makes it a lot easier to test the program. 

from math import *

print("Trigger: The ultimate trigonometry program")
print("Version 2.0.0")
print("Calculates all properties of a triangle, given the first three")
print(" ")

while True:
	sides = [None, None, None] # A, B, C
	angles = [None, None, None] # Opposite A, B, C
	# NoneType is way easier to debug than "tRiED tO COmpArE StriNG wITh INt"

	print("1 for SSS") # Side Side Side
	print("2 for SSA") #  Side Side Angle
	print("3 for SAS") # Side Angle Side
	print("4 for AAS") # Angle Angle Side
	print("5 for ASA") # Angle Side Angle
	c = input(" ")

	if c == "1": # SSS
		sides[0] = float(input("Side A? "))
		sides[1] = float(input("Side B? "))
		sides[2] = float(input("Side C? "))

		semiSum = (sides[0] + sides[1] + sides[2]) / 2

		if sides[0] > semiSum or sides[1] > semiSum or sides[2] > semiSum:
			print(" ")
			print("Triangle is invalid.")
			print(" ")
			continue

		elif sides[0] == semiSum or sides[1] == semiSum or sides[2] == semiSum:
			print(" ")
			print("Triangle has 0 area.")
			print(" ")
			continue

		area = sqrt(semiSum * (semiSum - sides[0]) * (semiSum - sides[1]) * (semiSum - sides[2])) # Apparently Heron's Formula, thanks GitHub Copilot
		circleRadius = (sides[0] * sides[1] * sides[2]) / (4 * area) # Radius of the circumscribed circle. Thanks again, Copilot
		
		angles[0] = (180 / pi) * asin((sides[0] / (circleRadius * 2))) # Calculate corners using sides
		angles[1] = (180 / pi) * asin((sides[1] / (circleRadius * 2))) # Thanks StackOverflow
		angles[2] = (180 / pi) * asin((sides[2] / (circleRadius * 2)))

	
	elif c == "2": # SSA
		sides[0] = float(input("Side A? "))
		sides[1] = float(input("Side B? "))
		angles[0] = float(input("Angle opp. A? "))

		angles[1] = degrees(asin((sides[1] * sin(radians(angles[0]))) / sides[0])) # I was stuck here for SO LONG because I forgot to do DEGREES()

		if  input("Any key if angle opp. B is obtuse?") != "":
			angles[1] = 180 - angles[1]

		angles[2] = 180 - angles[0] - angles[1]

		sides[2] = (sin(radians(angles[2])) * sides[0]) / sin(radians(angles[0])) # Thanks mathsisfun.com

	
	elif c == "3": # SAS
		sides[0] = float(input("Side A? "))
		angles[2] = float(input("Angle opp. C? "))
		sides[1] = float(input("Side B? "))

		sides[2] = sqrt(sides[0] ** 2 + sides[1] ** 2 - 2 * sides[0] * sides[1] * cos(angles[2] * pi / 180)) # Thanks Copilot

		semiSum = (sides[0] + sides[1] + sides[2]) / 2 # Code hasn't finished DRYing yet
		area = sqrt(semiSum * (semiSum - sides[0]) * (semiSum - sides[1]) * (semiSum - sides[2])) 
		circleRadius = (sides[0] * sides[1] * sides[2]) / (4 * area)

		angles[0] = degrees(asin((sides[0] / (circleRadius * 2))))
		angles[1] = degrees(asin((sides[1] / (circleRadius * 2))))


	elif c == "4": # AAS
		angles[0] = float(input("Angle opp. A? "))
		angles[2] = float(input("Angle opp. C? "))
		sides[2] = float(input("Side C? "))

		if angles[0] + angles[2] > 180:
			print(" ")
			print("Triangle has 0 area.")
			print(" ")
			continue

		angles[1] = 180 - angles[0] - angles[2]

		sides[0] = (sides[2] * sin(radians(angles[0]))) / sin(radians(angles[2]))  # Thanks Copilot
		sides[1] = (sides[2] * sin(radians(angles[1]))) / sin(radians(angles[2]))


	elif c == "5": # ASA
		angles[0] = float(input("Angle opp. A? "))
		sides[2] = float(input("Side C? "))
		angles[1] = float(input("Angle opp. B? "))

		if angles[0] + angles[1] > 180:
			print("Triangle has 0 area.")
			continue

		angles[2] = 180 - angles[0] - angles[1]

		sides[0] = (sides[2] * sin(radians(angles[0]))) / sin(radians(angles[2]))
		sides[1] = (sides[2] * sin(radians(angles[1]))) / sin(radians(angles[2]))

	else:
		break

	print(" ")
	print("Side A:") # Almost as many print statements as HybridOS v2
	print(sides[0])
	print("Side B:")
	print(sides[1])
	print("Side C:")
	print(sides[2])
	input("...") # Restpoints to help with scrolling up to copy an answer
	print("Angle opp. A:")
	print(angles[0])
	print("Angle opp. B:")
	print(angles[1])
	print("Angle opp. C:")
	print(angles[2])
	input("...")

	semiSum = (sides[0] + sides[1] + sides[2]) / 2
	print("Area:")
	print(sqrt(semiSum * (semiSum - sides[0]) * (semiSum - sides[1]) * (semiSum - sides[2])))
	input("...")
