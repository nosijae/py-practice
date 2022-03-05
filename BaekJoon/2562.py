maxNum = 0
idx = 0
for i in range(9):
    num = int(input())
    if maxNum < num:
        idx = i+1
        maxNum = num

print(maxNum)
print(idx)