import sys
def dfs(idx, sum):
  if sum > total // 2:  # 시간복잡도 줄이기 위한 조건문.
    return
  if total % 2 != 0:  # 원소의 총 합이 홀수라면 두 부분집합의 합이 같은 경우가 나올 수 없다.
    return
  if idx == n:
    if sum == (total-sum):
      print("YES")
      sys.exit(0)
  else:
    dfs(idx+1, sum + numList[idx])
    dfs(idx+1, sum)


if __name__ == "__main__":
	n = int(input())
	numList = list(map(int, input().split()))
	total = sum(numList)
	dfs(0, 0)  # 만약 두 부분집합의 합이 같은 경우가 있다면 아래 print코드는 실행되지 않는다.
	print("NO")  # dfs가 강제종료 되지 않았다면, 두 부분집합의 합이 같은 경우가 없다는 뜻.


