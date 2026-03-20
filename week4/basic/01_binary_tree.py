"""
[이진 트리 - Binary Tree 기본]

문제 설명:
- 이진 트리의 기본 구조를 구현합니다.
- 각 노드는 최대 2개의 자식(왼쪽, 오른쪽)을 가집니다.
- 전위, 중위, 후위 순회를 구현합니다.
- 각 노드가 최대 2개의 자식 노드(왼쪽, 오른쪽)를 가질 수 있는 트리 구조.

입력:
- 트리 노드들

출력:
- 전위 순회: 루트 → 왼쪽 → 오른쪽
- 중위 순회: 왼쪽 → 루트 → 오른쪽
- 후위 순회: 왼쪽 → 오른쪽 → 루트

예제:
트리 구조:
      1
     / \
    2   3
   / \
  4   5

전위: [1, 2, 4, 5, 3]
중위: [4, 2, 5, 1, 3]
후위: [4, 5, 2, 3, 1]

힌트:
- 재귀로 간단히 구현 가능
- 순회 순서만 다름
"""

# root = Node(10) -> 값이 10인 노드를 만들고 그 노드를 root가 가리킨다.
# root.left = Node(5) -> 값이 5인 노드를 새로 만들어서, root의 왼쪽 자식으로 연결한다.

# 높이(height) : 트리가 얼마나 높이 뻗어 있는지
# 깊이(depth) : 위에서 아래로 얼마나 내려왔는지

class TreeNode:
    """이진 트리 노드"""
    def __init__(self, value):
        self.value = value # 값 하나 저장
        self.left = None # 왼쪽 자식은 아직 없음
        self.right = None # 오른쪽 자식은 아직 없음

def preorder(root):
    """전위 순회: 루트 → 왼쪽 → 오른쪽"""
    result = []
    
    # TODO: root가 None이면 빈 리스트 반환
    if root is None:
        return result
    
    # TODO: 루트 값 추가
    result.append(root.value)
    
    # TODO: 왼쪽 서브트리 순회
    result.extend(preorder(root.left))
    
    # TODO: 오른쪽 서브트리 순회
    result.extend(preorder(root.right))
    
    return result

def inorder(root):
    """중위 순회: 왼쪽 → 루트 → 오른쪽"""
    result = []
    
    # TODO: root가 None이면 빈 리스트 반환
    if root is None:
        return result
    
    # TODO: 왼쪽 서브트리 순회
    result.extend(inorder(root.left))
    
    # TODO: 루트 값 추가
    result.append(root.value)
    
    # TODO: 오른쪽 서브트리 순회
    result.extend(inorder(root.right))
    
    return result

def postorder(root):
    """후위 순회: 왼쪽 → 오른쪽 → 루트"""
    result = []
    
    # TODO: root가 None이면 빈 리스트 반환
    if root is None:
        return result
    
    # TODO: 왼쪽 서브트리 순회
    result.extend(postorder(root.left))
    
    # TODO: 오른쪽 서브트리 순회
    result.extend(postorder(root.right))
    
    # TODO: 루트 값 추가
    result.append(root.value)
    
    return result

# 테스트 케이스
if __name__ == "__main__":
    # 트리 생성:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print("=== 이진 트리 순회 ===")
    print(f"전위 순회: {preorder(root)}")
    print(f"중위 순회: {inorder(root)}")
    print(f"후위 순회: {postorder(root)}")

