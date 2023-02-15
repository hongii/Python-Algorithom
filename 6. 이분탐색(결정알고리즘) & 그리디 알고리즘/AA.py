length = int(input())
boxes = list(map(int, input().split()))
m = int(input())

# solution 참고
boxes.sort()
for _ in range(m):
  boxes[0] += 1
  boxes[-1] -= 1
  boxes.sort()
print(boxes[-1] - boxes[0])