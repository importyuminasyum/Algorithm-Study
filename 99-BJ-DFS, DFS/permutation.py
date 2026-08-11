def permutation(N, R):
    # N: 총 노드 개수
    # R: 연결된 노드 개수 (선택할 노드 개수)
    # 출력은 경우의 수인데 노드를 R 개수 만큼 출력
    # 가능한 경우의 수를 리스트로?
    while R != 0:
        for node in range(1, N+1):
            for _ in range(1, R+1):
                return node, permutation(N-1, R-1)
            
permutation(5, 2)