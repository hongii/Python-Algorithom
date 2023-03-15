import itertools as it
import sys
filePath_laptop = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\6. 이분탐색(결정알고리즘) & 그리디 알고리즘\\input.txt"
filePath_desktop = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\python_algo_practice\\Python-Algorithom\\6. 이분탐색(결정알고리즘) & 그리디 알고리즘\\input.txt"
sys.stdin = open(filePath_desktop, "rt")
n = int(input())
numList = list(map(int, input().split()))

'''
# itertools를 이용한 모든 부분집합 구하기
cb = []
for i in range(n+1):
  cb += list(it.combinations(numList, i))
print(cb)
'''

totalSum = sum(numList)
cb = []
for i in range(n+1):
  cb += list(it.combinations(numList, i))

# ex. itertools로 생성한 [1, 2, 3]의 부분집합은,
# [], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3] 이다.
# 여기서 두 부분집합의 합은, [1]과 [2, 3]인 두 부분집합의 합이나 [2, 3]과 [1]인 두 부분집합의 합은 같으므로, for문의 range범위를 len(cd)//2로 한 것
for i in range(len(cb) // 2): 
  if totalSum-sum(cb[i]) == sum(cb[i]):
    print("YES")
    break
else:
  print("NO")
