# 트리 - 상근이의 여행 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/9372

T = int(input()) # 테스트 케이스 수

# n = 국가의 수
# m = 비행기 종류

for _ in range(T):
    n, m = map(int, input().split())

    for _ in range(m):
        input()
        
    print(n-1)