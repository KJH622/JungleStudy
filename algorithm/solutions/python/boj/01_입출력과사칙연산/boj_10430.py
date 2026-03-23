# BOJ 10430 - 나머지
# 핵심: A, B, C를 입력받고 나머지 구하는 식을 통해 출력한다.

A, B, C = map(int, input().split())

print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)