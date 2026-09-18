import copy

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def in_range(r, c):
    return 0 <= r < N and 0 <= c < N

def can_move(r, c, robot_d):
    pass

def grain_change(new_field):
    pass

def simulation(start_r, start_c, start__d):
    harvest = 0
    day = 1
    rr, rc = start_r, start_c # 로봇 현재 위치

    move = can_move()

    while day <= M:
        # 날이 바뀌면 곡식 변화
        changed_field = grain_change(field)

        # 오전 작업
        # 곡식이 열렸으면
        if changed_field[rr][rc] == 0:
            # 다음 농지로 이동할 수 있으면
            
            # 다음 농지로 이동할 수 없으면

        # 빈 농지면
        # 수확 / 수확량 업데이트

        # 오후 작업
        # 이동 가능하면 이동 / break
        f



        # 작업 끝
        day += 1

    return harvest

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(N)]

    for r in range(1, N - 1):
        for c in range(1, N - 1):
            for d in (0, 1, 2, 3):
                if field[r][c] == 0:
                    max_harvest = max(max_harvest, simulation(r, c, d))
    '''
    기본 일이 지나면
    - 씨 1일 후: 싹
    - 첫번째로 싹: 1 + 3일 후 곡식
    - k번째로 싹: 3 + k일 후 곡식
    
    씨: 1, 싹: 2, 곡식: 3
    
    1. 뭘 선택
    시작점 선택 / 바라보는 방향
    
    1) 오전
    현재 빈 농지에 있고, 다음 농지로 이동 가능? 씨 심기
    빈 농지고, 다음 농지로 이동 불가능? 현재 위치에 머무르기
    곡식이 열린 경우 수확, 수확하면 빈 농지 됨

    2) 오후 - 이동 가능한 곳으로 이동
    이동 가능한 곳은 빈 농지, 곡식이 열린 농지 / 1이거나 싹이면 이동 불가능
    이동 가능한 곳이 여러개면, 가장 먼저 이동 가능한 곳
    이동 불가능하면 머무르기
    3) 다음 낳이 되면 1-2 반복

    
    2. 제약조건
    
    3. 선택하면 뭐가 바뀜
    다음날: 전체 상태가 한 번 바뀜
    오전, 오후
    
    로봇 방향과 농장 상태 한 번 더
    
    4. 최대/최소
    곡식을 가장 많이 수확할 수 있는 시작 위치와 방향 찾고, 수확 횟수 (최댓값) 출력
    
    저 곡식 자라는 걸 어떻게 표현?
    3차원 배열이나
    튜플로 저장해서
    지금 상태, 지금 상태가 변경된 날짜
    변경할 때는 날짜 확인해서 정확히 3 + k일 째일때 바꿔주기

    '''
