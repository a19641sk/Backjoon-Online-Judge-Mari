numberOfLine = input()
l = []
for i in range(int(numberOfLine)) :
	l.append(str(input()))

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for string in l :
	count = []
	for letter in alphabet :
		count.append((string.count(letter),letter))
	count.sort()
	if count[-1][0] == count[-2][0] :
		print ('?')
	else :
		print (count[-1][1])

''' Same result but this spends more time. 
numberOfLine = input()
l = []
for i in range(int(numberOfLine)) :
	l.append(str(input()))

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for string in l :
	count = -1
	maxLetter = '?'
	for letter in alphabet :
		countOfLetter = string.count(letter)
		if countOfLetter > count :
			count = countOfLetter
			maxLetter = letter
		elif countOfLetter == count :
			maxLetter = '?'
	print (maxLetter)
'''