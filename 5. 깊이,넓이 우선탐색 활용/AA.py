codeStr = list(input())
code = [int(x) for x in codeStr]
cnt = 0
res = []


def dfs(x):
  global cnt
  if x == len(code):
    cnt += 1
    for a in res:
      print(chr(a+64), end="")
    print()
  else:
    for i in range(1, 27):  # 알파벳 a(=1) ~ z(=26)까지 가지를 뻗는 상태트리 생성
      if i == code[x]:
        res.append(i)
        dfs(x+1)
        res.pop()
      elif i == int("".join(codeStr[x:x+2])) and i >= 10:
        res.append(i)
        dfs(x+2)
        res.pop()


dfs(0)
print(cnt)
