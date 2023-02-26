import sys
filePath_laptop = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\7. 동적 계획법\\input.txt"
filePath_desktop = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\python_algo_practice\\Python-Algorithom\\7. 동적 계획법\\input.txt"
sys.stdin = open(filePath_desktop, "rt")

n = int(input())
inf = int(1e9)
dp = [[inf] * (n+1) for _ in range(n+1)] # 무한대 값으로 초기화

# 자기 자신으로 가는 가중치는 0으로 설정
for i in range(1, n+1):
  dp[i][i] = 0

# 입력받은 값으로 dp 테이블 초기값 넣기
while True:
  i, j = map(int, input().split())
  if i == -1 and j == -1:
    break
  else: # 양방향 그래프의 가중치는 i->j, j->i 모두 채운다.
    dp[i][j] = 1
    dp[j][i] = 1

# 플로이드 워셜
for k in range(1, n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
      dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
# print(dp)

# 회원들의 점수 구하기 -> 각 회원의 점수 들 중 최댓값이 해당 회원의 점수가 된다.(ex: dp[1] = [0, 1, 2, 2, 3] 인 경우, 1번회원의 점수는 최댓값인 3이 된다. )
scoreMin = [inf] * (n+1)
for i in range(1, n+1):
  scoreMin[i] = max(dp[i][1:])

# 회장 후보 회원번호 찾기
resNum = min(scoreMin)
res = []
for i in range(1, n+1):
  if scoreMin[i] == resNum:
    res.append(i)

print("{0} {1}".format(resNum, len(res)))
print(*res)