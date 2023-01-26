from itertools import permutations 
import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\4. 완전탐색(백트래킹)-DFS기초\\input.txt"
sys.stdin = open(filePath, "rt")

n, m = map(int, input().split())
numList = [i for i in range(1, n + 1)]

data = list(permutations(numList, m))
for x in data:
	print(*x)
print(len(data))