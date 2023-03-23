n = int(input())
words = [input().lower() for _ in range(n)]

w1, w2 = "",  ""
for i in range(len(words)):
  midIdx = len(words[i]) // 2
  w1 = words[i][:midIdx]
  w2 = words[i][midIdx:][::-1]
  if len(words[i]) % 2 == 1:
    w2 = words[i][midIdx+1:][::-1]

  if w1 == w2:
    print("#{0} YES".format(i+1))
  else:
    print("#{0} NO".format(i+1))