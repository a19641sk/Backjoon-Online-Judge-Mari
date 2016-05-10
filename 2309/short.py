l=[];exec(9*'l+=[int(input())];');l.sort()
for i in l:
	for j in l:
		if i+j==sum(l)-100 and i!=j:l.remove(i);l.remove(j) 
		#we don't need to check that i!=j because of problems condition prevent it.
		#Because of the whole 9 numbers are different,
		#if there exist x, which 2*x = sum(l)-100, always there is a (i,j) pair with condition i < x < j
for i in l:print(i)