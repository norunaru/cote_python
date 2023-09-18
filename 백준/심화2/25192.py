import sys

nickName = set()

count = 0

for i in range(int(input())):
    chat = sys.stdin.readline().rstrip()
    if chat == "ENTER":
        nickName = set()
    elif chat not in nickName:
        count += 1
        nickName.add(chat)

print(count)
