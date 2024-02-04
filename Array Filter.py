import re
filtersize = input("Enter filter size: ")
arrsize = input("Enter array size: ")
nums = input("Enter integers separated by space: ")
filtersize = int(filtersize)
arrsize = int(arrsize)
numsarr = re.split(" ", nums)
numsarr = list(map(int, numsarr))
answer = []
counter = 0
while(True):
	temp = []
	incounter = 0
	try:
		numsarr[filtersize + counter - 1]
	except:
		break
	while(incounter != filtersize):
		temp.append(numsarr[counter+incounter])
		incounter += 1
	counter += 1
	temp.sort()
	answer.append(temp[0])
formattedans = ""
for ans in answer:
	formattedans += str(ans)
	formattedans += " "
print(formattedans)