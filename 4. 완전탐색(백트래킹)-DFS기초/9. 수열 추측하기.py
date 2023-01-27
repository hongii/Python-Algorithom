# 다시 풀어볼 문제 -> 접근 아이디어 : 이항계수 이용
import sys
from math import factorial
from itertools import permutations
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\4. 완전탐색(백트래킹)-DFS기초\\input.txt"
sys.stdin = open(filePath, "rt")
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

'''
		이항계수 배열 c:						
															  	1
																1  1
      												1  2  1       <- n=2
                            1  3  3  1      <- n=3
                          1  4  6  4  1			<- n=4	
            
  ex. n=4, f=16 일때,
       이항계수 배열 c:  1 3 3 1
        순열 배열 p:  3 1 2 4
         c[i] * p[i]:  3 3 6 4
											3+3+6+4 = 16(마지막 숫자가 16)
                      따라서, 답은 3124가 된다.
'''