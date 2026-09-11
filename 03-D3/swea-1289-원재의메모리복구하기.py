'''
초기화 배열

목표 상태

둘이 비교하면서 이차원 배열 사용

만약 같으면 넘어가

아니면
거기부터 반복문 돌면서
뒤에 값 다 덮어씌우기 - 뭘로?
목표 배열 값으로
'''
T = int(input())
for tc in range(1, T+1):
    goal = input()
    N = len(goal)
    reset = [str(0)] * N
    count = 0

    
    for i in range(N):
        print(reset)
        if reset[i] == goal[i]:
            continue

        for j in range(i, N):
            reset[j] = goal[i]

        count += 1

    print(f'#{tc} {count}')
