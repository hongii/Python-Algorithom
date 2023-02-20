import sys
filePath_laptop = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\7. 동적 계획법\\input.txt"
filePath_desktop = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\python_algo_practice\\Python-Algorithom\\7. 동적 계획법\\input.txt"
sys.stdin = open(filePath_desktop, "rt")
n = int(input())
dp = [0] * (n+2)

dp[1] = 1
dp[2] = 2
for i in range(3, n+2):
  dp[i] = dp[i-1] + dp[i-2]

# 돌다리를 건너서(n개의 돌다리를 건너서) 반대편 지점까지 도착(+1)해야 하므로, dp[n]이 아니라 dp[n+1]의 값을 구해야한다.
print(dp[n+1])