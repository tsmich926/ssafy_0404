def solve():
    D = [[1e10]*N for _ in range(N)]
    Q = [(0,0)] #너비우선
    D[0][0] = 0

    while Q:
        #브레이크 조건 넣지 않기
        curr,curc = Q.pop(0)
        for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            newr =curr + dr
            newc = curc +dc
            if 0<= newr <N and  0<=newc<N:
                gap = max(1,arr[newr][newc]-arr[curr][curc]+1)
                if D[newr][newc] > D[curr][curc] + gap:
                    D[newr][newc] = min(D[newr][newc],D[curr][curc] + gap)
                    Q.append((newr,newc))

    return D[N-1][N-1]


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [ list(map(int,input().split())) for _ in range(N)]

    ans = solve()
    print(f'#{tc} {ans}')