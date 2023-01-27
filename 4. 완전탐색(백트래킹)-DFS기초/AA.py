from math import factorial
from itertools import permutations
n, f = map(int, input().split())
c = [0] * n
numList = [i for i in range(1, n+1)]
p = list(permutations(numList, n)) # 가능한 순열이 들어간다.

# n의 값에 따른 이항계수 배열 생성 (n=4라면 배열 c에는 [1,3,3,1], n=5라면 [1,4,6,4,1]이 들어간다.) 
for i in range(n):
  c[i] = factorial(n-1) // (factorial(n-1 - i) * factorial(i))

# 가능한 순열과 이항계수의 곱을 이용하여 마지막 숫자(f)와 같은 순열을 찾기
for i in range(len(p)):
  res = [x*y for x,y in zip(c,p[i])]
  if sum(res) == f:
    print(*p[i])
    break

