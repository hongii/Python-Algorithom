# 플로이드 워샬 알고리즘 : 모든 정점에서 모든 정점으로의 최단거리 구하는 알고리즘
# 따라서, 2차원 dp 테이블이 필요하다.
# 각 단계마다 특정한 노드 𝑘를 거쳐 가는 경우를 확인한다. 즉, i에서 j로 가는 최단 거리보다 i에서 𝑘를 거쳐 j로 가는 거리가 더 짧은지 검사한다

'''
2차원 dp 테이블의 초기값 -> 인접행렬을 채워넣는다.(간선이 연결되어 있지 않는 곳은 무한대 값을 넣어준다)

▣ 입력설명
첫 번째 줄에는 도시의 수N(N<=100)과 도로수 M(M<=200)가 주어지고, M줄에 걸쳐 도로정보와 
비용(20 이하의 자연수)이 주어진다. 만약 1번 도시와 2번도시가 연결되고 그 비용이 13이면 
“1 2 13”으로 주어진다. 

▣ 입력예제 1
5 8
1 2 6
1 3 3
3 2 2
2 4 1
2 5 13
3 4 5
4 2 3
4 5 7
                    정점번호:  0  1  2  3  4  5    (0번 정점은 무시(더미값), 정점은 1~n번까지)
=> 초기 dp 테이블 정보 : dp = [[inf, inf, inf, inf, inf, inf],
                              [inf, 0, 6, 3, inf, inf],
                              [inf, inf, 0, inf, 1, 13],
                              [inf, inf, 2, 0, 5, inf],
                              [inf, inf, 3, inf, 0, 7],
                              [inf, inf, inf, inf, inf, 0]]

* dp[i][j]의 의미: 정점 i -> j 로 가는 최소 비용값 / k: i -> j 까지 가는데 존재하는 중간 경유지
dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])  -> 3중 for문 사용 (k가 1~n까지, i -> j로 가는 2중 for문)

'''

import sys
filePath_laptop = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\7. 동적 계획법\\input.txt"
filePath_desktop = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\python_algo_practice\\Python-Algorithom\\7. 동적 계획법\\input.txt"
sys.stdin = open(filePath_desktop, "rt")

n, m = map(int, input().split())
M = int(1e9) # M = 10억(무한대 값)
dp = [[M] * (n+1) for _ in range(n+1)]

for i in range(1, n+1): # 자기 자신으로 가는 비용은 0으로 갱신
  dp[i][i] = 0

# dp테이블 초기값은 인접행렬 간선 가중치 값으로 갱신
for i in range(m):
  i, j, w = map(int, input().split())
  dp[i][j] = w

# 모든 정점에서 모든 정점으로 가는 최소비용 구하기
for k in range(1, n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
      dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

for i in range(1, n+1):
  for j in range(1, n+1):
    if dp[i][j] == 1e9:
      print("M", end=" ")
    else:
      print(dp[i][j], end=" ")
  print()
