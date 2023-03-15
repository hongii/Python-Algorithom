import itertools as it
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

for i in range(len(cb) // 2):
  if totalSum-sum(cb[i]) == sum(cb[i]):
    print("YES")
    break
else:
  print("NO")
