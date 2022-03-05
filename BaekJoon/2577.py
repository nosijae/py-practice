A = int(input())
B = int(input())
C = int(input())

multiNum = str(A * B * C)

for i in range(10):
    print(multiNum.count(str(i)))