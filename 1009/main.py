numberOfLine = input()
a = []
b = []
for i in range(int(numberOfLine)):
	line = input()
	splits = line.split(' ')
	x = int(splits[0])%10
	y = int(splits[1])
	a.append(x)
	b.append(y)

for i in range(int(numberOfLine)):
	mul = []
	x = a[i]
	while (x not in mul):
		mul.append(x)
		x = (x*a[i])%10
	k = mul[b[i]%len(mul)-1]
	if k == 0:
		print ('10')
	else :
		print (k)