N,M = map(int,input().split())
spaceState = [] # It has [car, costRate] list and car 0 is empty state
carWeight = [0] # first one is dummy data
money = 0
queue = []
def searchAndCharge(inAndOut) : #if the code become longer and complexed, global variable could be harmful.
	global money
	for space in range(N) :
		if spaceState[space][0] == 0 :
			spaceState[space][0] = inAndOut
			money += spaceState[space][1] * carWeight[inAndOut]
			break
		elif space == N-1:
			queue.append(inAndOut)
	return money
for _ in range(N) :
	spaceState.append([0,int(input())])
for _ in range(M) :
	carWeight.append(int(input()))
for _ in range(2*M) :
	inAndOut = int(input())
	if inAndOut>0:
		money = searchAndCharge(inAndOut)
	else :
		for space in range(N) :
			if spaceState[space][0] == -inAndOut :
				spaceState[space][0] = 0
		if queue != [] :
			searchAndCharge(queue[0])
			queue = queue[1:]
print (money)
