# 다시 풀어볼 문제 -> 아이디어 생각 못함
import sys
filePath_laptop = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\6. 이분탐색(결정알고리즘) & 그리디 알고리즘\\input.txt"
filePath_desktop = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\python_algo_practice\\Python-Algorithom\\6. 이분탐색(결정알고리즘) & 그리디 알고리즘\\input.txt"
sys.stdin = open(filePath_desktop, "rt")

n, c = map(int, input().split())
position = [int(input()) for _ in range(n)]
position.sort()
res = 0

lt = position[0]
rt = position[-1]
while lt <= rt:
  mid = (lt + rt) // 2
  
  # 가까운 두 말의 거리가 mid값 이상이 되도록 말을 배치
  cnt = 1 # 맨 처음 죄표에 말 한마리 배치
  pre = 0 # 가장 가까운 이전 말의 idx
  for i in range(1, n):
    # print( position[pre],position[i])
    if position[i] - position[pre] >= mid:
      cnt += 1
      pre = i

    if cnt == c:
      break
  
  if cnt < c:
    rt = mid - 1
  else:
    res = mid
    lt = mid + 1

print(res)


