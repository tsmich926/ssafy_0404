def find_set(x): #x가 속한 집합의 대표
    while x != rep[x]: #대표가 아니면
        x= rep[x] #x==rep[x]까지 반복
    return x

def union(x,y):
    rep[find_set(y)] = find_set(x) #y가 속한 곳의 대표원소를 찾아가봄 x의 대표원소를 가리키도록 바꿈
    rep[y] = find_set(x)

#makeset()
rep = [i for i in range(6)]
print(rep)

