# 최단경로
# 간선의 가중치가 있는 그래프에서
# 간선 가중치의 합이 최소인 경로

# 다익스트라
# 시작정점에서 거리가 최소인 정점을 선택해 나가면서 최단경로 구함


# 5 11
# 0 1 2
# 0 2 4
# 1 2 1
# 1 3 7
# 2 1 1
# 2 3 4
# 2 4 6
# 3 4 2
# 3 5 3
# 4 0 3
# 4 5 6


# 5 8
# 0 1 2
# 0 2 4
# 1 2 1
# 1 3 7
# 2 4 3
# 3 4 2
# 3 5 1
# 4 5 5

def dijkstra(s,V): #s출발에서 V마지막정점 번호
    U = [0]*(V+1) # U 최소비용이 결정된 정점 집합
    U[s] = 1 #U = {s}
    for i in range(V+1): #s에서 정점 i로 가는 비용
        D[i] = adjM[s][i] #D를 초기화하는 작업
    
    
    # while U != V: 남은 정점의 비용 결정
    N = V+1 #N개의 정점
    for _ in range(N-1): #N-1개 정점의 비용 결정
        #D[w]가 최소인 w 결정
        minV = INF
        w = 0
        for i in range(V+1):
            if U[i] ==0 and minV > D[i] : #비용이 확정되지 않은 것 중-남은 정점 i중 최소
                w = i #일단 i를 후보로 둠
                minV = D[i]
        U[w] = 1 #최소 비용 D[w]가 확정됨
        # w에 인접인 정점에 대해, 기존비용과 w를 거쳐가는 비용비교

        for v in range(V+1): #무한대가 아니면 인접
            if 0< adjM[w][v] < INF: #w에 인접인 v의 조건
                D[v] = min(D[v],D[w]+adjM[w][v]) #기존비용과 w를 거쳐가는 비용중 작은것은 min으로 골라줌



INF = 10000 #문제에 따라 조정
V,E =map(int,input().split()) #0~V번 정점 , E간선수
adjM = [[INF]*(V+1) for _ in range(V+1)]
for i in range(V+1):
    adjM[i][i] = 0 #자기자신으로 가는 비용
for _ in range(E):
    u,v,w = map(int,input().split()) #u->v,w 가중치
    adjM[u][v] = w

D =[0]*(V+1)
dijkstra(0,V)
print(D)


