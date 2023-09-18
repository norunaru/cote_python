def recursion(string, left, right):
    global count
    count += 1
    if left >= right:
        return 1
    elif string[left] != string[right]:
        return 0
    else:
        return recursion(string, left + 1, right - 1)


def isPalindrome(
    string,
):
    result = recursion(string, 0, len(string) - 1)
    return result


tc = int(input())

for _ in range(tc):
    count = 0
    string = input()

    print(isPalindrome(string), count)
