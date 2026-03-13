# 오븐 시계

# https://www.acmicpc.net/problem/2525

a, b = map(int, input().split()) # a(시) b(분)
c = int(input()) # c: 요리하는 시간

a += (b+c) // 60
b = (b+c) % 60

if a >= 24:
    a -= 24

print(a, b)