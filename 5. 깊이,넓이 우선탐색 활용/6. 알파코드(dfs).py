# 다시 풀어볼 문제 -> 아이디어 다시 보기
import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\5. 깊이,넓이 우선탐색 활용\\input.txt"
sys.stdin = open(filePath, "rt")

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
    for i in range(1, 27): # 알파벳 a(=1) ~ z(=26)까지 가지를 뻗는 상태트리 생성
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