numberOfLine = input()
l = []
for i in range(int(numberOfLine)) :
	l.append(int(input()))
fib=[1,1]
for i in range(2,40):
	fib.append(fib[i-1]+fib[i-2])
for i in l :
	if i == 0 :
		print ('1 0')
	elif i == 1 :
		print ('0 1')
	else :
		print (str(fib[i-2]) + ' ' + str(fib[i-1]))