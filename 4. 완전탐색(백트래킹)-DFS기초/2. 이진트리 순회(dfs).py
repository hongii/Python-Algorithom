# 전위순회 출력 => 깊이 우선 탐색에서 재귀 호출 전에 부모노드 print 먼저하고, 왼쪽 자식과 오른쪽 자식을 호출한다.
def dfs_preorder(v):
  if v > 7:
    return
  else:
    print(v, end=" ") #부모(현재)노드
    dfs_preorder(v*2)  # 왼쪽 자식 노드
    dfs_preorder(v*2+1)  # 오른쪽 자식 노드


# 중위순회 출력 => 깊이 우선 탐색에서 왼쪽 자식먼저 호출하고 그 다음 부모노드를 print하고 오른쪽 자식을 호출한다.
def dfs_inorder(v):
  if v > 7:
    return
  else:
    dfs_inorder(v*2)
    print(v, end=" ")
    dfs_inorder(v*2+1)


# 후위순회 출력(ex. 병합정렬) => 깊이 우선 탐색에서 왼쪽 자식과 오른쪽 자식 먼저 호출하고 마지막에 부모노드를 print한다.
def dfs_postorder(v):
  if v > 7:
    return
  else:
    dfs_postorder(v*2)
    dfs_postorder(v*2+1)
    print(v, end=" ")


if __name__ == '__main__':
  dfs_preorder(1)
  dfs_inorder(1)
  dfs_postorder(1)