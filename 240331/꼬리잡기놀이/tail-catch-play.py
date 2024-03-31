def dfs(r,c,n,t_lst):
    global tails
    if n == 3:
        tails.append(t_lst)
        return

    for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
        nr,nc = dr+r , dc+c
        if 0<=nr<N and 0<=nc<N and v[nr][nc] == False and g[nr][nc] == 2 or g[nr][nc] == 3 :
            v[nr][nc] = True
            dfs(nr,nc,g[nr][nc],t_lst+[(nr,nc)])

def haed_move(head):
    r , c = head[0], head[1]
    for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
        nr,nc = dr+r , dc+c
        if 0<=nr<N and 0<=nc<N and g[nr][nc] == 4:
            head = (nr,nc)
            return head

def tail_move(head,head_di,tail : list):
    if head_di == 0:
        tail.pop()
        tail = [head] +tail
        return tail

    elif head_di == -1:
        tail.pop(0)
        tails.append(head)
        return tail




def shoot(k):
    m, n = int(k//N) , int(k%N)
    d = int(m%4)
    # print(m,n,d)
    ball = []
    if d == 0:
        for i in range(N):
            ball.append((n_list[n],i))
        return ball

    elif d == 1:
        for i in range(N-1,-1,-1):
            ball.append((i,n_list[n]))
        return ball

    elif d == 2 :
        for i in range(N-1,-1,-1):
            ball.append((n_list[n-1],i))
        return ball
    elif d == 3 :
        for i in range(N):
            ball.append((i,n_list[n-1]))
            return ball


def circulata(ball,tail : list,head_di):
    global score , is_move
    seq = 0
    for i in ball:
        # print(i, tail)
        if i in tail:
            seq = tail.index(i)
            break

    if seq == 0 :
        is_move.append(False)
        return

    if head_di == 0:
        score += (seq+1)**2
        is_move.append(True)
        return

    elif head_di == -1:
        score += (len(tail) - seq)**2
        is_move.append(True)
        return

def is_head_move(head_id, is_move, head, tail):
    # print(tail,"ismove 시")
    # print(is_move, "과ㅆ")
    if is_move == False:
        # print(head_id,head)
        return head_id, head

    elif is_move == True:
        if head_id == 0:

            head_id = -1
            head = tail[-1]
            # print(head_id, head)
            return head_id, head
        else:
            print(tail)
            head_id =0
            head = tail[0]
            # print(head_id, h
            return head_id, head










N,M, K = map(int,input().split())

n_list = [N-1]


for i in range(N-1):
    n_list.append(i)



tails = []

g = [list(map(int,input().split())) for _ in range(N)]

v = [[False]*N for _ in range(N)]
## 꼬리 위치 찾기
for i in range(N):
    for j in range(N):
        if g[i][j] == 1:
            dfs(i,j,1,[(i,j)])

dfs(0,0,1,[])


# 각 헤드 리스트를 만들어
heads = []

for row in tails:
    heads.append(row[0])

heads_di = [0]*M
# 전체 tail 움직이기 // head 방향??
# 맞는 지 확인하고 점수 넣고 맞으면 head 바꿔주기


# 턴 마다 돌면서 움직이고 공 쏘고 점수 계산하고 방향 바꾸기
score = 0


for k in range(K):
    is_move = []
    heads = list(map(haed_move,heads))
    new_tails =[]


    for l in range(M):
        tail = tail_move(heads[l],heads_di[l],tails[l])
        new_tails.append(tail)


    tails = new_tails

    # 공 위치 리스트
    balls = shoot(k+1)

    # 각 꼬리의 돌면서 결과 계산하기
    for j in range(M):
        circulata(balls,tails[j],heads_di[j])

    for o in range(M):
        heads_di[o] , heads[o] = is_head_move(heads_di[o],is_move[o],heads[o],tails[o])




print(score)