cnt_3 = 0
cnt_5 = 0

for i in range(10):
    k = int(input())

    if k%3 == 0:
        cnt_3+=1
    
    if k%5 == 0:
        cnt_5+=1

print(cnt_3, cnt_5)