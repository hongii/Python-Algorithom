import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\4. 완전탐색(백트래킹)-DFS기초\\input.txt"
sys.stdin = open(filePath, "rt")

# solution참고 -> path배열 대신 check배열을 사용해서 이미 지나간 경로인지 파악하는 것으로 변경
n, m = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
check = [0] * (n+1) 
cnt = 0

for i in range(m):
  x, y = map(int, input().split())
  graph[x][y] = 1


def dfs(v):  # v는 node번호
	global path, cnt
	if v == n:
		cnt += 1
	else:
		for i in range(1, n+1):
			if graph[v][i] == 1:
				if check[i] == 0:
					check[i] = 1
					dfs(i)
					check[i] = 0

check[1] = 1  # 1번노드 부터 n번 노드까지 가는 경로이므로 1번 노드가 시작점이 된다.
dfs(1)
print(cnt)


''' 첫번째 코드 40점 -> path배열 사용
import sys
# filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\4. 완전탐색(백트래킹)-DFS기초\\input.txt"
# sys.stdin = open(filePath, "rt")

n, m = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
path = [1]  # 1번노드 부터 n번 노드까지 가는 경로이므로 1번 노드가 시작점이 된다.
cnt = 0

for i in range(m):
  x, y = map(int, input().split())
  graph[x][y] = 1


def dfs(x, v):  # x는 깊이(depth or level), v는 node 번호
	global path, cnt
	if list(set(path)) != sorted(path):
		return
	if v == n:
		cnt += 1
		# print(*path)
	else:
		for i in range(1, n+1):
			if graph[v][i] == 1:
				path.append(i)
				dfs(x+1, i)
				path.pop()


dfs(0, 1)
print(cnt)
'''