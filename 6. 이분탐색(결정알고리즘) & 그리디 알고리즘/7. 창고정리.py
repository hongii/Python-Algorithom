import sys
filePath_laptop = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\6. 이분탐색(결정알고리즘) & 그리디 알고리즘\\input.txt"
filePath_desktop = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\python_algo_practice\\Python-Algorithom\\6. 이분탐색(결정알고리즘) & 그리디 알고리즘\\input.txt"
sys.stdin = open(filePath_desktop, "rt")

length = int(input())
boxes = list(map(int, input().split()))
m = int(input())

# maxIdx, minIdx = 0, 0
while m > 0:
  # 박스의 최대 높이와 최소 높이 위치 찾기
  maxHeight = 0
  minHeight = 100
  for i in range(length):
    if maxHeight < boxes[i]:
      maxHeight = boxes[i]
      maxIdx = i
    if minHeight > boxes[i]:
      minHeight = boxes[i]
      minIdx = i

  # 최대 높이에서 최소높이로 box 한개 이동  
  boxes[maxIdx] -= 1
  boxes[minIdx] += 1
  m -= 1
print(max(boxes) - min(boxes))


'''
# solution 참고 -> but, 입력값의 범위가 큰 경우 대부분 for문 안에 sort()를 사용하면 시간초과 나는 경우가 많다.
boxes.sort()
for _ in range(m):
  boxes[0] += 1
  boxes[-1] -= 1
  boxes.sort()
print(boxes[-1] - boxes[0])
'''