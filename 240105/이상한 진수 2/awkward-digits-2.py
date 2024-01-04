a = list(input())

index = 0
for i in a:

    if i == '0' :
        index = a.index(i)

a[index] = '1'
a_str = ''.join(a)
a_b = int(a_str,2)
print(a_b)