N = int(input())

for i in range(N):
    num, myStr = input().split()
    for j in myStr:
        print(j * int(num), end='')


