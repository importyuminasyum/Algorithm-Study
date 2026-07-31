def power_calc(N, base):
    power = 0
    while N % base == 0:
        N /= base
        power += 1
    return power

T = int(input())

for test_case in range(1, T+1):
    number = int(input())
    prime = [2, 3, 5, 7, 11]
    result = [0] * 5
	
    for i in range(len(prime)):
        result[i] = power_calc(number, prime[i])
	
    print(f"#{test_case}")

    for s in result:
        print(s)