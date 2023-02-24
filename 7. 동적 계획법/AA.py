n, m = map(int, input().split())
scoreAndTime = [list(map(int,input().split())) for _ in range(n)]
dp = [0] * (m+1)

for i in range(n):
  score, time = scoreAndTime[i][0], scoreAndTime[i][1]
  for j in range(m, time-1, -1): # 제한시간인 m부터 거꾸로 내려가면서 dp를 채운다 -> 하나의 문제유형을 1번만 풀기위함(중복 피하기 위함)
    dp[j] = max(dp[j], dp[j-time] + score)
print(dp[m])