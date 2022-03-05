N = int(input())

nums = list(map(int, input().split()))
newNums = []

M = max(nums)
for i in range(N):
    newNum = nums[i]/M * 100
    newNums.append(newNum)

print(sum(newNums)/len(newNums))
