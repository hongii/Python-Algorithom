# 냅색 알고리즘
# dp[j] : j원을 거슬러 주는데 사용된 동전의 최소갯수

import sys
filePath_laptop = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\7. 동적 계획법\\input.txt"
filePath_desktop = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\python_algo_practice\\Python-Algorithom\\7. 동적 계획법\\input.txt"
sys.stdin = open(filePath_desktop, "rt")

n = int(input())
coins = list(map(int, input().split()))
m = int(input())
coins.sort()
dp = [501] * (m+1)
dp[0] = 0

for coin in coins:
  for j in range(coin, m+1):
    dp[j] = min(dp[j], dp[j-coin] + 1)
print(dp[m])