# 퀵소트: 전위순회, 리스트의 가장 마지막 값을 pivot으로 설정
#  pivot 기준으로 왼쪽은 pivot 보다 작은 값들로, 오른쪽은 pivot보다 큰 값으로 분리(partition) 먼저 수행 후, 왼쪽과 오른쪽 분할(재귀호출)작업 수행 
def quickSort(lt, rt):
  if lt < rt:
    # pivot기준으로 pivot앞쪽은 pivot보다 작은값으로, pivot 뒤쪽은 pivot보다 큰 값으로 분리(partition)
    pos = lt
    pivot = arr[rt]
    for i in range(lt, rt):
      if arr[i] < pivot:
        arr[i], arr[pos] = arr[pos], arr[i]
        pos += 1
    arr[rt], arr[pos] = arr[pos], arr[rt] # pivot과 arr[pos]를 swap

    # pivot 기준으로 왼쪽과 오른쪽 부분 분할(재귀호출) 작업
    quickSort(lt, pos-1)
    quickSort(pos+1, rt)


if __name__ == "__main__":
  arr = [23, 11, 45, 36, 15, 67, 33, 21]
  print("Before Sort : ", end = " ")
  print(arr)
  quickSort(0, 7)
  print()
  print("After Sort : ", end=" " )
  print(arr) 