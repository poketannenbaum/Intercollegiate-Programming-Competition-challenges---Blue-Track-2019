import re
shiftnumber= input("Enter the shift number ")
nums = input("Enter the numbers in list separated by space. End with 0. ")
shiftnumber = int(shiftnumber)
ogshift = shiftnumber
numsarr = re.split(" ", nums)
numsarr = list(map(int, numsarr))
numsarr.pop(len(numsarr) - 1)
templist = []
counter = 0
while(True):
	try:
		numsarr[shiftnumber]
	except:
		while(counter < ogshift):
			templist.append(numsarr[counter])
			counter += 1
		break
	templist.append(numsarr[shiftnumber])
	shiftnumber += 1
strans = ""
for ans in templist:
	strans += str(ans)
	strans += " "
print(strans)