n = int(input())

people = [tuple(input().split()) for i in range(n)]


sorted_people = sorted(people,reverse = True, key = lambda x : x[0])

print(f'name {sorted_people[0][0]}')
print(f'addr {sorted_people[0][1]}')
print(f'city {sorted_people[0][2]}')