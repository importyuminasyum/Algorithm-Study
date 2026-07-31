def slicing(arr):
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            return arr[:i] + arr[i + 2:]
 
T = int(input())

for test_case in range(1, T + 1):
    count = 0
    repeat_word = input()

    while len(repeat_word) != 0:
        count += 1
        slicing(repeat_word)
        print(count, repeat_word)