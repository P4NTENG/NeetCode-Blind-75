def findMin(nums: list[int]) -> int:
    left = 0
    right = len(nums) - 1
    while nums[left] > nums[right]:
        mid = (right + left) // 2
        if nums[mid] < nums[right]:
            right = mid  # 왼쪽 선택
        else:
            left = mid + 1  # 오른쪽 선택

    return nums[left]


print(findMin([3, 4, 5, 1, 2]))
# O(logn)
