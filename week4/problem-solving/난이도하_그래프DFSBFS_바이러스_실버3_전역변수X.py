# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606

# 1. 입력
n = int(input())
m = int(input())

# 2. 그래프 생성
graph = [[] for _ in range(n + 1)]

# 3. 간선 입력
for _ in range(m):
    x, y = map(int, input().split())
    # 양방향 연결 저장
    graph[x].append(y)
    graph[y].append(x)

# 4. 방문 배열
visited = [False] * (n + 1)

# 5. DFS 함수
def dfs(graph, start, visited):
    # 현재 노드 방문 처리
    visited[start] = True

    # 현재 노드 포함해서 개수 1로 시작
    total = 1

    # 연결된 노드들 확인
    for neighbor in graph[start]:
        # 아직 방문 안 했다면
        # total에 dfs 결과 더하기
        if not visited[neighbor]:
            total += dfs(graph, neighbor, visited)

    return total

# 6. 탐색 시작
result = dfs(graph, 1, visited)

# 7. 1번 제외하고 출력
print(result - 1)