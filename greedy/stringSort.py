"""
알파벳 대문자와 숫자 0~9로 이루어진 문자열이 입력으로 주어짐
이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력하고, 그 뒤에 모든 숫자를 더한 값을 이어서 출력한다.
K1KA5CB7 -> ABCKK13
"""

"""
내 코드

string = list(input())
abc = []
numbers = []

for i in string:
    if ord(i) >= 64:
        abc.append(i)
    else:
        numbers.append(i)
print(abc)
print(numbers)

abc = sorted(abc)
numbers = sorted(numbers)
new_string = ""

for i in abc:
    new_string += i
for j in numbers:
    new_string += j

print(new_string)

"""

data = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data:
    # 알파벳이면 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더하기
    else:
        value += int(x)
# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하면 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력(리스트를 문자열로 변환)
print("".join(result))

string = list(input())
abc = []
numbers = []

for i in string:
    if ord(i) >= 64:
        abc.append(i)
    else:
        numbers.append(i)
print(abc)
print(numbers)

abc = sorted(abc)
numbers = sorted(numbers)
new_string = ""

for i in abc:
    new_string += i
for j in numbers:
    new_string += j

print(new_string)

string = list(input())
abc = []
numbers = []

for i in string:
    if ord(i) >= 64:
        abc.append(i)
    else:
        numbers.append(i)
print(abc)
print(numbers)

abc = sorted(abc)
numbers = sorted(numbers)
new_string = ""

for i in abc:
    new_string += i
for j in numbers:
    new_string += j

print(new_string)
