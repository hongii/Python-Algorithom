import sys
filePath_laptop = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\7. 동적 계획법\\input.txt"
filePath_desktop = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\python_algo_practice\\Python-Algorithom\\7. 동적 계획법\\input.txt"
sys.stdin = open(filePath_desktop, "rt")

n = int(input())

dp = [0]*(n+1) # memoization
dp[1] = 1
dp[2] = 2
for i in range(3, n+1): # bottom-up
  dp[i] = dp[i-1] + dp[i-2]
print(dp[n])