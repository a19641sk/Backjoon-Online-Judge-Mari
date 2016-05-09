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

''' Another Solution
originalNumber = input()
if int(originalNumber) < 10:
	originalNumber = '0' + str(originalNumber)
else :
	originalNumber = str(originalNumber)
new = originalNumber
counter = 0
while True:
	new = int(new[1])*10 + (int(new[0]) + int(new[1])) % 10
	counter = counter + 1
	if new < 10:
		new = '0' + str(new)
	else :
		new = str(new)
	if new == originalNumber:
		break
print (counter)
'''
''' short coding
i=int;s=str;
def c(n):
 if n<10:return'0'+s(n)
 else:return s(n)
n=o=c(i(input()));t=0
while True:
 n=i(n[1])*10+(i(n[0])+i(n[1]))%10;t=t+1;n=c(n)
 if n==o:break
print(t)
'''
''' short coding of another solution
i=int;s=str
o=input()
if i(o)<10:n=o='0'+s(o)
else:n=o=s(o)
c=0
while True:
 n=i(n[1])*10+(i(n[0])+i(n[1]))%10;c=c+1
 if n<10:n='0'+s(n)
 else:n=s(n)
 if n==o:break
print(c)
'''

