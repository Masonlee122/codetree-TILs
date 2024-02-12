s = 0
i = 0
while True:
    k = int(input())
    if 20<=k<30 :
        s += k
        i+= 1

    elif k < 20 or k >= 30:
        avg = round(s/i,2)
        print(f'{avg:.2f}')
        break