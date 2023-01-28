import sys
# filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\4. 완전탐색(백트래킹)-DFS기초\\input.txt"
# sys.stdin = open(filePath, "rt")

n, m = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
check = [0] * (n+1)
cnt = 0

for i in range(m):
  x, y = map(int, input().split())
  graph[x][y] = 1


def dfs(x, v):  # x는 깊이(depth or level), v는 node 번호
	global path, cnt
	if v == n:
		cnt += 1
		# print(*path)
	else:
		for i in range(1, n+1):
			if graph[v][i] == 1:
				if check[i] == 0:
					check[i] = 1
					dfs(x+1, i)
					check[i] = 0


check[1] = 1  # 1번노드 부터 n번 노드까지 가는 경로이므로 1번 노드가 시작점이 된다.
dfs(0, 1)
print(cnt)
