import re
nums = input("Enter your numbers separated by a space ")
numsarr = re.split(" ", nums)
numsset = set(numsarr)
for num in numsset:
	if (numsarr.count(num) < 1):
		print(num, "occurs ", numsarr.count(num), " time")
	else:
		print(num, "occurs ", numsarr.count(num), " times")