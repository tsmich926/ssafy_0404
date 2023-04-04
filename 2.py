def make_set(x): #빈거 만들기
    p[x]=x
    rank[x] = 0 #깊이는 자기자신


#대표를 찾는 작업
def find_set(x):
    while p[x] != x:
        x =p[x]
    return x


# def find_set(x):
#     if x==p[x]:
#         return x
#     return find_set(p[x])

def union(x,y):
    # xp =find_set(x)
    # yp =find_set(y)
    # p[yp]=xp
    # p[find_set(y)] = find_set(x)
    
    xp =find_set(x)
    yp = find_set(y)
    if rank[xp] == rank[yp]:
        p[yp] = xp
        rank[xp] += 1 #랭크 조정
    elif rank[xp] < rank[yp]: #깊이가 더 깊으면 걔를 부모로 만든다
        p[xp] = yp
    else:
        p[yp] = xp
        


V = 6
p = [-1]*V
rank = [0]*V
for i in range(V):
    make_set(i)

print(p)
union(2,3)
union(4,5)
print(p)
print(find_set(3))
print(find_set(5))
union(3,5) #부모바꾸기
print(find_set(5))
print(p)

