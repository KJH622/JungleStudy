# 45분 일찍 알람 설정하기

# https://www.acmicpc.net/problem/2884

h, m = map(int, input().split())

if 45 <= m <= 59:
    print(h, m-45)
else:
    if h == 0:
        print(23, (60+(m-45)))
    else:
        print(h-1, (60+(m-45)))