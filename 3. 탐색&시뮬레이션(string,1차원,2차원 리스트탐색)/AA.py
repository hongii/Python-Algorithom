n, m = map(int, input().split())
numList = list(map(int, input().split()))

# 3번째 도전, solution 참고 => [lt:rt]까지의 합을 구한다.(rt번째 앞까지의 숫자까지 더함)
# tmp> m인 경우, tmp값에서 lt가 가리키고 있던 값을 빼주고 rt는 그대로 두기, lt는 1증가 !!! <-- 2번째 도전에서 나타난 time limit 해결
tmp = numList[0]
cnt = 0
lt, rt = 0, 1
while True:
  if tmp < m:
    if rt < n:
      tmp += numList[rt]
      rt += 1
    else:
      # lt가 가르키는 값부터 rt가 가르키는 값 바로 직전(numList의 마지막 원소)까지 더한 값들이 m보다 작고 rt가 더 이상 가르킬 다음 원소가 없는 경우
      break
  else:
    if tmp == m:  # tmp값에서 lt가 가르키고 있던 값을 빼준다.
      cnt += 1
    tmp -= numList[lt]
    lt += 1

print(cnt)
