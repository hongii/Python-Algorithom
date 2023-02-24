### 냅색 알고리즘 ###
'''
w: 보석의 무게, v: 보석의 가치, j: 가방에 담을 수 있는 보석의 총 무게
dp[j] = max(dp[j-w] + v, dp[j]) 

입력예제
4 11
5 12
3 8
6 14
4 8
=> 보석의 종류는 4가지, 가방에 담을 수 있는 보석의 최대 무게는 11
1) 보석무게(w) = 5, 보석의 가치(v) = 12 -> 이 보석을 이용하여 dp 테이블을 먼저 채운다.
    j   0  1  2  3  4  5  6  7  8  9  10  11
    dp  0  0  0  0  0  12 12 12 12 12 24  24
                       ↑               ↑
                    dp[5-5]+12      dp[10-5]+12

2) 보석무게(w) = 3, 보석의 가치(v) = 8 -> 이 보석을 이용하여 dp 테이블을 다시 추가적으로 채운다.
    j   0  1  2  3  4  5  6  7  8  9  10  11
    dp  0  0  0  8  8  12 16 16 20 24 24  28
                 ↑      ↑
          dp[3-3]+8    dp[5-3]+8 = 8
                          vs
                      기존의 dp[5] = 12 중, max값으로 갱신한다.
                      즉,dp[j] = max(dq[j], dp[j-w]+v)   

3) ...나머지 보석 2개에 대해서도 반복 수행.
'''

import sys
filePath_laptop = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\7. 동적 계획법\\input.txt"
filePath_desktop = "C:\\Users\\cywoo\\OneDrive\\바탕 화면\\Python\\python_algo_practice\\Python-Algorithom\\7. 동적 계획법\\input.txt"
sys.stdin = open(filePath_desktop, "rt")
n, m = map(int, input().split())
dp = [0]* (m+1)

for i in range(n):
  w, v = map(int, input().split())
  for j in range(w, m+1):
    dp[j] = max(dp[j], dp[j-w]+v)
print(dp[m])