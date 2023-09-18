# T = int(input())

# for i in range(T):
#     stack = []
#     a = input()
#     for j in a:
#         if j == "(":
#             stack.append(j)
#         elif j == ")":
#             if stack:  # 스택이 비어있지 않으면
#                 stack.pop()
#             else:  # 스택이 비어있는데 pop명령이 오면
#                 print("NO")
#                 break
#         else:  # break문으로 끊기지 않고 수행됬을경우 수행한다
#             if not stack:  # break문으로 안끊기고 스택이 비어있다면 괄호가 다 맞는거다.
#                 print("YES")
#             else:  # break안 걸렸더라도 스택에 괄호가 들어있다면 NO이다.
#                 print("NO")

import sys

n = int(input())

for i in range(n):
    string = sys.stdin.readline()
    stack = []

    for char in string():
        if char == "(":
            stack.append(char)
        elif char == ")":
            if stack:
                stack.pop()
            else:
                print("NO")
                break
        else:
            if not stack:
                print("YES")
            else:
                print("NO")
