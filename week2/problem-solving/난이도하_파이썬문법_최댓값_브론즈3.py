# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562

lst = []

for _ in range(9):
    n = int(input())
    lst.append(n)

print(max(lst))

print(lst.index(max(lst)) + 1)