a ,b = map(int,input().split())

bmi = (100**2)*b/a**2

print(int(bmi))
if bmi >= 25:
    print('Obesity')