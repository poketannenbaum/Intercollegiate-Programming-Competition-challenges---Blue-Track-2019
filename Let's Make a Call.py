num = input("Enter the phone number: ")
allnumber = list(num)
answer = []
counter = 0
stranswer = ""
while(True):
	if(allnumber[counter] == "A" or allnumber[counter] == "B" or allnumber[counter] == "C" ):
		answer.append("2")
		counter += 1
	elif(allnumber[counter] == "D" or allnumber[counter] == "E"or allnumber[counter] == "F"):
		answer.append("3")
		counter += 1
	elif(allnumber[counter] == "G"or allnumber[counter] == "H"or allnumber[counter] == "I"):
		answer.append("4")
		counter += 1
	elif(allnumber[counter] == "J"or allnumber[counter] == "K"or allnumber[counter] == "L"):
		answer.append("5")
		counter += 1
	elif(allnumber[counter] == "M"or allnumber[counter] == "N"or allnumber[counter] == "O"):
		answer.append("6")
		counter += 1
	elif(allnumber[counter] == "P"or allnumber[counter] == "Q"or allnumber[counter] == "R"or allnumber[counter] == "S"):
		answer.append("7")
		counter += 1
	elif(allnumber[counter] == "T"or allnumber[counter] == "U"or allnumber[counter] == "V"):
		answer.append("8")
		counter += 1
	elif(allnumber[counter] == "W"or allnumber[counter] == "X"or allnumber[counter] == "Y" or allnumber[counter] == "Z"):
		answer.append("9")
		counter += 1
	else:
		answer.append(allnumber[counter])
		counter += 1
	try:
		allnumber[counter]
	except:
		break
for ans in answer:
	stranswer += ans
print(stranswer)