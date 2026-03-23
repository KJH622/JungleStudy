# BOJ 1330 - 두 수 비교하기
# 핵심: A와 B를 입력받고 두 수를 비교한다. (if-eilf-else)

a, b = map(int, input().split())

if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("==")