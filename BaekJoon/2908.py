A, B = input().split()
A, B = A[::-1], B[::-1] # 뒤집기

if int(A) > int(B):
    print(A)
else:
    print(B)
