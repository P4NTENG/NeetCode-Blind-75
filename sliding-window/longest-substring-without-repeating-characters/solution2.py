def lengthOfLongestSubstring(s: str) -> int:
    answer = 0
    left = 0
    word_counter = set()
    for right in range(len(s)):
        while s[right] in word_counter:
            word_counter.remove(
                s[left]
            )  # set이 인덱스로도 접근할 수 있고 value 로도 접근할 수 있음
            left += 1

        word_counter.add(s[right])
        answer = max(answer, right - left + 1)

    return answer


print(lengthOfLongestSubstring("zxyzxyz"))
print(lengthOfLongestSubstring("lengthOfLongestSubstring"))
print(lengthOfLongestSubstring("ewwpkew"))
print(lengthOfLongestSubstring("aab"))
print(lengthOfLongestSubstring("ab"))
print(lengthOfLongestSubstring("dvdf"))
