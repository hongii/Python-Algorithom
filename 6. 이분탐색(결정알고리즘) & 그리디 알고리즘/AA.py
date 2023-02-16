n, m = map(int, input().split())
weight = list(map(int, input().split()))
weight.sort()
cnt = 0
while weight:
  if len(weight) == 1:
    cnt += 1
    break
  # 가장 무거운 승객과 가장 가벼운 승객의 몸무게 합이 m을 초과하는 경우, 가장 무거운 승객만 구조된다.
  if weight[0] + weight[-1] > m:
    weight.pop()
    cnt += 1

  # 가장 무거운 승객과 가장 가벼운 승객의 몸무게 합이 m이하라면 두명이 함께 구조된다.
  else:
    weight.pop()
    weight.pop(0)
    cnt += 1

print(cnt)