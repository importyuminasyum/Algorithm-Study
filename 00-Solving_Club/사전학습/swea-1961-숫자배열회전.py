# SWEA 1961. 숫자 배열 회전
# Algorithm: Matrix Rotation (행렬 회전)
# 회전 함수를 하나 만들어 90도 회전을 반복하여 180도, 270도 생성

# 90도 시계 방향 회전 함수
def rotate(arr):
    N = len(arr)

    # 회전된 결과를 저장할 N x N 배열 생성
    result = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            # 90도 회전 규칙
            # 새로운 배열의 (i, j) 위치에는
            # 원본 배열의 (N-1-j, i) 값이 들어감
            #
            # 예)
            # 1 2 3       7 4 1
            # 4 5 6  ->   8 5 2
            # 7 8 9       9 6 3
            result[i][j] = arr[N - 1 - j][i]

    return result


# 입력
T = int(input())

# 여러 테스트 케이스 처리
for test_case in range(1, T + 1):

    N = int(input())

    # N x N 2차원 배열 입력
    arr = [
        list(map(int, input().split()))
        for _ in range(N)
    ]

    # 회전 배열 생성
    # rotate()는 90도 회전 함수이므로 반복 호출하면
    # 180도, 270도 회전 결과를 얻을 수 있음
    rotate90 = rotate(arr)
    rotate180 = rotate(rotate90)
    rotate270 = rotate(rotate180)

    # 테스트 케이스 번호 출력
    print(f"#{test_case}")

    for i in range(N):

        # join() : 문자열 리스트를 하나의 문자열로 결합
        # map(str, 리스트) : 리스트의 각 요소를 문자열로 변환
        #
        # 예)
        # rotate90[i] = [7, 4, 1]
        # map(str, rotate90[i])
        # -> ["7", "4", "1"]
        #
        # ''.join(...)
        # -> "741"
        #
        # 숫자 배열 한 행을 출력 형식에 맞게 문자열로 변환

        print(
            ''.join(map(str, rotate90[i])),
            ''.join(map(str, rotate180[i])),
            ''.join(map(str, rotate270[i]))
        )