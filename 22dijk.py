# 방향그래프를 기준으로
#다익스트라

# 5 8
# 0 1 2
# 0 2 4
# 1 2 1
# 1 3 7
# 2 4 3
# 4 3 2
# 3 5 1
# 4 5 5

def dijk():
    U = []
    D = [1e10]*V


    D[0] = 0
    while len(U) < V:
        minV =1e10
        #D중 제일 작은 v를 선택
        for i in range(V):
            if i in U: continue
            if minV > D[i]:
                minV = D[i]
                v= i
        #U에 v를 추가
        U.append(v)
        # D를 갱신
        for w in range(V):
            if w in U:continue
            if G[v][w]:
                D[w] = min(D[w], D[v] + G[v][w])
    print(D)
    print(U)


V,E = map(int,input().split())
V += 1
G = [[0]*V for _ in range(V)]
for _ in range(E):
    v1,v2,w =map(int,input().split())
    G[v1][v2] = w

dijk()
