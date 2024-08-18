n = int(input())
data = [ list(map(str,input().split())) for i in range(n)]

dict_y = {}

for i in range(n):
    k = list(map(str,data[i][0].split('-')))
    k = ''.join(k)
    dict_y[int(k)] = [i,data[i][2]]

sort_dict = dict(sorted(dict_y.items(), key = lambda x : x[0]))

for i in sort_dict.values():
    if i[1] =='Rain':
        print(*data[i[0]])
        break