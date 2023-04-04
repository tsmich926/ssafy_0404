#프림 알고리즘
# 6 11
# 0 1 32
# 0 2 31
# 0 5 60
# 0 6 51
# 1 2 21
# 2 4 46
# 2 6 25
# 3 4 34
# 3 5 18
# 4 5 40
# 4 6 51

def prim():
    U = [] #빈거
    D = [1e10]* V #무한대값으로 초기화
    s = [-1]*V

    D[0] = 0 #시작점 선택
    while len(U) < V:
        minV = 1e10
        for i in range(V):
            if i in U:
                continue    #최솟값 구하지 않음
            if minV >  D[i]:
                minV = D[i]
                v = i

        #1 D에서 제일 작은 값인 index(v)를 찾는다.
        # U에 없는 v기준으로

        #2 v를 U에 넣는다
        U.append(v)

        #3 v하고 연결된 w의 D값을 최선으로 수정한다.
        # U에 없는 v기준으로
        for w in range(V):
            if w in U :  continue
            if G[v][w]: #값이 있으면 연결돼 있는거
                D[w] = min(D[w],G[v][w])


    print(D)
    print(U)


V,E =map(int,input().split())
V += 1
G = [[0]*V for _ in range(V) ]
for _ in range(E):
    v1,v2,w =map(int,input().split())
    G[v1][v2] = w
    G[v2][v1] = w

prim()
# print(G)

#결과는 제일 작은 간선들이 나온다



