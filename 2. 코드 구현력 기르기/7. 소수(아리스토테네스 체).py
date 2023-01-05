import sys
# filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\2. 코드 구현력 기르기\\input.txt"
# sys.stdin = open(filePath,"rt");

### solution : 아리스토테네스 체 풀이 이용 ###
n = int(input())
primeCnt=[0] * (n+1);
cnt = 0
for i in range(2, n+1):
	if(primeCnt[i] == 0):
		cnt += 1
		for j in range(i, n+1, i):
			primeCnt[j] = 1 

print(cnt)





''' case1 sucess, but others cases are time limit
n = int(input())
prime=[]

for i in range(2, n+1):
	for j in range(2, i+1):
		if(i == j):
			prime.append(j);
		elif(i % j == 0):
			break;
		

print(len(prime));

'''

