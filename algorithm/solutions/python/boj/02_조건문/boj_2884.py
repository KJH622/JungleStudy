# BOJ 2884 - 알람 시계
# 핵심: 45분 일찍 알람 설정하기

h, m = map(int, input().split())

if 45 <= m <= 59:
    print(h, m-45)
else:
    if h == 0:
        print(23, 60-(45-m))
    else:
        print(h-1, 60-(45-m))