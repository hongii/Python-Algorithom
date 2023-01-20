n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
res = 0
l = r = n//2
for i in range(n):
	if i <= n//2:
		res += sum(board[i][l:r+1])
		l -= 1
		r += 1
	elif i > n//2:
		l += 1
		r -= 1
		res += sum(board[i][l+1:r])
print(res)
