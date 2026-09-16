'''
정사각형 안에 K개의 미생물 군집이 있음
N * N 정사각형 셀
가장자리들은 약품이 칠해져 있음
셀이 있을 수 있는 범위 (1, N - 1), (1, N - 1)

1.
최초 미생물 군집의 위치, 군집 내 미생물 수, 이동 방향(상하좌우 중 하나)
2.
각 군집들은 1시간마다 이동 방향에 있는 다음 셀로 이동
3.
약품이 칠해진 셀에 도착: 절반이 죽고 이동 방향이 반대로 바뀜
미생물 수가 홀수면 미생물 수 // 2
미생물이 한 마리 있는 경우, 군집이 사라지게 됨
4.
이동 후 두 개 이상의 군집이 한 셀에 모이는 경우 군집이 합쳐지게 됨
미생물 수는 두 군집의 합, 이동 방향: 미생물이 더 많은 군집의 이동방향
(같은 경우는 고려 x)

M 시간 동안 격리 후 남아 있는 미생물 수의 총합

10      
7 2 9   
1 1 7 1 
2 1 7 1
5 1 5 4
3 2 8 4 
4 3 14 1
3 4 3 3 
1 5 8 2 
3 5 100 1
5 5 1 1

'''

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
reverse = [1, 0, 3, 2]

def in_range(r, c):
    return 1 <= r < N - 1 and 1 <= c < N - 1

def simulation():
    time = 0
    while time < M:
        for i in range(len(microbiome) - 1, -1, -1):
            cr, cc, microbial_count, dir = microbiome[i]
            nr, nc = cr + dirs[dir][0], cc + dirs[dir][1]

            if not in_range(nr, nc):
                dir = reverse[dir]
                microbial_count //= 2

            microbiome[i] = nr, nc, microbial_count, dir

        groups = {}
        for i in range(len(microbiome)):
            if not microbiome[i][2]:
                continue

            r, c = microbiome[i][:2]
            groups.setdefault((r, c), []).append(i)

        new_microbiome = []
        for idxs in groups.values():
            if len(idxs) == 1:
                idx, = idxs
                new_microbiome.append(microbiome[idx])
                continue

            r, c = microbiome[idxs[0]][:2]
            total_count = sum(microbiome[idx][2] for idx in idxs)
            max_idx = max(idxs, key=lambda idx: microbiome[idx][2])
            new_dir = microbiome[max_idx][3]

            new_microbiome.append((r, c, total_count, new_dir))

        microbiome[:] = new_microbiome
        time += 1

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    microbiome = []
    for _ in range(K):
        r, c, microbes, dir = map(int, input().split())
        dir -= 1
        microbiome.append((r, c, microbes, dir))

    simulation()
    print(f'#{tc} {sum(microbes for _, _, microbes, _ in microbiome)}')