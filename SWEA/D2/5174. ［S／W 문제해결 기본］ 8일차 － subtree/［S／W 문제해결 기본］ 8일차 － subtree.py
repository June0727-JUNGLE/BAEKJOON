T = int(input())

def count_nodes(node):
    count = 1  # 현재 자기 자신을 포함하여 1부터 시작
    
    # 자식 노드들이 있다면 각각을 루트로 하는 서브 트리 개수를 더함
    for child in tree[node]:
        count += count_nodes(child)
    
    return count

for tc in range(1, T+1):
    E, N = map(int, input().split())

    tree = [[] for _ in range(E + 2)]  # 노드 번호는 1부터 시작하므로 E+1, 그리고 자식 노드가 하나인 경우를 대비하여 +1

    edges = list(map(int, input().split()))
    for i in range(0, len(edges), 2): #2칸씩 건너뛰면서 기록
        parent = edges[i]
        child = edges[i+1]
        tree[parent].append(child)

    result = count_nodes(N)
    print(f'#{tc} {result}')
    