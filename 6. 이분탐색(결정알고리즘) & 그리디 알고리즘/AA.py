length = int(input())
boxes = list(map(int, input().split()))
m = int(input())

for i, x in enumerate(boxes):
  boxes[i] = [x, i] # boxes리스트 요소를 [높이, 위치(idx)]쌍으로 다시 저장

while m > 0:
  maxHeight, maxIdx = max(boxes)
  minHeight, minIdx = min(boxes)
  boxes[maxIdx][0] -= 1
  boxes[minIdx][0] += 1
  m -= 1
  
print(max(boxes)[0] - min(boxes)[0])