# 배열 중 해당하는 정수 개수 세기

# https://www.acmicpc.net/problem/10807

# 1번째 방법

n = int(input()) # 정수의 개수
arr = list(map(int, input().split())) # 배열
v = int(input()) # 찾으려고 하는 정수

print(arr.count(v)) # arr 안에서 v가 나온 횟수

# 2번째 방법

'''
n = int(input())
data = list(map(int, input().split()))
v = int(input())

count = 0
for i in range(len(data)):
    if v == data[i]:
        count += 1

print(count)
'''