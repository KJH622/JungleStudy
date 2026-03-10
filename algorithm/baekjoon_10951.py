'''
try:
    실행할 코드
  except:
    예외가 발생할 때 실행할 코드
'''

# https://www.acmicpc.net/problem/10951

while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break