# BOJ 14681 - 사분면 고르기
# 핵심: 점의 좌표를 입력받아 그 점이 어느 사분면에 속하는지 알아낸다.

x = int(input())
y = int(input())

if x > 0:
    if y > 0:
        print(1)
    elif y < 0:
        print(4)
elif x < 0:
    if y > 0:
        print(2)
    elif y < 0:
        print(3)