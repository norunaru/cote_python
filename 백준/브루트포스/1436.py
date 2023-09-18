n = int(input())

count = 0
number = 0
while count != n:
    number += 1
    str_number = str(number)
    if "666" in str_number:
        count += 1
print(number)
