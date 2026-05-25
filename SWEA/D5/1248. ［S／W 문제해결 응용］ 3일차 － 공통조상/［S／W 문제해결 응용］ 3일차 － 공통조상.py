T = int(input())

for t in range(1, T + 1):
    # V: 정점 개수, E: 간선 개수, n1, n2: 공통 조상을 찾을 두 정점
    V, E, n1, n2 = map(int, input().split())
    
    # 트리 관계를 저장할 배열
    parent = [0] * (V + 1)
    left = [0] * (V + 1)
    right = [0] * (V + 1)
    
    # 간선 정보 입력 처리
    edge_data = list(map(int, input().split()))
    for i in range(0, len(edge_data), 2):
        p = edge_data[i]
        c = edge_data[i+1]
        
        parent[c] = p
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    # n1의 모든 조상 노드를 루트(1)까지 찾아 리스트에 저장
    n1_ancestors = []
    curr = n1
    while curr != 0:
        n1_ancestors.append(curr)
        curr = parent[curr]

    # n2의 조상을 거슬러 올라가면서 처음 겹치는 노드(LCA) 찾기
    lca = 0
    curr = n2
    while curr != 0:
        if curr in n1_ancestors:
            lca = curr
            break
        curr = parent[curr]

    # 함수(재귀) 대신 큐(리스트)를 활용한 반복문으로 서브 트리 크기 구하기
    sub_tree_size = 0
    queue = [lca]
    
    while queue:
        node = queue.pop(0)
        sub_tree_size += 1
        
        if left[node] != 0:
            queue.append(left[node])
        if right[node] != 0:
            queue.append(right[node])

    print(f"#{t} {lca} {sub_tree_size}")