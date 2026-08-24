# dp[i] = 1월부터 i월까지의 최소 비용
# dp[i] 결정?
# dp[i - 1] + 일일권
# dp[i - 1] + 한달권
# dp[i - 3] + 세달권

T = int(input())
for tc in range(1, T + 1):
    day_price, month_price, three_month_price, answer = map(int, input().split())
    month_plan = [0]
    month_plan.extend(list(map(int, input().split())))
    dp = [0] * 13 # dp[0] = 아무것도 사지 않았을 때의 초기 비용, base case

    for month in range(1, 13):
        day_cost = month_plan[month] * day_price
        month_cost = month_price
        three_month_cost = three_month_price

        dp[month] = min(dp[month - 1] + day_cost, dp[month - 1] + month_cost)
        if month > 2:
            dp[month] = min(dp[month], dp[month - 3] + three_month_cost)

    answer = min(answer, dp[12])
    print(f'#{tc} {answer}')