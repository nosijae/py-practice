N = int(input())

num = 1
for i in range(N):
    print(' '*(N - i -1), end='')
    print('*' * num)
    num += 2