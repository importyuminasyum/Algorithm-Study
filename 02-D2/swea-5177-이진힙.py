T = int(input())
for tc in range(1, T+1):
    N = int(input())
    heap = [0]
    nodes = list(map(int, input().split()))

    for node in nodes:
        heap.append(node)

        child = len(heap) - 1

        while child > 1:
            parent = child // 2

            if heap[parent] <= heap[child]:
                break

            heap[parent], heap[child] = heap[child], heap[parent]
            child = parent

    child = len(heap) - 1
    answer = 0
    
    while child != 1:
        parent = child // 2

        answer += heap[parent]
        child = parent

    print(f'#{tc} {answer}')


