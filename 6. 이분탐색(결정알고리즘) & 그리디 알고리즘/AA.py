n, m = map(int, input().split())
dvd = list(map(int, input().split()))
totalTime = sum(dvd)
maxTime = max(dvd)
lt = 1
rt = totalTime
res = 0
while lt <= rt:
  mid = (lt + rt) // 2
  tmpSum = 0
  cnt = 1
  for x in dvd:
    if tmpSum + x > mid:
      cnt += 1
      tmpSum = x
    else:
      tmpSum += x

  if mid >= maxTime and cnt <= m: # 반례 수정: dvd 최소 용량은 적어도 곡의 길이의 최대값보다는 크거나 같아야 한다. -> mid >= maxTime 조건 추가
    res = mid
    rt = mid - 1
  else:
    lt = mid + 1
  
print(res)
