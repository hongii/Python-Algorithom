### 다시 풀어볼 문제 ###
import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\3. 탐색&시뮬레이션(string,1차원,2차원 리스트탐색)\\input.txt"
sys.stdin = open(filePath, "rt")
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


''' 2번째 도전 90점 => 4번에서 time limit
# 내 예상 : 아래의 코드는 최악의 경우 등차수열의 합 -> 시간 복잡도가 O(N^2)이 된다.
tmp = 0
cnt = 0
lt, rt = 0, 0
while lt <= n - 1:
  tmp += numList[rt]
  if tmp < m:
    rt += 1
    if rt >= n :
      break
  else:
    if tmp == m:
      cnt += 1
    tmp = 0
    lt += 1
    rt = lt


print(cnt)
'''

''' 1번째 도전 80점 => 4,5에서 time limmit
# 이중 for문이 아니라 O(N)으로 풀어야 한다.
tmp = 0
cnt = 0
for i in range(len(numList)):
  for j in range(i, len(numList)):
    tmp += numList[j]
    if tmp == m:
      cnt += 1
      break
    elif tmp > m:
      break
  tmp = 0
print(cnt)
'''
