n = int(input())

lst = list(map(int,input().split()))
lst.sort()

lst1 = lst[0:n]
lst2 = lst[n:2*n]
lst2.sort(reverse=True)

max_sum = 0 

for i in range(n):
    s = lst1[i]+lst2[i]
    if s > max_sum:
        max_sum= s

print(s)