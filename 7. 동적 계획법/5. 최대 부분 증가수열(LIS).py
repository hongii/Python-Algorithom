# LIS(Longest Increasing Subsequence)
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
      length = max(length, dp[j] + 1)
  dp[i] = length
print(max(dp))

'''
arr = [5, 3, 7, 8, 6, 2, 9, 4]
1) 5가 마지막 항일때의 증가수열 : [5]
2) 3이 마지막 항일때의 증가수열 : [3]
3) 7이 마지막 항일때의 증가수열 : [3, 7], [5, 7]
4) 8이 마지막 항일때의 증가수열 : [3, 7, 8], [5, 7, 8], [3, 8], [5, 8]
5) 6이 마지막 항일때의 증가수열 : [3, 6], [5, 6]
6) 2가 마지막 항일때의 증가수열 : [2]
7) 9가 마지막 항일때의 증가수열 : 위의 1)~6)의 부분수열에서 9를 각각 포함시킨 수열들 모두 포함
8) 4가 마지막 항일때의 증가수열 : [3, 4], [2, 4]

즉, 부분 증가 수열의 최대길이를 저장하는 dp 테이블은,
dp = [1, 1, 2, 3, 2, 1, 4, 2]가 된다.
arr[i] 값이 마지막 항이 되므로, arr[0]~arr[i-1]의 값들 중 arr[i]값보다 더 작은값인 arr[x]를 찾아 해당 dp[x] + 1한 값이 dp[i]가 된다.
'''