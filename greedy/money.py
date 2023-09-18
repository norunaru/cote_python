#큰 단위의 동전이 작은 단위 화폐의 배수이면 최적해 보장
#큰 단위가 작은 단위의 배수이면 작은 단위의 동전들을 조합해 다른 해가 나올 수 없기 때문.

n = 1260
count = 0

array = [500,100,50,10]

for coin in array:
    count += n // coin
    n %= coin

print(count)

#시간복잡도 분석
# 화폐 종류가 K라고 할 때, 소스코드의 시간 복잡도는 O(K)가 된다.
# 이 알고리즘의 시간 복잡도는 거슬러줘야 하는 금액과 무관하며, 동전의 총 종류에만 영향받는다.