"""
스택 1,2중에 최소값이 맨 위에 있는게 있다면 pop하여 삭제한다.
스택 1의 최상단이 count값이 아니면 pop하여 스택2에 넣는다
스택 2에 넣을떄 넣는 값이 현재 스택2에 있는 값보다 크면 Sad출력
스택 1,2의 최상단이 모두 count가 
"""
n = int(input())

count = 1
stack1 = list(map(int, input().split()))
stack1.reverse()

stack2 = []

while 1:
    # 모두 다 꺼냈으면 OK
    if stack1 == [] and stack2 == []:
        print("Nice")
        break
    # 스택 1만 들어있을때
    if stack1 and stack2 == []:
        if stack1[-1] == count:
            stack1.pop()
            count += 1
        else:
            stack2.append(stack1.pop())
    # 스택 2만 들어있을떄
    elif stack2 and stack1 == []:
        if stack2[-1] == count:
            stack2.pop()
            count += 1
        else:
            print("Sad")
            break
    # 스택 1,2 모두 들어있을떄
    elif stack1 and stack2:
        # 스택 1의 최상위가 count면
        if stack1[-1] == count:
            stack1.pop()
            count += 1
        # 스택 2의 최상위가 count면
        elif stack2[-1] == count:
            stack2.pop()
            count += 1
        # 스택 1,2의 최상위가 모두 count가 아니라면
        else:
            stack2.append(stack1.pop())
            if stack2[-1] != min(stack2):
                print("Sad")
                break
