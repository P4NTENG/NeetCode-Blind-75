def longestConsecutive(nums: List[int]) -> int:
    nums_set = set(nums)
    if len(nums_set) == 1:
        return 1
    nums_set = sorted(nums_set)
    streak = 1
    longest = 0
    for i in range(1, len(nums_set)):
        if nums_set[i] == nums_set[i-1] + 1:
            streak += 1
        else:
            streak = 1
        if streak > longest:
            longest = streak
    return longest

print(longestConsecutive([0,0]))