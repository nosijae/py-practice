N = int(input())

num = 1
for i in range(N):
    print(' '*(N - i -1), end='')
    print('*' * num)
    num += 2

num -= 4
for i in range(N-1):
    print(' ' * (i+1), end='')
    print('*' * (num))
    num -= 2
