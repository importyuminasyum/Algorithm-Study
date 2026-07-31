
T = int(input())

for test_case in range(1, T + 1):
    numbers = [str(i) for i in range(10)]

    init_number = int(input())
    count = 0
    
    while numbers:
        count += 1
        N = str(init_number * count)

        for num in N:
            if num in numbers:
                numbers.remove(num)

    print(f"#{test_case}", N)