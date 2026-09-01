def cal_charge_count():
    last_charge = 0
    count = 0

    while last_charge < N:
        for charge_station in range(last_charge + K, last_charge, -1):
            if charge_station >= N:
                return count 
            
            elif charge_station in charge_stations:
                last_charge = charge_station
                count += 1
                break
        else:
            return 0

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charge_stations = list(map(int, input().split()))

    print(f'#{tc} {cal_charge_count()}')