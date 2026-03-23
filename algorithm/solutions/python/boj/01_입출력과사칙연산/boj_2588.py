# BOJ 2588 - 곱셈
# 핵심: (세 자리 수) * (세 자리 수)를 구하는 과정을 출력한다.

a = int(input())
b = input()

for i in range(2, -1, -1):
    c = a * int(b[i])
    print(c)

print(a * int(b))