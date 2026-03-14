# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920

# N개의 정수에 X라는 정수가 존재하는지 알아내는 프로그램

import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
arr.sort()

m = int(input())

target = list(map(int, input().split()))

for i in target:
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == i:
            print(1)
            break
        elif arr[mid] > i:
            right = mid - 1
        else:
            left = mid + 1
        
    else:
        print(0)