for tc in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))

    for _ in range(dump):
        if max(boxes) == min(boxes):
            break

        boxes[boxes.index(max(boxes))] -= 1
        boxes[boxes.index(min(boxes))] += 1

    print(f'#{tc} {max(boxes) - min(boxes)}')