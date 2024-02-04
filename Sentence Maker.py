listofletters = input("Enter the list of letters: ")
senttoformat = input("Enter the sentence to be formed: ")
listofletters = list(listofletters)
senttoformat = list(senttoformat)
for letter in senttoformat:
	if (letter == " "):
		senttoformat.remove(letter)
for i in listofletters:
	if i in senttoformat:
		senttoformat.remove(i)
try:
	senttoformat[0]
	print("not possible")
except:
	print("possible")