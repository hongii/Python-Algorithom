import sys
filePath_laptop = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\3. 탐색&시뮬레이션(string,1차원,2차원 리스트탐색)\\input.txt"
filePath_desktop = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\python_algo_practice\\Python-Algorithom\\3. 탐색&시뮬레이션(string,1차원,2차원 리스트탐색)\\input.txt"
sys.stdin = open(filePath_desktop, "rt")

# solution 참고해서 다시 풀어본 것
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
res = 0
l = r = n//2
for i in range(n):
	res += sum(board[i][l:r+1])
	if i < n//2:
		l -= 1
		r += 1
	elif i >= n//2:
		l += 1
		r -= 1

print(res)

# 첫번째 풀이 -> 100점
# n = int(input())
# board = [list(map(int, input().split())) for _ in range(n)]
# res = 0

# j = 0
# for i in range(n//2, -1, -1):
#   tmp1 = board[n//2 - j]  # 윗부분 삼각형(가운데 n//2행 포함)
#   res += sum(tmp1[j:n-j])
#   if (i != n//2):  # 아랫부분 역삼각형(가운데 n//2행 포함안함)
#     tmp2 = board[n//2 + j]
#     res += sum(tmp2[j:n-j])
#   j += 1
# print(res)
