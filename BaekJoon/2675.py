N = int(input())
rstList = []

for i in range(N):
    num, myStr = input().split()
    rstStr = ''
    for j in myStr:
        rstStr += j * int(num)
        # print(j * int(num), end='')
    rstList.append(rstStr)


for i in range(N):
    print(rstList[i])