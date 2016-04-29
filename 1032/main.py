num = int(input())
l =[]
for i in range(num):
	l.append(input())
sen = ''
for i in range(len(l[0])):
	f = l[0][i]
	b = True
	for j in range(1,num):
		if f != l[j][i]:
			b = False
	if b == True :
		sen += f
	else :
		sen += '?'
print (sen)
