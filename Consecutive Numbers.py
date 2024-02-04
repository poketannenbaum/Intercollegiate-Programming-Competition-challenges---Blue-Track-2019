import re
nums = input("Enter your numbers separated by a space ")
numarray = re.split(" ", nums)
numarray = list(map(int, numarray))
counter = 0
answer = ""
for num in numarray:
	if(counter == 0):
		counter += 1
	elif(counter == 1):
		counter += 1
	else:
		if (num == numarray[counter - 1] and num == numarray[counter - 2]):
			answer = "Consecutive values found for "
			print(answer, num)
		counter += 1
if (answer == ""):
	print("Consecutive values not found")
