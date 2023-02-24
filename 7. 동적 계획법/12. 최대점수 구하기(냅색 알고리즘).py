# 2차원 dp 테이블 이용, 하나의 문제유형은 한번만 풀 수 있다(배점 10점, 5초 걸리는 문제는 한번만 풀 수 있다) -> 이 조건이 있기 때문에 2차원 dp테이블이 필요하다.
# but, 메모리 할당이 커지면 시간도 오래걸리기 때문에 1차원으로 해결해야한다.
# 따라서, 1차원 dp 테이블로 풀이 -> dp테이블을 채울때 제한시간 m부터 거꾸로 내려가면서 채운다.
# 10. 가방문제 와 11. 동전교환 문제처럼 dp테이블을 앞에서 부터 채우면 중복적용이 허용되므로(같은 동전 여러개 사용가능) 뒤에서 부터 채워야한다.

import sys
filePath_laptop = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\7. 동적 계획법\\input.txt"
filePath_desktop = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\python_algo_practice\\Python-Algorithom\\7. 동적 계획법\\input.txt"
sys.stdin = open(filePath_desktop, "rt")

n, m = map(int, input().split())
scoreAndTime = [list(map(int,input().split())) for _ in range(n)]
dp = [0] * (m+1)

for i in range(n):
  score, time = scoreAndTime[i][0], scoreAndTime[i][1]
  for j in range(m, time-1, -1): # 제한시간인 m부터 거꾸로 내려가면서 dp를 채운다 -> 하나의 문제유형을 1번만 풀기위함(중복 피하기 위함)
    dp[j] = max(dp[j], dp[j-time] + score)
print(dp[m])