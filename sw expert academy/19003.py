"""

문자열 역순 출력은 stringVar[::-1] 로 한다!!!!

"""

tc = int(input())

for test_no in range(tc):
    numOfWords, wordLength = map(int, input().split())
    words = []
    pelindrome_words = []
    result = 0

    # 각 테스트 케이스의 단어들 추가
    for i in range(numOfWords):
        words.append(input())

    # 문자열들을 하나씩 확인, 그 문자가 펠린드롬이면 그 문자의 길이(숫자)를 다른 배열에 추가,펠린드롬 아니면 순서 반대인 문자열 있는지 확인하고 있으면 그 길이만큼 추가.
    for x in words:
        # 현재 문자열이 펠린드롬이면
        if x == x[::-1]:
            # 펠린드롬 배열에 길이를 추가
            pelindrome_words.append(len(x))
        else:  # 펠린드롬 문자열이 아니면
            if x[::-1] in words:  # 순서가 거꾸로인 문자열이 배열 내에 있는지 확인하고
                result += len(x)  # 결과값에 현재 확인중인 문자열 길이 더한다.
    if pelindrome_words:
        result += max(pelindrome_words)  # 펠린드롬 단어들 중 길이가 가장 긴 것을 결과에 추가
    print(f"#{test_no+1} {result}")
