while True:
    lst_sqr = list(input().split())
    width = int(lst_sqr[0])
    length = int(lst_sqr[1])
    print(width*length)
    if lst_sqr[2] == 'C':
        break