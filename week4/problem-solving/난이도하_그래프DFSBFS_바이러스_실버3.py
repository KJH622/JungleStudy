# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606

# 이는 DFS로 풀면 될 것 같다. (깊이 우선 탐색)

# 핵심: 1번 컴퓨터와 연결된 모든 컴퓨터 수를 세면 된다.
# 즉, 그래프에서 1번 정점에서 시작해서 방문 가능한 정점 개수를 세면 된다.

# 1번 컴퓨터에서 DFS를 시작해 방문한 모든 컴퓨터 수를 센 뒤, 자기 자신을 제외하기 위해 1을 빼준다.


n = int(input()) # 컴퓨터의 수
m = int(input()) # 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수

# graph[0]은 그냥 비워두는 칸
# graph[1] ~ graph[7]까지
graph = [[] for _ in range(n+1)] # 컴퓨터 번호를 그대로 인덱스로 쓰기 위해서

visited = [False] * (n + 1) # 방문하지 않은 것 : False, 방문한 것 : True

count = 0

# 그래프를 만드는 작업 (양방향)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(graph, start, visited): # 이미 만들어진 그래프를 탐색하는 작업
    global count
    
    # 1. 방문 처리
    visited[start] = True

    # 2. count 증가
    count += 1

    # 3. 연결된 노드들 확인
    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

dfs(graph, 1, visited)

print(count-1)