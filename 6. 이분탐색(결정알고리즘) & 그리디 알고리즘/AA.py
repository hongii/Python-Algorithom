n, m = map(int, input().split())
dvd = list(map(int, input().split()))

maxTime = sum(dvd)
lt = 1
rt = maxTime
res = 0
while lt <= rt:
  mid = (lt + rt) // 2
  tmpSum = 0
  cnt = 0
  for x in dvd:
    tmpSum += x 
    if tmpSum >= mid:
      cnt += 1
      tmpSum = x
      # print(mid, cnt, tmpSum)

  if cnt == m:
    res = mid
    lt = mid + 1
  elif cnt < m:
    rt = mid - 1
  else:
    lt = mid + 1
  
print(res)
