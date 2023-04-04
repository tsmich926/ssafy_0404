
def dijk(V): 
    U = [] #지금까지 계산한 것들을 기록
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

    return D[V - 1]

T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    V += 1
    G = [[0]*V for _ in range(V)]
    for _ in range(E):
        v1,v2,w =map(int,input().split())
        G[v1][v2] = w

    ans = dijk(V)
    print(f'#{tc} {ans}')




