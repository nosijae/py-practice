while True:
    myStr = input()
    if myStr == '0':
        break

    rvMyStr = myStr[::-1]
    if rvMyStr == myStr:
        print('yes')
    else:
        print('no')