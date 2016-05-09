#get first line
numberOfLine = int(input())
#get second line == first line with N numbers
string = input()
l = [int(i) for i in string.split()]
l.sort(reverse = True)
for linenumber in range(1,numberOfLine) :
	string = input()
	#if split of string is bigger than the smallest one of l which means N-biggest, append it to list l
	newLine = [int(i) for i in string.split() if int(i) > l[-1] ]
	l = l + newLine
	l.sort(reverse = True)
	l = l[0:numberOfLine]
print (l[-1])
