# 병합정렬 : 왼쪽분할, 오른쪽분할 작업 먼저 수행 후(재귀호출) 합치기 작업 수행 => 후위순회
def divideAndConquerSort(lt, rt):
  if lt < rt:
    mid = (lt+rt) // 2
    divideAndConquerSort(lt, mid) # 왼쪽 분할
    divideAndConquerSort(mid+1, rt) # 오른쪽 분할

    # 두 리스트 합치기(병합)
    tmp = []
    p1 = lt
    p2 = mid + 1
    while p1 <= mid and p2 <= rt:
      if arr[p1] < arr[p2]:
        tmp.append(arr[p1])
        p1 += 1
      else:
        tmp.append(arr[p2])
        p2 += 1
    if p1 <= mid:
      tmp = tmp + arr[p1:mid+1]
    elif p2 <= rt:
      tmp = tmp + arr[p2:rt+1]

    # 정렬된 tmp리스트를 본래의 arr 리스트에 복사하기
    for i in range(len(tmp)):
      arr[lt + i] = tmp[i]



if __name__ == "__main__":
  arr = [23, 11, 45, 36, 15, 67, 33, 21]
  print("Before Sort : ", end = " ")
  print(arr)
  divideAndConquerSort(0, 7)
  print()
  print("After Sort : ", end=" " )
  print(arr) 