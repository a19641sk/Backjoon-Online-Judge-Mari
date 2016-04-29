import math
num = input()
line = input()
a = [int(i) for i in line.split()]
a.sort()
m = a.pop()
term = m
while True :
	chk = []
	for i in a :
		if m % i != 0 :
			chk.append(False)
	if False in chk :
		m = m + term
	else :
		break
if m == term :
	print (m*a[0])
else :
	print (m)