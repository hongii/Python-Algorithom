import sys
# filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\2. 코드 구현력 기르기\\input.txt"
# sys.stdin = open(filePath,"rt");

n = int(input())
numList = list(map(int, input().split()))

max = 0;
res = numList[0];
def digit_sum(x):
	x = str(x);
	x_sum = 0;
	for i in range(len(x)):
		x_sum += int(x[i]);
	return x_sum;

for x in numList:
	tmp_max = digit_sum(x);
	if(max < tmp_max):
		max = tmp_max;
		res = x;
print(res);

