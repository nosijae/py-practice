rstList = []

for i in range(10):
    num = int(input())
    num %= 42
    if num not in rstList:
        rstList.append(num)

print(len(rstList))