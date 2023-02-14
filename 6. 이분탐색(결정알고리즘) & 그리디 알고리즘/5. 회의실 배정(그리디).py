# 다시 풀어볼 문제 -> sort함수 key사용문법, sort 오름차순 기준을 회의 끝나는 시간으로 해야하는 idea
import sys
filePath_laptop = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\6. 이분탐색(결정알고리즘) & 그리디 알고리즘\\input.txt"
filePath_desktop = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\python_algo_practice\\Python-Algorithom\\6. 이분탐색(결정알고리즘) & 그리디 알고리즘\\input.txt"
sys.stdin = open(filePath_desktop, "rt")

n = int(input())
meetingsTime = [tuple(map(int, input().split())) for _ in range(n)]
meetingsTime.sort(key = lambda x: (x[1], x[0])) # 리스트의 원소인 튜플(a, b)에서 b값 기준으로 오름차순 정렬. 즉, 여기서는 회의 끝나는 시간 기준으로 오름차순 정렬

cnt = 1
pre = meetingsTime[0][1]
for i in range(1, n):
  if pre <= meetingsTime[i][0]:
    cnt += 1
    pre = meetingsTime[i][1]
print(cnt)