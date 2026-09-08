def minWindow(s: str, t: str) -> str:
    left = 0
    goal_freq = {}
    curr_freq = {}
    answer = ""
    min_len = float("inf")
    formed = 0

    for char in t:
        goal_freq[char] = goal_freq.get(char, 0) + 1

    for right in range(0, len(s)):
        curr_freq[s[right]] = curr_freq.get(s[right], 0) + 1
        if curr_freq[s[right]] == goal_freq.get(s[right], 0):
            formed += 1

        while formed == len(goal_freq):
            if right - left + 1 < min_len:
                answer = s[left : right + 1]
                min_len = len(answer)

            curr_freq[s[left]] -= 1
            if curr_freq[s[left]] < goal_freq.get(s[left], 0):
                formed -= 1

            left += 1

    return answer


print(minWindow("OUZODYXAZV", "XYZ"))
# 조건을 만족한 문자만 세기
