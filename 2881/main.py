#Time over
#@profile
def main():
	
	numberOfTree = int(input())
	trees = []
	for i in range(0,numberOfTree) :
		trees.append([int(i) for i in input().split()])
	numberOfRoute = int(input())
	routes = []
	for i in range(0,numberOfRoute) :
		routes.append([int(i) for i in input().split()])
	'''
	trees = [[1,2],[3,2],[2,3],[2,5],[4,4],[6,3],[3,2],[2,3],[2,5],[4,4],[6,3],[3,2],[2,3],[2,5],[4,4],[6,3],[3,2],[2,3],[2,5],[4,4],[6,3],[3,2],[2,3],[2,5],[4,4],[6,3],[3,2],[2,3],[2,5],[4,4],[6,3],[3,2],[2,3],[2,5],[4,4],[6,3],[3,2],[2,3],[2,5],[4,4],[6,3],[3,2],[2,3],[2,5],[4,4],[6,3],[3,2],[2,3],[2,5],[4,4],[6,3],[3,2],[2,3],[2,5],[4,4],[6,3],[3,2],[2,3],[2,5],[4,4],[6,3],[3,2],[2,3],[2,5],[4,4],[6,3],[3,2],[2,3],[2,5],[4,4],[6,3],[3,2],[2,3],[2,5],[4,4],[6,3]]
	routes = [[2,2,4,4],[2,2,6,5],[3,3,5,6],[5,1,6,6],[2,2,6,5],[3,3,5,6],[5,1,6,6],[2,2,6,5],[3,3,5,6],[5,1,6,6],[2,2,6,5],[3,3,5,6],[5,1,6,6],[2,2,6,5],[3,3,5,6],[5,1,6,6],[2,2,6,5],[3,3,5,6],[5,1,6,6],[2,2,6,5],[3,3,5,6],[5,1,6,6],[2,2,6,5],[3,3,5,6],[5,1,6,6],[2,2,6,5],[3,3,5,6],[5,1,6,6],[2,2,6,5],[3,3,5,6],[5,1,6,6],[2,2,6,5],[3,3,5,6],[5,1,6,6],[2,2,6,5],[3,3,5,6],[5,1,6,6],[2,2,6,5],[3,3,5,6],[5,1,6,6],[2,2,6,5],[3,3,5,6],[5,1,6,6],[2,2,6,5],[3,3,5,6],[5,1,6,6],[2,2,6,5],[3,3,5,6],[5,1,6,6]]
	'''
	x=[]
	y=[]
	'''
	for route in routes:
		x.append(route[0])
		x.append(route[2])
		y.append(route[1])
		y.append(route[3])
	x = set(x)
	y = set(y)
	validTrees = []
	'''
	for tree in trees :
		if (tree[0] in x) and (tree[1] in y) :
			validTrees.append(tree)
	cnt = []
	for route in routes :
		count = 0
		for tree in trees:
		#for tree in validTrees :
			if ( (tree[0] == route[0] or tree[0] == route[2]) and (route[1] <= tree[1]) and (tree[1] <= route[3])) or ((tree[1] == route[1] or tree[1] == route[3]) and (route[0] <= tree[0]) and (tree[0] <= route[2])) :
				count = count + 1
		cnt.append(count)
	for i in cnt :
		print (i)
main()