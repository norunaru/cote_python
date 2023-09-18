"""
27*27 리스트
-> 9*9 사각형 9개로 구성
-> 9*9는 3*3 9개로 구성
-> 3*3 은 1*1 9개로 구성
가운데는 비어있음

***
* *
***


"""

n = int(input()) # 27*27 사각형

result = [[[] for j in range(n)] for i in range(n)]
count = 1

def star(n):
    if n != 3:
        star(n//3)
    else:
