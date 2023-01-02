T = int(input())

for i in range(T):
	n, s, e, k = map(int, input().split())
	nList = list(map(int, input().split()))

	num = nList[s-1:e]
	num.sort()
	print("#{0} {1}".format(i, num[k-1]))




