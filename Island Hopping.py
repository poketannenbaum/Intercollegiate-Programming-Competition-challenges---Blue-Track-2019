import re
nums = input ("Enter number of islands followed by each jump value ")
numsarr = re.split(" ", nums)
numsarr = list(map(int,numsarr))
islandnum = numsarr[0]
numsarr.pop(0)
rollingnumtojump = numsarr[0]
pointer = 0
while(True):
	if(pointer == len(numsarr) - 1):
		print("Success")
		break
	if(rollingnumtojump == 0):
		print("Failure")
		break
	try:
		numsarr[pointer]
	except:
		print("Failure")
		break
	rollingnumtojump = numsarr[pointer]
	pointer += rollingnumtojump