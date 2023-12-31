# 1이 될 때까지
# 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나 반복적으로 선택하여 수행.
"""
1. N에서 1을 뺸다
2. N을 K로 나눈다

ex) N이 17, K가 4라고 가정하면 1 수행, N이 16이됨. 이후 2과정을 두 번 수행, N이 1이됨. 
이 경우 실행 횟수 3회. 1,2과정을 수행해야 하는 최소 횟수를 구하는 프로그램을 작성하라
"""


"""
가능하면 최대한 많이 나누는 작업이 최적해를 보장하는가?
N이 아무리 큰 수여도, K로 계속 나눈다면 기하급수적으로 빠르게 줄어든다.
다시 말해 K가 2 이상이라면 K로 나누는 것이 1을 빼는 것보다 항상 빠르게 N을 줄일 수 있다. 
-> 또한 N은 항상 1에 도달하게 된다. (최적해 성립)
"""

"""
내 코드
N,K = map(int, input().split())
count = 0
while(N != 1):
    if(N%K == 0):
        N = N % K
        count += 1
    else:
        N = N - 1
        count += 1

print(count)
"""
# / = 나누기, // = 몫 구하기, % = 나머지 구하기
n, k = map(int, input().split())

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k) * k  # N 이하의 K로 나누어지는 값 찾는 연산
    # result는 1을 빼는 연산을 몇 번 하는지 저장하는 변수
    result += n - target
    n = target
    # N이 K보다 작을 떄 (더이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += n - 1
print(result)
