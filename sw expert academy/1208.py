"""
index 함수 : 
리스트에서 특정 원소의 인덱스를 반환해주는 함수

1. array.index(x) 리스트에서 x의 인덱스 반환
2. array.index(x, start) 리스트[start:]에서 x의 인덱스 반환
3. array.index(x, start, stop) 리스트[start:stop]에서 x의 인덱스 반환. (stop은 포함되지 않음. 즉 start부터 stop-1까지의 원소들만 포함)

ex) a 리스트에서 10의 인덱스 찾기
a = [11,10,12,13,20,31,11,10,10,11]
print(a.index(10)) 
# 1
"""
# 초기 코드 문제점 : gap이 1이면 그냥 리턴시켰는데
T = 10

for test_case in range(1, T + 1):
    dump_chance = int(input())
    box = list(map(int, input().split()))

    for dump in range(dump_chance):
        HIGH = max(box)
        LOW = min(box)
        gap = HIGH - LOW
        if gap == 1 or gap == 0:
            break

        Hindex = box.index(HIGH)
        Lindex = box.index(LOW)

        # flatten
        box[Hindex] -= 1
        box[Lindex] += 1
        HIGH = max(box)
        LOW = min(box)
        gap = HIGH - LOW

    print(f"#{test_case} {gap}")
