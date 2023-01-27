import itertools as it

n, k = map(int, input().split())
numList = list(map(int, input().split()))
m = int(input())
cnt = 0
c = list(it.combinations(numList, k))

for x in c:
  res = sum(x)
  if res % m == 0:
    cnt += 1
print(cnt)
