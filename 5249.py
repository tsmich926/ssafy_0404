#그래프-최소비용
#정점을 연결하는 간선들의 합이 최소가 되는 트리
#신장트리
# n개의 정점 무방향그래프 n-1개의 간선
#최소신장트리:가중치의 합이 최소

#가중치의 합구하기


# 탐욕기법-프림,크루스칼,다익스트라



def find_set(x): #x가 속한 집합의 대표
    while x != rep[x]: #대표가 아니면
        x= rep[x] #x==rep[x]까지 반복
    return x

def union(x,y):
    rep[find_set(y)] = find_set(x) #y가 속한 곳의 대표원소를 찾아가봄 x의 대표원소를 가리키도록 바꿈
    rep[y] = find_set(x)

T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split()) #0~V 정점번호, E 간선수
    #makeset()
    rep = [i for i in range(V+1)]
    graph = []
    for  _ in range(E):
        v1,v2,w = map(int,input().split())
        graph.append([v1,v2,w])

        #가중치 기준 오름차순정렬
    graph.sort(key=lambda x:x[2])
    #graph.sort()
    # print(graph)

    # N개 정점(V+1),N-1개의 간선 선택
    N =V+1
    s =  0 #mst에 포함된 간선의 가중치 합
    MST = []
    cnt = 0
    MST = []

    for u,v,w in graph: #가중치가 작은것부터...
        #사이클 확인
        if find_set(u) != find_set(v): #사이클이 생기지 않으면
            cnt += 1
            s += w #가중치합
            MST.append([u,v,w])
            union(u,v)
            if cnt == -1: #MST구성완료
                break
    print(f'#{tc} {s}')




