import sys
filePath_laptop = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\6. 이분탐색(결정알고리즘) & 그리디 알고리즘\\input.txt"
filePath_desktop = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\python_algo_practice\\Python-Algorithom\\6. 이분탐색(결정알고리즘) & 그리디 알고리즘\\input.txt"
sys.stdin = open(filePath_desktop, "rt")

n = int(input())
info = [list(map(int, input().split())) for _ in range(n)] # [키, 몸무게]
info.sort(reverse=True) # 키 순으로 내림차순 정렬

pre = info[0]
cnt = 1 # 키 순으로 내림차순으로 정렬했으므로, 맨 처음에 위치하는 사람의 키가 가장 크다. 따라서, 맨 처음 사람의 cnt를 포함시켜야 한다.
for i in range(1, n):
  if pre[1] < info[i][1]: # 키는 무조건 이전에 위치한 사람(pre)이 더 크므로 키는 볼 필요 없고, 몸무게를 이전 사람의 몸무게와 비교해서 더 무게가 많이 나가야 선발된다.
    pre = info[i]
    cnt += 1
print(cnt)