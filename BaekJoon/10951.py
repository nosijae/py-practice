import sys

try:
    while True:
        A, B = map(int, input().split())
        print(A + B)
except EOFError:
    sys.exit()