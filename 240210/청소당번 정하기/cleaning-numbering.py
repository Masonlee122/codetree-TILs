cnt_c = 0
cnt_a = 0
cnt_t = 0

n = int(input())

for i in range(1,n+1):
    if i%12 == 0:
        cnt_t += 1
    elif i%6 ==0:
        cnt_a +=1
    elif i%3 == 0:
        cnt_a +=1
    elif i%2 ==0:
        cnt_c +=1

print(cnt_c,cnt_a,cnt_t)