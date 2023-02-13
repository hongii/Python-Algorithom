k, n = map(int, input().split())
numList = [int(input()) for _ in range(k)]

maxLen = max(numList)
lt = 1
rt = maxLen
res = 0

while lt <= rt:
  mid = (lt + rt) // 2
  total = 0
  for x in numList:
    total += x // mid

  if total >= n:
    res = mid 
    lt = mid + 1
  elif total < n:
    rt = mid - 1

print(res)