N = int(input())

num = N * 2 - 1
for i in range(N):
    print(' ' * i, end='')
    print('*' * (num))
    num -= 2

num += 4
for i in range(1, N):
    print(' '*(N - i -1), end='')
    print('*' * num)
    num += 2