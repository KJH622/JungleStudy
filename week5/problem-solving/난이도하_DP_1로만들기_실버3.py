# DP - 1로 만들기 (실버 3)
# 문제 링크: https://www.acmicpc.net/problem/1463

# 작은 수들의 정답을 이용해서 큰 수의 정답을 만들 수 있다.
# dp[x] : x를 1로 만드는 최소 연산 횟수
# dp[x] = (한 번 움직인 것 1회) + (도착한 작은 숫자의 최소 횟수)



def make_one(n):

    if n == 1:
        return 0

    dp = [0] * (n + 1)
    dp[1] = 0

    for i in range(2, n+1):
        # 1을 빼는 경우
        dp[i] = dp[i-1] + 1
        
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3]+1)
        
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2]+1)
    
    return dp[n]

n = int(input())

print(make_one(n))
