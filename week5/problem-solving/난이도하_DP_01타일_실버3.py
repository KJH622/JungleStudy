# DP - 01타일 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/1904

# 각각의 타일들은 0 또는 1이 쓰여 있는 낱장의 타일들이다.
# 현재는 1 또는 0을 두 개 붙인 한 쌍의 00타일만이 남게 되었다.

# 보텀업 방식으로 사용할 예정


def fibo(n):

    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 15746
        # 모듈러 연산 : 어떤 수를 특정 수로 나눈 뒤, 그 나머지만 남기는 연산
    
    return dp[n]

n = int(input())
print(fibo(n))