while True:
    k = int(input())
    if k > 25:
        print('Lower')
    elif k < 25:
        print('Higher')
    else:
        print('Good')
        break