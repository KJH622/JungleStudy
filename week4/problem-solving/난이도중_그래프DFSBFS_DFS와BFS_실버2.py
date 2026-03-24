# 그래프, DFS, BFS - DFS와 BFS (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1260

# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.

# n = 정점의 개수, m = 간선의 개수, v = 탐색을 시작할 정점의 번호

from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)] # 정점의 번호를 그대로 인덱스에 쓰기 위해서

visited_dfs = []
visited_bfs = []

order = []

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 작은 번호부터 먼저 방문해야 하므로 
for i in range(1, n + 1):
    graph[i].sort()

# DFS로 수행
def dfs(graph, start, visited_dfs=None):

    visited_dfs.append(start)

    for neighbor in graph[start]:
        if neighbor not in visited_dfs:
            dfs(graph, neighbor, visited_dfs)
    
    return visited_dfs

# BFS로 수행
def bfs(start, visited_bfs):

    queue = deque()
    queue.append(start)
    visited_bfs.append(start)

    while queue:
        current = queue.popleft()
        order.append(current)

        for neighbor in graph[current]:
            if neighbor not in visited_bfs:
                queue.append(neighbor)
                visited_bfs.append(neighbor)
    
    return order

result_dfs = dfs(graph, v, visited_dfs)
result_bfs = bfs(v, visited_bfs)

print(*result_dfs)
print(*result_bfs)
# *는 리스트(또는 튜플)의 원소를 하나씩 풀어서 전달한다는 의미이다.