import sys
filePath = "C:\\Users\khj77\\OneDrive\\바탕 화면\\Python\\python_Algo_practice\\Python-Algorithom\\3. 탐색&시뮬레이션(string,1차원,2차원 리스트탐색)\\input.txt"
sys.stdin = open(filePath, "rt")

numList = [i for i in range(0, 21)]
for i in range(10):
  a, b = map(int, input().split())
  tmp = numList[a:b+1]
  numList[a:b+1] = tmp[::-1]

for i in range(21):
  if i == 0:
    continue
  else:
    print(numList[i], end=" ")


'''
### 리스트 요소를 뒤집을때 사용하는 reverse와 reversed의 차이 ###
1. [리스트].reverse()
=> 반환값이 없다. 따라서 새로운 리스트 변수에 담을 수 없다.
=> 리스트 함수이므로 리스트에서만 사용가능하다.
=> 기존 리스트 원형을 변경한다.
	ex. a = [1, 2, 3]
			b = a.reverse() #None
      print(b) #None
      print(a) #[3, 2, 1] 출력됨, 원형 리스트 자체가 변경된다.

2. reversed([리스트])
=> 객체 반환값이 있다. 따라서 새로운 리스트 변수에 뒤집은 리스트를 담을 수 있다.
=> 파이썬 내장함수이다. 리스트 뿐만 아니라 딕셔너리, 튜플, 스트링에서도 사용 가능하다.
=> 해당 객체의 원형을 바꾸지 않는다. 새로운 객체 반환값을 넘겨주는 것이다.
	ex. a = [1, 2, 3]
			b = reversed(a)
      print(b) #[3, 2, 1]
      print(a) #[1, 2, 3] 원형 리스트는 변경되지 않는다.
'''
