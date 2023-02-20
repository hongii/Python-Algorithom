# 네트워크 선 자르기(Top-Down : 재귀, 메모이제이션)
import sys
filePath_laptop = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\7. 동적 계획법\\input.txt"
filePath_desktop = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\python_algo_practice\\Python-Algorithom\\7. 동적 계획법\\input.txt"
sys.stdin = open(filePath_desktop, "rt")

n = int(input())
dp = [0]*(n+1)

def dfs(x):
  if dp[x] != 0:
    return dp[x]
  if x == 1 or x == 2:
    return x

  else:
    dp[x] = dfs(x-1) + dfs(x-2) # memoization
    return dp[x]

print(dfs(n))