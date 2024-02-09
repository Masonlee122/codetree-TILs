person_1 = list(input().split())
person_2 = list(input().split())
person_3 = list(input().split())

lst = [person_1,person_2,person_3]
cnt = 0

for i in lst:
    if i[0] == 'Y' and int(i[1]) >= 37:
        cnt+=1
    

if cnt >=2 :
    print('E')
else:
    print('N')