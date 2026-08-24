# month가 곧 depth\
# 한 노드 마다 세가지 선택지
# 1일 : * day * day_p 하고 다음 노드로
# 1달: * month1_p 다음 노드로
# 3달: * month3_p +3 노드로 건너뛰기
# 종료조건: 12 달 다 돌았을때
# 전달해줄거 & 업데이트 할 거 : 각 누적 price , 그 자식 노드
# 필요한 거: 누적 price 추가할 리스트 ? 어떤 시점? 재귀 끝나고 누적 price도 초기화

def dfs(month, cum_price):
    global answer

    if month >= 12:
        answer = min(answer, cum_price)
        return answer

    dfs(month + 1, cum_price + month_plan[month] * day_p) # 일
    dfs(month + 1, cum_price + month1_p) # 달
    dfs(month + 3, cum_price + month3_p) # 3달

T = int(input())
for tc in range(1, T + 1):
    day_p, month1_p, month3_p, answer = map(int, input().split())
    month_plan = list(map(int, input().split()))
    cum_price = 0
    dfs(0, 0)
    print(f'#{tc} {answer}')