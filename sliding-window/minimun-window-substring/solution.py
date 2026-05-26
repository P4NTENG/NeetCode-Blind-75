def minWindow(s: str, t: str) -> str:
    left = 0
    t_freq = {}
    answer = s
    for char in t:
        t_freq[char] = t_freq.get(char, 0) + 1

    for right in range(0, len(s)):
        check_freq = t_freq.copy()
        for char in s[left : right + 1]:
            check_freq[char] = check_freq.get(char, 0) - 1
        if all(v <= 0 for v in check_freq.values()):
            left += 1

    answer = min(answer, s[left : right + 1])

    return answer


print(minWindow("OUZODYXAZV", "XYZ"))
