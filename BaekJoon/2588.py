# store mid rst
rstList = []

A = input()
B = input()

digit = 1
for i in range(len(B) - 1, -1, -1):
    print(int(A) * int(B[i]))
    rstList.append(int(A) * int(B[i]) * digit)
    digit *= 10

print(sum(rstList))
