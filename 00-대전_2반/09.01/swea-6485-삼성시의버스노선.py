from collections import defaultdict
T = int(input())
for tc in range(1, T+1):
    N = int(input())

    bus_stops = defaultdict(int)
    result = []

    for _ in range(N):
        a, b = map(int, input().split())
        for i in range(a, b + 1):
            bus_stops[i] += 1

    print(f"#{tc}", end=" ")
    P = int(input())
    for _ in range(P):
        index = int(input())
        print(bus_stops[index], end=" ")
    print()