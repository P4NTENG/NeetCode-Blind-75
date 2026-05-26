def minWindow(s: str, t: str) -> str:
    left = 0
    goal_freq = {}
    freq = {}
    answer = s
    for char in t:
        goal_freq[char] = goal_freq.get(char, 0) + 1

    for right in range(0, len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1

        diff = dict.fromkeys(goal_freq.keys(), 0)

        for k in diff.keys():
            diff[k] = goal_freq[k] - freq.get(k, 0)

        if all(v <= 0 for v in diff.values()):
            freq[s[left]] -= 1
            left += 1

        answer = min(answer, s[left : right + 1])

    return answer


print(minWindow("OUZODYXAZV", "XYZ"))
# 조건을 만족한 문자만 세기
