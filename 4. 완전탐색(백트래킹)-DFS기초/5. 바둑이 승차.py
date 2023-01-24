# 다시 풀어볼 문제 -> 재귀함수 조건문 추가한 부분 다시 이해하기
import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\4. 완전탐색(백트래킹)-DFS기초\\input.txt"
sys.stdin = open(filePath, "rt")

#solution 추가 -> 재귀함수 조건문 추가함으로써 time limit 해결
def dfs(idx, sum, checkSum): # checkSum은 여태 지나온 노드의 값의 합
  global max, totalSum
  # resSum = totalSum - checkSum, resSum은 전체 바둑이의 총 무게(전체 노드의 합) - 현재까지 지나온 노드의 합(여태 지나온 노드의 합) -> 즉, leaf node까지 남은 노드의 값의 합
  if sum + (totalSum - checkSum) < max:
    return
  if sum > c:
    return
  if idx == n:
    if sum <= c and max < sum:
      max = sum
      return
  else:
    dfs(idx+1, sum + weight[idx], sum + weight[idx])
    dfs(idx+1, sum, sum + weight[idx])
      
if __name__ == "__main__":
  c, n  = map(int, input().split())
  weight = [int(input()) for _ in range(n)]
  totalSum = sum(weight)
  max = 0
  dfs(0, 0, 0)
  print(max)


'''첫번째 코드 60점 -> 4,5번 테케에서 타임리밋
def dfs(idx, sum):
  global max
  if sum > c:
    return
  if idx == n:
    if sum <= c and max < sum:
      max = sum
      return
  else:
    dfs(idx+1, sum + weight[idx])
    dfs(idx+1, sum)
      
if __name__ == "__main__":
  c, n  = map(int, input().split())
  weight = [int(input()) for _ in range(n)]
  max = 0
  dfs(0, 0)
  print(max)
'''