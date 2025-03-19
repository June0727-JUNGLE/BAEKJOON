n = int(input())

# 입력받은 단어들을 set으로 중복 제거하며 저장
words = set()
for _ in range(n):
    words.add(input().strip())

# set을 list로 변환한 후, 길이와 사전순을 기준
sorted_words = sorted(words, key=lambda x: (len(x), x))

# 정렬된 단어들을 출력
for word in sorted_words:
    print(word)