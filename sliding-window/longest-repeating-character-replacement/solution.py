def characterReplacement(s: str, k: int) -> int:
    count = {}
    answer = 0
    left = 0
    most_freq = 0

    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1
        most_freq = max(most_freq, count[s[right]])

        while (right - left + 1) - most_freq > k:  # 나머지들을 k로 처리할 수 있는 동안
            count[s[left]] -= 1
            left += 1

        answer = max(answer, right - left + 1)
    return answer


# print(characterReplacement("XYYX", 2))
# print(characterReplacement("AAABABB", 1))
# print(characterReplacement("BAAA", 0))
print(characterReplacement("AABABBA", 1))
