# 다시 풀어볼 문제 -> 잘못된 결과에 대한 코드 수정 못했음
import sys
filePath_laptop = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\6. 이분탐색(결정알고리즘) & 그리디 알고리즘\\input.txt"
filePath_desktop = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\python_algo_practice\\Python-Algorithom\\6. 이분탐색(결정알고리즘) & 그리디 알고리즘\\input.txt"
sys.stdin = open(filePath_desktop, "rt")

n = int(input())
inverse = list(map(int, input().split()))
res = [0]*n
for i in range(n):
  cnt = inverse[i]
  for j in range(n):
    if res[j] == 0 and cnt == 0:
      res[j] = i+1
      break
    elif res[j] == 0:
      cnt -= 1
  
  # print(res)
print(*res)

