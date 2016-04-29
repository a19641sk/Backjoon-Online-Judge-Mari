num = int(input())
line = input()
a = [int(i) for i in line.split()]
line = input()
b = [int(i) for i in line.split()]
a.sort()
b.sort(reverse = True)
acc = 0
for i in range(num) :
	acc += int(a[i]) * int(b[i])
print (acc)