T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    #트리를 리스트로 표현
    #0번인덱스는 사용하지 않으므로 +1, 
    #자식노드가 하나인 경우, 리프노드를 채우는 방식에서 out of range가 발생할 수 
    #있기 때문에 +1, 총 +2
    Tree = [0] * (N+2)
    
    # 리프 노드를 채움
    for _ in range(M):
        leaf_num, leaf_data = map(int, input().split())
        Tree[leaf_num] = leaf_data

    # 리프 노드가 아닌 노드의 값을 채움
    for i in range(N-M, 0, -1):
        Tree[i] = Tree[i*2] + Tree[i*2+1]
        if i == L:
            break
    
    print(f'#{tc} {Tree[L]}')