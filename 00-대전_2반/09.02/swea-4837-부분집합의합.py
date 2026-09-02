# 부분집합
# - permutation에서 모든 순열의 경우
# 각 depth에 대해서 선택하고 안 하고 하면서 내려가기


def perm(depth): # depth - 현재 원소, 지금까지 선택한 원소들의 합
    global count

    if depth == 13:
        if len(pick_numbers) == N and sum(pick_numbers) == K:
            count += 1
        return

    perm(depth + 1)

    pick_numbers.append(depth)
    perm(depth + 1)
    pick_numbers.pop()

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = [num for num in range(1, 13)]
    pick_numbers = []
    count = 0
    perm(1)
    print(f'#{tc} {count}')