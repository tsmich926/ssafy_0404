# T = int(input())
# for tc in range(1,T+1):
#     N,M = map(int,input().split())
#     arr = list(map(int,input().split()))
#     #make_Set 대신해서
#     P = [i for i in range(N+1)]
#
#     for idx in range(M):
#         v1 = arr[idx*2]
#         v2 = arr[idx*2+1]
#         union(v1,v2)
#
#


def dfs(v):
    visited[v] =True
    for w in G[v]:
        if not visited[w]:
            dfs(w)

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    G = [[] for _ in range(N+1)]
    visited = [False]*(N+1)
    cnt = 0
    for i in range(M):
        v1 = arr[i*2]
        v2 = arr[i*2+1]
        G[v1].append(v2)
        G[v2].append(v1)

    for i in range(1,N+1):
        if not visited[i]:
            dfs(i)
            cnt += 1
    print(f'{tc} {cnt}')

