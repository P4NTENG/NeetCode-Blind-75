def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagram_dict = [[word, "".join(sorted(word))] for word in strs]
    grouped = {}
    for anagram in anagram_dict:
        word, sorted_ana = anagram[0], anagram[1]
        grouped.setdefault(sorted_ana, []).append(word)
    return list(grouped.values())


print(groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]))
print(groupAnagrams(["", ""]))
