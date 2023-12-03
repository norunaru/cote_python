"""
list(string) 은 문자열의 한 글자씩 떼어내서 리스트에 넣고,
[string]은 문자열 자체를 리스트에 넣는다.
"""


for tc in range(1, int(input()) + 1):
    data, chance = input().split()  # 숫자판의 정보, 교환횟수
    chance = int(chance)
    N = len(data)

    now = set([data])  # {'123'}
    nxt = set()

    for _ in range(chance):  # chance만큼 반복
        while now:  # 현재 now set가 비어있지 않으면 계속 반복
            s = now.pop()  # 뽑아낸 한 숫자를 s변수라 칭함.
            s = list(s)  # ['1','2','3']처럼 set에서 하나를 뽑아 리스트형으로 변형.
            for i in range(N):  # 완전탐색
                for j in range(i + 1, N):
                    s[i], s[j] = s[j], s[i]
                    nxt.add("".join(s))  # 다음 set에 추가, nxt set을 가지고 다음 반복 수행.
                    s[i], s[j] = s[j], s[i]
        now, nxt = nxt, now

    print("#{} {}".format(tc, max(map(int, now))))
