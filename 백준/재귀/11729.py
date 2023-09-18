def hanoi(n, start, end, other):
    if n == 0:
        return
    hanoi(n - 1, start, other, end)  # n-1개 원판을 초기 1번에서 2번으로 옮김
    print(start, end)  # 가장 큰 원판을 목표지점으로 옮김

    # 여기는 재귀 한번만 실행된다.
    hanoi(n - 1, other, end, start)  # n-1개를 3번 장대로 다시 옮긴다.


n = int(input())

print(2**n - 1)
hanoi(n, 1, 3, 2)
