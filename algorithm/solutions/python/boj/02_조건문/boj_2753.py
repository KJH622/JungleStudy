# BOJ 2753 - 윤년
# 핵심: 연도가 주어졌을 때 윤년이면 1, 아니면 0이다. 
#       윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.

year = int(input())

if year % 4 == 0:
    if year % 100 != 0 or year % 400 == 0:
        print(1)
    else:
        print(0)
else:
    print(0)