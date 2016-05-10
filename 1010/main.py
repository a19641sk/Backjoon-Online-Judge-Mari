from math import factorial as f
numberOfCase = int(input())
for i in range(0,numberOfCase) :
	l=list(map(int,input().split()))
	print(int(f(l[1])/(f(l[0])*f(l[1]-l[0]))))