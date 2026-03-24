# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606

from collections import deque

# 입력
n = int(input())
m = int(input())

# 그래프 생성
graph = [[] for _ in range(n + 1)]

# 간선 입력
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n + 1)
count = 0

def bfs(start):
    global count

    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        current = queue.popleft()
        count += 1

        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    
bfs(1)
print(count - 1)