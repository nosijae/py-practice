N = int(input())

num = N * 2 - 1
for i in range(N):
    print(' ' * i, end='')
    print('*' * (num))
    num -= 2
