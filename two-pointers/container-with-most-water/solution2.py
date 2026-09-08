def maxArea(heights: list[int]) -> int:
    left, right = 0, len(heights) - 1
    max_area = 0

    while left < right:
        curr_area = (right - left) * min(heights[left], heights[right])
        max_area = max(max_area, curr_area)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_area

if __name__ == "__main__":
    heights = [1,7,2,5,4,7,3,6]
    print(maxArea(heights))
