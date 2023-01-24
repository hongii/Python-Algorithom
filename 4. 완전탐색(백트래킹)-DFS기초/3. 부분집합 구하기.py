# 다시 풀어볼 문제 
import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\4. 완전탐색(백트래킹)-DFS기초\\input.txt"
sys.stdin = open(filePath, "rt")

n = int(input())
check = [0]*(n+1)

def dfs(x):
	if x > n:
		for i in range(1, n+1):
			if check[i] == 1:
				print(i, end=" ")
		print()
	else:
		# 왼쪽자식(x값을 부분집합으로 포함하는 가지)
		check[x] = 1
		dfs(x+1)

		# 오른쪽자식(x값을 부분집합으로 포함하지 않는 가지)
		check[x] = 0
		dfs(x+1)


if __name__ == "__main__":
	dfs(1)



# ex. n=3일 때, 부분집합 구하는 로직
# 													1
# 									o/  		        \x
# 									2				 	       2
# 							o/     \x 	     o/ 	   \x
# 							3       3        3        3
# 					o/   \x  o/   \x  o/   \x  o/   \x
# 					4    4   4    4   4    4   4     4
# check:[1,1,1], [1,1,0], [1,0,1], [1,0,0], [0,1,1], [0,1,0], [0,0,1], [0,0,0]
#  	{1,2,3}, {1,2}, {1,3}, {1}, {2,3}, {2}, {3}, 공집합		
