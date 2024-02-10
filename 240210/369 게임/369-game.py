n = int(input())
i = 1

while i <= n:
    str_i = str(i)
    if i % 3 == 0 or '3' in str_i or '6' in str_i or '9' in str_i:
        print(0, end= ' ')

    else:
        print(i, end =' ') 
    
    i+=1