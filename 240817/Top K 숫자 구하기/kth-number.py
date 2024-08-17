n, k = map(int,input().split())
lst = list(map(int,input().split()))

sorted_lst = sorted(lst)
print(sorted_lst[k-1])