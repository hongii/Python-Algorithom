import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\4. 완전탐색(백트래킹)-DFS기초\\input.txt"
sys.stdin = open(filePath, "rt")
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

