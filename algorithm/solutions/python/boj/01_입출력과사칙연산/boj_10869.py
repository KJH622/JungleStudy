# BOJ 10869 - 사칙연산
# 핵심: A와 B를 입력받고 A + B, A - B, A * B, A // B, A % B를 출력한다.

A, B = map(int, input().split())
print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)