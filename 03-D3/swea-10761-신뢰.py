'''
B 2 O 1 O 2 B 4
버튼을 누르려면 순서대로여야 하니까
일단 앞에서 확인
b 위치: 1
o 위치: 1

b - 2 눌러라
1초 b += 1 
- i인덱스 다음 인덱스를 봣을때

2초 b 버튼
o - 1 눌러라
3초 o 버튼 / b += 1
o - 2 눌러라
4초 o += 1

b 2
o 1
o 2
b 4

i
b:1, o:1
0
2 - 1 + 1: 2
b: 2, o: 1
누적 2
1
1 - 1 + 1: 1
b:2, o: 1
누적 3
2
2 - 1 + 1: 2
b:2, o: 2
누적 5

방금 추가한 시간이랑 - (현재 목표 위치 - (현재 목표 위치 - 이전위치)) + 1
누적시간과 - 이전 위치의 절댓값

b:5
1, 1
5, 1
5 - 1 + 1: 5
5
b:8
5, 1
8, 1
8 - 5 + 1: 4
9
o:100
8, 1
8, 100
목표 위치 - 이전 로봇 위치
누적 시간 - 이전 로봇 누적 시간
여기서 9는? 0은?
100 - 1 - (9 - 0)
음수가 아님
90
9 + 90 + 1

o:100

방금 추가한 시간 + 이전위치의 절댓값 + 1
이전위치의 절댓값

2 - (4 - 2) + 1: 1
b:4, o:2
누적 6

arr = [[b, 2], [o, 1], [o, 2], [b, 4]]
cur_cum = {'B': 1, 'O': 1}
o_num, b_num = 1, 1


for i in range(N):
    # 목표 로봇 이름, 목표 버튼 위치
    robot = arr[i][0]
    button = arr[i][1]
    # 추가해야 할 시간: 이동거리 + 버튼 누르는 시간
    add_time = abs(button - cur_num[robot])
    
    # 첫번째 경우
    if i == 0 :
        # 그 시간만큼 추가해주기
        total_time += add_time + 1
    # 이전과 지금의 로봇이 다르면
    elif robot != prev_robot:
        # 추가 시간 고려: 방금 추가한 시간에서 이번 총 추가 시간 빼기
        extra_time = prev_time - add_time
        # 추가한 시간보다 이번에 추가할 시간이 더 많으면 그 차이 만큼 추가해주기
        # 그 다음 버튼 누르는 시간 추가
        if extra_time < 0:
            total_time += -extra_time
        total_time += 1
    # 이전과 지금 로봇이 같으면

    else:
        total_time += add_time + 1

    # 대상 로봇 위치 갱신
    cur_num[robot] = button
    # 방금 이동한 로봇 마킹
    prev_robot = robot
    # 방금 추가한 시간 (이동 + 버튼)
    prev_time = add_time + 1



지금 목표 로봇이 직전 이동한 로봇과 같을 때
- 방금 로봇 위치에서 지금 목표 로봇으로 가기 위한 거리 + 1(버튼): 추가 소요 시간
- 추가 소요 시간을 누적 총 소요 시간에 추가

지금 목표 로봇이 직전 이동한 로봇과 다를 때
- 방금 추가 소요 시간과 abs(지금 목표 로봇 위치 - 지금 목표 로봇으로 가기 위한 거리) 간의 차이 + 1(버튼): 추가 소요 시간
- 추가 소요 시간을 누적 총 소요 시간에 추가
목표 위치 - 이전 로봇 위치
누적 시간 - 이전 로봇 누적 시간

'''


T = int(input())
for tc in range(1, T+1):
    text = input().split()
    arr = []
    N = int(text[0])
    total_time = 0

    cur_num = {'B': 1, 'O': 1}
    cur_prev_num = {'B': 1, 'O': 1}
    cur_time = {'B': 0, 'B': 0}
    cur_prev_time = {'B': 0, 'O': 0}

    for i in range(1, N * 2 + 1, 2):
        arr.append((text[i], int(text[i + 1])))
    
    for i in range(N):
        # 목표 로봇 이름, 목표 버튼 위치
        robot = arr[i][0]
        button = arr[i][1]
        
        # 추가해야 할 시간: 이동거리 + 버튼 누르는 시간
        add_move_time = abs(button - cur_prev_num[robot])
        button_time = 1

        # 첫번째 경우
        if i == 0 :
            # 그 시간만큼 추가해주기
            total_time += add_move_time + button_time

        # 이전과 지금의 로봇이 다르면
        elif robot != prev_robot:
            # 추가 시간 고려: 누적 시간에서 이번 총 추가 시간 빼기
            extra_time = add_move_time - (total_time - cur_prev_time[robot])

            # 추가한 시간보다 이번에 추가할 시간이 더 많으면 그 차이 만큼 추가해주기
            # 그 다음 버튼 누르는 시간 추가
            if extra_time > 0:
                total_time += extra_time

            total_time += button_time
            
        # 이전과 지금 로봇이 같으면
        else:
            total_time += add_move_time + button_time

        # 대상 로봇 위치 갱신
        cur_num[robot] = button
        cur_prev_num[robot] = cur_num[robot]
        cur_time[robot] = add_move_time + button_time
        cur_prev_time[robot] = cur_time[robot]

        # 방금 이동한 로봇 마킹
        prev_robot = robot

    print(f'#{tc} {total_time}')