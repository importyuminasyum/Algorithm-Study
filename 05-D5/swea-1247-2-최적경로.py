
'''
perm
해야할 것
모든 좌표에 대해서 좌표 길이 ** 2 크기의 배열 만들어서 거리 구해놓기

perm으로 경로 뽑기
'''
from itertools import permutations

def cal_min_length():
    global result

    for perm in permutations(range(1, N + 1), N):

        min_length = distance[0][perm[0]]
        for i in range(1, len(perm)):
            min_length += distance[perm[i - 1]][perm[i]]
        min_length += distance[perm[-1]][-1]
        result = min(min_length, result)
    return
            

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rcs = list(map(int, input().split()))
    pairs = []
    
    for i in range(0, 2 * (N + 2), 2):
        pairs.append((rcs[i], rcs[i + 1]))

    home = pairs.pop(1)
    pairs.append(home)

    result = float('inf')

    distance = [
        [0] * (N + 2)
        for _ in range(N + 2)
    ]

    for row in range(N + 2):
        for col in range(N + 2):
            distance[row][col] = abs(pairs[row][0] - pairs[col][0]) + abs(pairs[row][1] - pairs[col][1])

    cal_min_length()

    print(f'#{tc} {result}')
