import re
nums = input("Enter file size 1, erase rate 1, file size 2, erase rate 2 separated by a space ")
numsarr = re.split(" ", nums)
numsarr = list(map(int,numsarr))
fs1 = numsarr[0]
er1 = numsarr[1]
fs2 = numsarr[2]
er2 = numsarr[3]
counter = 0
while(fs2 >= er2):
	fs2 = fs2 - er2
	counter += 1
while(fs1 >= er1):
	fs1 = fs1 - er1
	counter += 1
print(counter," seconds")