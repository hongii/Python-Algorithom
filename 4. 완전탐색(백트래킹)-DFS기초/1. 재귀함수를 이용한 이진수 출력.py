import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\4. 완전탐색(백트래킹)-DFS기초\\input.txt"
sys.stdin = open(filePath, "rt")
n = int(input())

def decimalToBinary(x):
	if x >= 1:
		decimalToBinary(x // 2)
		print(x % 2, end = "")

decimalToBinary(n)