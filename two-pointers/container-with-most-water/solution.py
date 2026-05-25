def maxArea(heights: list[int]) -> int:
    answer = 0

    left, right = 0, len(heights)-1

    while left < right:
        answer = max(min(heights[left], heights[right]) * (right-left), answer)
        if heights[left] > heights[right]:
            right -= 1
        else:
            left += 1

    return answer

print(maxArea([1,7,2,5,4,7,3,6]))