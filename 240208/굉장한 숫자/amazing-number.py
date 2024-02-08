a = int(input())

if a %2 == 1 and a%3 ==0:
    print('true')
elif a%2 == 0 and a%5 == 0:
    print('true')
else:
    print('false')