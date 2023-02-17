# 다시 풀어볼 문제 -> 잘못된 결과에 대한 코드 수정 못했음
n = int(input())
inverse = list(map(int, input().split()))
res = [0]*n
for i in range(n):
  cnt = inverse[i]
  for j in range(n):
    if res[j] == 0 and cnt == 0:
      res[j] = i+1
      break
    elif res[j] == 0:
      cnt -= 1
  
print(*res)

