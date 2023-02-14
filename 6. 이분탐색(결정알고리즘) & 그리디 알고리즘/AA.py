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