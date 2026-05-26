def lengthOfLongestSubstring(s: str) -> int:
    if len(s) < 2:  # 길이 0 or 1일 때 substring은 제한적
        return len(s)
    substring = s[0]
    max_length = 1

    for i in range(1, len(s)):
        for index, character in enumerate(substring):
            if character == s[i]:
                substring = substring[index + 1 :]
        substring += s[i]

        max_length = max(max_length, len(substring))

    return max_length


print(lengthOfLongestSubstring("zxyzxyz"))
print(lengthOfLongestSubstring("lengthOfLongestSubstring"))
print(lengthOfLongestSubstring("ewwpkew"))
print(lengthOfLongestSubstring("aab"))
print(lengthOfLongestSubstring("ab"))
print(lengthOfLongestSubstring("dvdf"))
