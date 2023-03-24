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