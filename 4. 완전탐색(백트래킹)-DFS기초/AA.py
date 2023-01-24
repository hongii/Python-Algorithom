import sys

# solution 추가 -> 재귀함수 조건문 추가함으로써 time limit 해결
def dfs(idx, sum, checkSum):  # checkSum은 여태 지나온 노드의 값의 합
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
  c, n = map(int, input().split())
  weight = [int(input()) for _ in range(n)]
  totalSum = sum(weight)
  max = 0
  dfs(0, 0, 0)
  print(max)
