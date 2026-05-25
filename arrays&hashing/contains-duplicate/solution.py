from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = set()
        for num in nums:
            if num in duplicate:
                return True
            else:
                duplicate.add(num)
        return False
    
asdf = Solution()
print(asdf.hasDuplicate([1, 2, 3, 3]))