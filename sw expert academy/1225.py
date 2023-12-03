from collections import deque

# queue = deque([1, 2, 3, 4, 5])
# queue.rotate(-1)
# print(queue)

for _ in range(10):
    tc = int(input())

    queue = deque(list(map(int, input().split())))

    cycle = 1

    # 0이 없으면 계속 아래 코드 반복
    while 0 not in queue:
        # 현재 사이클의 값만큼 첫번째 인덱스의 값 감소시킨다
        queue[0] -= cycle

        # 0 이하면 0으로 대체
        if queue[0] <= 0:
            queue[0] = 0

        queue.rotate(-1)

        # 사이클 값이 5가 되면 다시 1로 초기화
        if cycle == 5:
            cycle = 1
        else:  # 아니면 cycle값 1 증가
            cycle += 1

    result = " ".join(map(str, queue))
    print(f"#{tc} {result}")


# 1 6 2 2 9 4 1 3 0
# 2 9 7 9 5 4 3 8 0
# 3 8 7 1 6 4 3 5 0
# 4 7 5 8 4 8 1 3 0
# 5 3 8 7 4 4 7 4 0
# 6 6 7 5 9 6 8 5 0
# 7 7 6 8 3 2 5 6 0
# 8 9 2 1 7 3 6 3 0
# 9 4 7 8 1 2 8 4 0
# 10 6 8 9 5 8 5 2 0
