def dfs(start):
    #종료 조건
    global cnt
    if start >= n:
        if start == n :
            cnt+=1
        return
    #하부 함수
    if n-start >=1 :
        dfs(start+1)
    if n-start >=2 :
        dfs(start + 2)
    if n-start >=3 :
        dfs(start + 3)
    if n-start >=4 :
        dfs(start + 4)

cnt = 0

n = int(input())

dfs(0)
print(cnt)