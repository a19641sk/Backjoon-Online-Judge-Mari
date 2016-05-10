n,k=map(int, input().split());
s=list(map(int, input().split(',')))
for i in range(k):
	t = []
	for i in range(n-1) :
		t.append(s[i+1]-s[i])
	s = t
	n = n-1
print (",".join(map(str,s)))