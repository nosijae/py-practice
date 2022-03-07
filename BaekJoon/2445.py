N = int(input())


for i in range(1, N * 2 + 1):
    if i <= N:
        print('*' * i, end='')
        print(' ' * (N - i) * 2, end='')
        print('*' * i)
    else:
        print('*' * (2 * N - i), end='')
        print(' ' * (i - N) * 2, end='')
        print('*' * (2 * N - i))

