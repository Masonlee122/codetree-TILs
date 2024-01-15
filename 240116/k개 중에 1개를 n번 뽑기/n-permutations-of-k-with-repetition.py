def dfs(n,lst):
    #종료 조건
    if n == N:
        return ans.append(lst)
    #하부 함수
    for j in range(1,M+1):
        dfs(n+1,lst+[j])

M, N = map(int,input().split())

ans = []
v = [0]*(N+1)

dfs(0,[])

for i in ans:
    print(*i)