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
