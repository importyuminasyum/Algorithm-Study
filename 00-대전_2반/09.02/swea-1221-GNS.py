#dictionary = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
T = int(input())
for tc in range(1, T+1):
    num, N = input().split()
    words = list(input().split())
    words_index = []
    sorted_words = []

    for word in words:
        words_index.append(numbers.index(word))

    words_index.sort()

    for idx in words_index:
        sorted_words.append(numbers[idx])

    print(num)
    print(*sorted_words)