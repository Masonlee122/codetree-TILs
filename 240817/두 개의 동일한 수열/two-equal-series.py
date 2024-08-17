n = int(input())

lst_a = list(map(int,input().split()))
lst_b = list(map(int,input().split()))

lst_sum = lst_a+lst_b
set_sum = set(lst_sum)

if len(set_sum) == n:
    print("Yes")
else:
    print("No")