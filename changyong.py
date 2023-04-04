def dfs(v):
    visited[v] =True #방문체크 해줌
    for w in G[v]:  #배열의 원소들도 방문처리 , 
        if not visited[w]: #원소가 미방문이면
            dfs(w) #재귀로 방문해서 원소의 원소까지 방문처리 할 수 있음
                    #처음 들어온 v와 연관된 원소들과 그 원소들의 원소들도 다 방문처리 되는 효과..


T = int(input())
for tc in range(1,T+1): 
    N,M =map(int,input().split()) # 1부터N번까지의 사람존재, M번째 줄에 걸쳐 입력받음

    G = [[] for _ in range(N+1)] #0,1,2,3,4.. N까지의 배열만듬
    visited = [False]*(N+1) #방문체크
    cnt = 0 #무리의 수 0으로 초기화


    for _ in range(M):
        a,b =map(int,input().split()) #서로 알고 있는 사람들..
        G[a].append(b) #
        G[b].append(a)

    for i in range(1, N + 1):
        if not visited[i]:
            dfs(i)  # G배열 i번째 원소들을 다 방문처리 해줌-한묶음으로 묶어주는 효과
            cnt += 1
    print(f'{tc} {cnt}')


#첫번째 tc
    # 0  1     2    3    4     5    6  번째
#G[[0],[2,5],[1,5],[4],[3,6],[2,1],[4]]