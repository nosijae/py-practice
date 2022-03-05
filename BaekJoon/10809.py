myStr = input()
# ASCII a == 97, z == 122

for i in range(97, 123):
    print(myStr.find(chr(i)), end=' ')