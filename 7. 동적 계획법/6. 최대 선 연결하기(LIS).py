# LIS응용 문제 -> why..?
import sys
filePath_laptop = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\7. 동적 계획법\\input.txt"
filePath_desktop = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\python_algo_practice\\Python-Algorithom\\7. 동적 계획법\\input.txt"
sys.stdin = open(filePath_desktop, "rt")
n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)

dp = [0] * (n+1)
dp[1] = 1
for i in range(2, n+1):
  length = 1
  for j in range(1, i):
    if arr[j] < arr[i]:
      length = max(length, dp[j]+1)
  dp[i] = length

print(max(dp))
