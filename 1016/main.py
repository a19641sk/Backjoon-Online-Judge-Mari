import math

line = input()
split = line.split()
small = int(split[0])
big = int(split[1])

l = []
for i in range(2,math.ceil(math.sqrt(big))+1):
	sqr = i**2
	if sqr > big :
		break
	l.append(sqr)

nl = []
for i in l:
	if small % i == 0:
		lower = small//i
	else :
		lower = small//i +1
	for j in range(lower,big//i+1):
		k = i * j
		nl.append(k)
print ( big - small + 1 -len(set(nl)))