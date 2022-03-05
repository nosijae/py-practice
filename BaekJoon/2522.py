N = int(input())

for i in range(1, N*2):
    print(' ' * abs(i - N), end='')
    if i > N:
        print('*' * (N * 2 - i))
    else:
        print('*' * i)