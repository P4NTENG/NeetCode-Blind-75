def search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if (nums[left] <= target <= nums[mid]) or (
            nums[left] > nums[mid] and (target <= nums[mid] or target >= nums[left])
        ):
            right = mid
        else:
            left = mid + 1
    return left if nums[left] == target else -1


print(search([3, 4, 5, 6, 1, 2], 1))
print(search([3, 5, 6, 0, 1, 2], 4))
print(search([4, 5, 6, 7, 8, 1, 2, 3], 8))
