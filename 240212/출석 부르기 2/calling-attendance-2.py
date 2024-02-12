student = {
    1 : 'John',
    2 : 'Tom',
    3 :  'Paul',
    4 : 'Sam'
}

while True:
    k = int(input())
    if k <=4 :
        print(student[k])
    else : 
        print('Vacancy')
        break