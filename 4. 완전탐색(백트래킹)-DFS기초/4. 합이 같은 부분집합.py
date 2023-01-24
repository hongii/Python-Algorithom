# 다시 풀어볼 문제_solution 익히기
import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\4. 완전탐색(백트래킹)-DFS기초\\input.txt"
sys.stdin = open(filePath, "rt")

# solution 
def dfs(idx, sum):
  if sum > total // 2: #시간복잡도 줄이기 위한 조건문.
    return
  if total % 2 != 0: # 원소의 총 합이 홀수라면 두 부분집합의 합이 같은 경우가 나올 수 없다. 
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
	dfs(0, 0) # 만약 두 부분집합의 합이 같은 경우가 있다면 아래 print코드는 실행되지 않는다.
	print("NO") # dfs가 강제종료 되지 않았다면, 두 부분집합의 합이 같은 경우가 없다는 뜻. 

'''
n = int(input())
numList = list(map(int, input().split()))
numList.append(-1)
m = max(numList) + 1
check = [-1] * m

def dfs(x,idx):
  if x == -1:
    set1 = [i for i in range(1, m) if check[i] == 1]
    set2 = [i for i in range(1, m) if check[i] == 0]
    # print(set1, set2)
    if sum(set1) == sum(set2):
      return True
    else:
      return False

  else:
    check[x] = 1
    res1 = dfs(numList[idx+1], idx+1)
    check[x] = 0
    res2 = dfs(numList[idx+1], idx+1)
    if res1 or res2:
      print("YES")
      exit()
  return False
    
if __name__ == "__main__":
  res = dfs(numList[0], 0)
  if res == False:
    print("NO")
'''