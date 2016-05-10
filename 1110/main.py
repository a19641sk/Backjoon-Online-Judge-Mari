def check(n):
	if n < 10 :
		return '0' + str(n)
	else :
		return str(n)
originalNumber = check(int(input()))
new = originalNumber
counter = 0
while True:
	new = int(new[1])*10 + (int(new[0]) + int(new[1])) % 10
	counter = counter +1
	new = check(new)
	if new == originalNumber:
		break
print (counter)